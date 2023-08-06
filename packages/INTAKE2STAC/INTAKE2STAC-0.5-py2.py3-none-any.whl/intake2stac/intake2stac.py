"""Main module."""
import json
import os
import random
from datetime import datetime

import intake
import pandas as pd
import pystac
import requests
import yaml
from pypgstac.db import PgstacDB
from pypgstac.load import Loader, Methods
from pystac.extensions.datacube import (
    DatacubeExtension,
    DimensionType,
    HorizontalSpatialDimension,
    Variable,
)
from shapely import geometry

from intake2stac import config_pgstac, funcs


class Convertor(object):
    def __init__(
        self,
        catalog,  # Intake YAML catalog address
        driver=None,  # Driver for the data source
        stac=False,  # Permitting creation of STAC catalogs
        stac_dir=None,  # Directory saving of created STAC catalogs
        stac_id=None,  # STAC catalog ID
        stac_description=None,  # STAC catalog description
        stac_catalog_dynamic=False,  # Choosing STAC catalog type between Static and Dynamic
    ):
        self.stac_id = stac_id
        self.driver = driver
        drivers = []  # list of all existance driver in the INTAKE catalog
        self.catalog = dict()  # Main STAC catalog
        color_arr = [
            "\033[95m",
            "\033[94m",
            "\033[96m",
            "\033[92m",
            "\033[93m",
            "\033[91m",
            "\033[0m",
            "\033[1m",
            "\033[4m",
        ]  # Colorization of lines

        # Getting details of Intake YAML file:
        req = requests.get(catalog)
        content = req.text
        intake_service = yaml.safe_load(content)
        print("Intake catalog details:")
        print(" Version: ", intake_service["metadata"]["version"])
        drivers = [
            intake_service["sources"][v]["driver"].capitalize()
            for i, v in enumerate(list(intake_service["sources"]))
        ]
        print(" Drivers: ", " , ".join(list(dict.fromkeys(drivers))))
        [
            print(
                random.choice(color_arr),
                "Parameter: ",
                v,
                " | Description: ",
                intake_service["sources"][v]["description"],
                " | urlpath: ",
                intake_service["sources"][v]["args"]["urlpath"],
            )
            for i, v in enumerate(list(intake_service["sources"]))
        ]

        cat = intake.open_catalog(catalog)
        if stac is not False:
            # Main STAC catalog for linking other items and collections
            self.catalog[funcs.replacement_func(stac_id)] = pystac.Catalog(
                id=stac_id,
                description="[" + stac_description + "](" + str(catalog) + ")",
            )
            # Creation of STAC Collections with empy Spatial and Temporal values
            for i, v in enumerate(list(intake_service["sources"])):
                self.catalog[funcs.replacement_func(v)] = pystac.Collection(
                    id=v,
                    extent=pystac.Extent(spatial=None, temporal=None),
                    description="[Link to Zarr S3 bucket]("
                    + intake_service["sources"][v]["args"]["urlpath"]
                    + ")",
                )

            # Ingesting STAC Items into STAC Collection
            array = [
                self.read_yml(cat, v)
                for i, v in enumerate(list(cat))
                if cat[v].entry.describe().get("driver")[0].lower()
                == self.driver.lower()
            ]
            # Saving STAC Catalog in local storage
            if len(array) != 0:
                self.catalog[funcs.replacement_func(stac_id)].normalize_hrefs(
                    os.path.join(stac_dir, "stac")
                )
                self.catalog[funcs.replacement_func(stac_id)].save(
                    catalog_type=pystac.CatalogType.SELF_CONTAINED
                )
            print(
                list(
                    self.catalog[
                        funcs.replacement_func(stac_id)
                    ].get_children()
                )
            )
        if stac_catalog_dynamic is not False:
            config_pgstac.run_all()  # This enables the confiduration of pgSTAC
            # Opening created STAC Catalog
            f = open(os.path.join(stac_dir, "stac/catalog.json"))
            catalog_json = json.load(f)
            # pgSTAC database will be loaded here
            loader = Loader(db=PgstacDB(dsn=""))
            # Each collection and item that are linked to the catalog through 'links' is extracted.
            for dc in catalog_json["links"]:
                if dc["rel"] == "item":
                    try:
                        loader.load_items(
                            str(
                                os.path.join(
                                    stac_dir,
                                    "stac/" + dc["href"].replace("./", ""),
                                )
                            ),
                            Methods.insert,
                        )
                    except:
                        continue
                    print("|____", dc["href"])
                # 'child' means Collection in Catalog json file
                if dc["rel"] == "child":
                    self.dynamic_ingester(
                        loader,
                        dc["href"],
                        stac_dir,
                        "stac/" + dc["href"].replace("./", ""),
                    )

    def dynamic_ingester(self, loaderx, param, stac_dirx, address_coll):
        """This is a function for ingesting collections
        into pgSTAC specifically for nested datasets"""

        f = open(os.path.join(stac_dirx, address_coll))
        collection_josn_path = os.path.join(stac_dirx, address_coll)
        collection_josn_data = json.load(f)

        item_collection_list = [
            ci["rel"] for ci in collection_josn_data["links"]
        ]

        if (
            "child" in item_collection_list
        ):  # To ensure collection exists in 'links'
            item_collection_list = []  # Considered empty to prevent recursion

            for ci in collection_josn_data["links"]:
                if ci["rel"] == "child":
                    try:
                        self.dynamic_ingester(
                            loaderx,
                            ci["href"],
                            stac_dirx,
                            collection_josn_path.replace(
                                "collection.json", "/"
                            )
                            + ci["href"].replace("./", ""),
                        )
                    except:
                        continue
        else:
            item_collection_list = []  # Considered empty to prevent recursion
            loaderx.load_collections(
                str(os.path.join(stac_dirx, collection_josn_path)),
                Methods.insert,
            )
            print(param)
            for ci in collection_josn_data["links"]:
                if ci["rel"] == "item":
                    try:
                        loaderx.load_items(
                            str(
                                os.path.join(
                                    stac_dirx,
                                    collection_josn_path.replace(
                                        "collection.json", "/"
                                    )
                                    + ci["href"].replace("./", ""),
                                )
                            ),
                            Methods.insert,
                        )
                        print("|____", ci["href"])
                    except:
                        continue

    def read_yml(self, cat, v):
        """
        Getting STAC Item attributes and ingesting STAC Items into STAC Collections
        and at the end connecting all Collection into STAC Catalog
        """
        collection_bbox = [0, 0, 0, 0]
        collection_time = [0, 0]

        variables = {}
        dimensions = {}
        print(cat[v].urlpath)

        print(list(cat[v].to_dask()))

        for i1, v1 in enumerate(list(cat[v].to_dask().coords)):
            if cat[v].to_dask().coords[v1].values != []:
                if "time" in v1:
                    mint = datetime.strptime(
                        pd.Timestamp(min(cat[v].to_dask().coords[v1].values))
                        .to_pydatetime()
                        .strftime("%Y-%m-%dT%H:%M:%S.%f"),
                        "%Y-%m-%dT%H:%M:%S.%f",
                    )
                    maxt = datetime.strptime(
                        pd.Timestamp(max(cat[v].to_dask().coords[v1].values))
                        .to_pydatetime()
                        .strftime("%Y-%m-%dT%H:%M:%S.%f"),
                        "%Y-%m-%dT%H:%M:%S.%f",
                    )
                    collection_time = [mint, maxt]
                if "lat" in v1:
                    collection_bbox[1] = min(
                        cat[v].to_dask().coords[v1].values
                    )
                    collection_bbox[3] = max(
                        cat[v].to_dask().coords[v1].values
                    )
                elif "lon" in v1:
                    collection_bbox[0] = min(
                        cat[v].to_dask().coords[v1].values
                    )
                    collection_bbox[2] = max(
                        cat[v].to_dask().coords[v1].values
                    )

                print(
                    v,
                    v1,
                    min(cat[v].to_dask().coords[v1].values),
                    max(cat[v].to_dask().coords[v1].values),
                )
        if float(collection_bbox[0]) > 180 or float(collection_bbox[2]) > 180:
            collection_bbox[0] = str(float(collection_bbox[0]) - 180)
            collection_bbox[2] = str(float(collection_bbox[2]) - 180)

        bbox_x = list(map(str, collection_bbox))
        collection_bbox = list(map(float, collection_bbox))
        print(collection_bbox)
        print(bbox_x)
        footprint = geometry.Polygon(
            [
                [bbox_x[0], bbox_x[1]],
                [bbox_x[0], bbox_x[3]],
                [bbox_x[2], bbox_x[3]],
                [bbox_x[2], bbox_x[1]],
            ]
        )
        item = pystac.Item(
            id=funcs.replacement_func(cat[v].name),
            geometry=geometry.mapping(footprint),
            bbox=bbox_x,
            datetime=collection_time[1],
            properties={},
        )

        item.add_asset(
            key="S3 XML address",
            asset=pystac.Asset(
                href=cat[v].urlpath,
                # title=without_slash,
                media_type="application/XML",
            ),
        )
        item.add_asset(
            key="Jupyter",
            asset=pystac.Asset(
                href="https://nbviewer.org/urls/codebase.helmholtz.cloud/cat4kit/automated-jupyter-viewer/-/raw/main/"
                + funcs.replacement_func(cat[v].name)
                + ".ipynb",
                # title=without_slash,
                media_type="application/Jupyter",
            ),
        )
        # Add auxiliary information to items
        item.common_metadata.start_datetime = collection_time[0]
        item.common_metadata.end_datetime = collection_time[1]
        item.common_metadata.description = (
            "[Link to the data in Climedata Zarr S3 Bucket]("
            + cat[v].urlpath
            + ")"
        )
        # applying datacube extension to items
        cube = DatacubeExtension.ext(item, add_if_missing=True)
        # Creating dimension and varibles to datacube extension
        for i2, v2 in enumerate(list(cat[v].to_dask().data_vars)):
            print(list(cat[v].to_dask().data_vars[v2].coords))

            variables[v2] = Variable(
                dict(
                    type="data",
                    description=v2,
                    dimensions=list(cat[v].to_dask().data_vars[v2].coords),
                )
            )

        for i3, v3 in enumerate(list(cat[v].to_dask().coords)):
            if list(cat[v].to_dask().coords[v3].values) != []:
                if "lon" in v3:
                    extend_ = [
                        collection_bbox[0],
                        collection_bbox[2],
                    ]
                    type_ = DimensionType.SPATIAL.value
                    description_ = "longitude"
                    axis_ = "x"
                elif "lat" in v3:
                    extend_ = [
                        collection_bbox[1],
                        collection_bbox[3],
                    ]
                    type_ = DimensionType.SPATIAL.value
                    description_ = "latitude"
                    axis_ = "y"
                elif "time" in v3:
                    extend_ = [collection_time[0], collection_time[1]]
                    type_ = DimensionType.TEMPORAL.value
                    description_ = "time"
                    axis_ = "time"

                dimensions[v3] = HorizontalSpatialDimension(
                    properties=dict(
                        axis=axis_,
                        extent=extend_,
                        description=description_,
                        reference_system="epsg:4326",
                        type=type_,
                    )
                )

        cube.apply(dimensions=dimensions, variables=variables)
        temporal_extent = pystac.TemporalExtent(intervals=[collection_time])

        spatial_extent = pystac.SpatialExtent(bboxes=[collection_bbox])
        self.catalog[funcs.replacement_func(v)].extent = pystac.Extent(
            spatial=spatial_extent, temporal=temporal_extent
        )
        self.catalog[funcs.replacement_func(v)].add_item(item)
        self.catalog[self.stac_id].add_child(
            self.catalog[funcs.replacement_func(v)]
        )
