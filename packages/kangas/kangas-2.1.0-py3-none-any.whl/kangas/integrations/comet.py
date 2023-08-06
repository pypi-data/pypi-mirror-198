# -*- coding: utf-8 -*-
######################################################
#     _____                  _____      _     _      #
#    (____ \       _        |  ___)    (_)   | |     #
#     _   \ \ ____| |_  ____| | ___ ___ _  _ | |     #
#    | |  | )/ _  |  _)/ _  | |(_  / __) |/ || |     #
#    | |__/ ( ( | | | ( ( | | |__| | | | ( (_| |     #
#    |_____/ \_||_|___)\_||_|_____/|_| |_|\____|     #
#                                                    #
#    Copyright (c) 2022 Kangas Development Team      #
#    All rights reserved                             #
######################################################

import datetime
import io
import json
import os
import sqlite3
import zipfile

from ..utils import ProgressBar


def get_comet_type(asset_type):
    """
    Mapping from datagrid Asset type to Comet
    asset type.
    """
    if asset_type == "Text":
        return "text-sample"
    else:
        # Audio, Image, Video, Curve, etc.
        return asset_type.lower()


def import_from_comet(path, name, options):
    from comet_ml import API

    from kangas import DataGrid, Image

    api = API()

    if path.count("/") == 2:
        # FIXME: id or name:
        workspace, project_name, experiment_id = path.split("/", 2)
        experiments = [api.get_experiment(workspace, project_name, experiment_id)]
    elif path.count("/") == 1:
        workspace, project_name = path.split("/", 1)
        experiments = api.get_experiments(workspace, project_name)
    elif path:
        workspace = path
        experiments = api.get_experiments(workspace)
    else:
        raise Exception(
            "PATH should be one of: workspace/project/exp, workspace/project, or workspace"
        )

    if name.endswith(".datagrid"):
        name = name[:-9]

    if os.path.isfile(name + ".datagrid"):
        os.remove(name + ".datagrid")

    dg = DataGrid(
        name=name,
        columns=[
            "Image",
            "File name",
            "Created at",
            "File size",
            "Step",
            "Comet asset id",
            "Tags",
            "Comet experiment id",
        ],
    )
    for experiment in experiments:
        asset_list = experiment.get_asset_list()

        # FIXME: temporary workaround until comet supports metadata on images:
        metadata_json_list = [
            asset
            for asset in asset_list
            if asset["fileName"].endswith("-datagrid-metadata.json")
        ]

        # Assuming just one datagrid per experiment for now:
        metadata = {}
        if len(metadata_json_list) > 0:
            print("Logged metadata found")
            # Map of Comet asset Id to kangas metadata:
            metadata = experiment.get_asset(
                metadata_json_list[0]["assetId"], return_type="json"
            )
        for asset in asset_list:
            # FIXME: pass in type(s) to get; currently gets all known
            # FIXME: each type will need its own column
            if asset["type"] == "image":
                # FIXME: workaround; overwrites comet-provided data, if any
                if asset["assetId"] in metadata:
                    if asset["metadata"]:
                        asset["metadata"].update(metadata[asset["assetId"]])
                    else:
                        asset["metadata"] = metadata[asset["assetId"]]
                dg.append(
                    [
                        Image(source=asset["link"], metadata=asset["metadata"]),
                        asset["fileName"],
                        datetime.datetime.fromtimestamp(asset["createdAt"] / 1000),
                        asset["fileSize"],
                        asset["step"],
                        asset["assetId"],
                        asset["tags"] if asset["tags"] else None,  # list, []
                        asset["experimentKey"],
                    ]
                )
            # FIXME: append audio, video, curve, JSON, etc.
    dg.save()


def export_to_comet(path, name, options):
    """
    Create the SQLite database, zip it, and log it to
    an experiment.

    Args:

    * path - (str, optional)
    * name - (str) the name of the datagrid file
    * options: "output_dir" (optional, str) the name of the output directory
        for the zipped datagrid file
    """
    import comet_ml

    output_dir = options.get("output_dir", ".")

    comet_ml.config._init(should_prompt_user=True)
    if comet_ml.config.get_config("comet.api_key") is None:
        raise Exception(
            "You will need to set your Comet API key; see: https://www.comet.com/docs/v2/guides/getting-started/quickstart/"
        )

    base_name, ext = os.path.splitext(name)
    zip_file = os.path.join(output_dir, base_name + "-comet.datagrid.zip")
    output = os.path.join(output_dir, base_name + "-comet.datagrid")

    if os.path.isfile(output):
        os.remove(output)

    if os.path.isfile(zip_file):
        os.remove(zip_file)

    conn = sqlite3.connect(output)
    cur = conn.cursor()
    cur.execute("ATTACH DATABASE '{name}' as original;".format(name=name))
    rows = conn.execute("SELECT * from original.assets;")

    if path is None:
        experiment = comet_ml.Experiment()
        experiment.log_other("Created from", "kangas")
    elif path.count("/") == 2:
        # FIXME: id or name:
        workspace, project_name, experiment_id = path.split("/", 2)
        experiment = comet_ml.ExistingExperiment(previous_experiment=experiment_id)
    elif path.count("/") == 1:
        workspace, project_name = path.split("/", 1)
        experiment = comet_ml.Experiment(workspace=workspace, project_name=project_name)
        experiment.log_other("Created from", "kangas")
    else:
        project_name = path
        experiment = comet_ml.Experiment(project_name=project_name)
        experiment.log_other("Created from", "kangas")

    # Log all of the assets:
    asset_map = {}
    metadata_map = {}
    for row in ProgressBar(rows.fetchall(), "Uploading DataGrid assets to comet.com"):
        asset_id, asset_type, asset_data, asset_metadata, asset_thumbnail = row
        # FIXME: convert annotations to comet-style
        metadata = json.loads(asset_metadata)
        if isinstance(asset_data, str):
            binary_io = io.StringIO(asset_data)
        else:
            binary_io = io.BytesIO(asset_data)
        file_name = metadata.get("filename", "%s-%s" % (asset_type, asset_id))
        comet_type = get_comet_type(asset_type)
        if "step" in metadata:
            step = metadata["step"]
        else:
            step = 0

        try:
            asset_results = experiment.log_image(
                binary_io,
                name=file_name,
                annotations=metadata["annotations"],
                step=step,
            )
            asset_results["assetId"] = asset_results["imageId"]
        except Exception:
            asset_results = experiment._log_asset(
                binary_io,
                file_name=file_name,
                copy_to_tmp=True,  # NOTE: comet_ml no longer supports False
                asset_type=comet_type,
                metadata=metadata,
                step=step,
                framework="kangas",
            )

        asset_map[asset_id] = asset_results
        # Comet asset ID -> kangas asset metadata
        metadata_map[asset_map[asset_id]["assetId"]] = metadata

    ## FIXME: workaround until comet support metadata on image assets
    experiment.log_asset_data(metadata_map, "%s-datagrid-metadata.json" % base_name)

    cur.execute("CREATE TABLE datagrid AS SELECT * from original.datagrid;")
    cur.execute("CREATE TABLE metadata AS SELECT * from original.metadata;")
    cur.execute(
        "CREATE TABLE assets AS SELECT asset_id, asset_type, asset_metadata, asset_thumbnail from original.assets;"
    )
    cur.execute("CREATE TABLE settings AS SELECT * from original.settings;")
    cur.execute("ALTER TABLE assets ADD COLUMN asset_data BLOB;")
    rows = list(
        conn.execute("SELECT asset_id, asset_metadata from original.assets;").fetchall()
    )

    for asset_id, asset_metadata_string in ProgressBar(
        rows, "Updating DataGrid metadata"
    ):
        comet_asset_id = asset_map[asset_id]["assetId"]
        asset_metadata = json.loads(asset_metadata_string)
        asset_metadata["source"] = asset_map[asset_id]["web"]
        asset_metadata["cometAssetId"] = comet_asset_id
        cur.execute(
            "UPDATE assets SET asset_metadata = ? WHERE asset_id = ?;",
            (json.dumps(asset_metadata), asset_id),
        )
    conn.commit()

    try:
        # zlib may not be installed
        with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(output)
    except Exception:
        # if not, we'll just "zip" it without compression:
        with zipfile.ZipFile(zip_file, "w") as zipf:
            zipf.write(output)

    print("Saved local DataGrid as %r" % output)
    print("Saved local compressed DataGrid as %r" % zip_file)
    experiment._log_asset(zip_file, file_name=zip_file, asset_type="datagrid")
    experiment.end()
