"""Provide class to read informations on vector data from file path or object path

The module contains the following class :

    - 'Vector' - Data Vector

"""

from osgeo import ogr
from rok4.Storage import get_data_str, copy
from rok4.Exceptions import *
import os
import tempfile

# Enable GDAL/OGR exceptions
ogr.UseExceptions()

class Vector :
    """A data vector

    Attributes:
        path (str): path to the file/object
        bbox (Tuple[float, float, float, float]): bounding rectange in the data projection
        layers (List[Tuple[str, int, List[Tuple[str, str]]]]) : Vector layers with their name, their number of objects and their attributes
    """

    def __init__(self, path: str, delimiter: str = ";", column_x : str = "x" , column_y : str = "y", column_WKT : str = None) -> None :
        """Constructor method for Shapefile, Geopackage, CSV and GeoJSON

        Args:
            path: path to the file/object
            delimiter (only for CSV) : delimiter between fields
            column_x (only for CSV) : field of the x coordinate
            column_y (only for CSV) : field of the y coordinate
            column_WKT (only for CSV if geometry in WKT) : field of the WKT of the geometry

        Raises:
            MissingEnvironmentError: Missing object storage informations
            StorageError: Storage read issue
            Exception: Wrong column
            Exception: Wrong data in column
            Exception: Wrong format of file
            Exception: Wrong data in the file

        """

        self.path = path

        path_split = path.split("/")

        if path.endswith(".csv") :

            data = get_data_str(path)
            data = data.split("\n")
            for i in range (len(data)) :
                data[i] = data[i].split(delimiter)

            attributes = []
            for i in range (len(data[0])) :
                attributes += [(data[0][i] , "String")]
            layers = [(path_split[-1][:-4], len(data)-1, attributes)]
            self.layers = layers

            geomcol = ogr.Geometry(ogr.wkbGeometryCollection)
            if column_WKT == None :
                try :
                    data_x = data[0].index(column_x)
                except :
                    raise Exception(f"{column_x} is not a column of the CSV")

                try :
                    data_y = data[0].index(column_y)
                except :
                    raise Exception(f"{column_y} is not a column of the CSV")

                for i in range (1, len(data)) :
                    point = ogr.Geometry(ogr.wkbPoint)
                    try :
                        point.AddPoint(float(data[i][data_x]), float(data[i][data_y]))
                    except :
                        raise Exception(f"{column_x} or {column_y} contains data which are not coordinates")
                    geomcol.AddGeometry(point)

            else :
                data_WKT = data[0].index(column_WKT)
                for i in range (1, len(data)) :
                    try :
                        geom = ogr.CreateGeometryFromWkt(data[i][data_WKT])
                    except :
                        raise Exception(f"{column_WKT} contains data which are not WKT")
                    geomcol.AddGeometry(geom)

            self.bbox = geomcol.GetEnvelope()

        else :

            if path.endswith(".shp") :
                with tempfile.TemporaryDirectory() as tmp :
                    tmp_path = tmp + "/" + path_split[-1][:-4]

                    copy(path, "file://" + tmp_path + ".shp")
                    copy(path[:-4] + ".shx", "file://" + tmp_path + ".shx")
                    copy(path[:-4] + ".cpg", "file://" + tmp_path + ".cpg")
                    copy(path[:-4] + ".dbf", "file://" + tmp_path + ".dbf")
                    copy(path[:-4] + ".prj", "file://" + tmp_path + ".prj")

                    dataSource = ogr.Open(tmp_path + ".shp", 0)

            elif path.endswith(".gpkg") :
                with tempfile.TemporaryDirectory() as tmp :
                    tmp_path = tmp + "/" + path_split[-1][:-5]

                    copy(path, "file://" + tmp_path + ".gpkg")

                    dataSource = ogr.Open(tmp_path + ".gpkg", 0)

            elif path.endswith(".geojson") :
                with tempfile.TemporaryDirectory() as tmp :
                    tmp_path = tmp + "/" + path_split[-1][:-8]

                    copy(path, "file://" + tmp_path + ".geojson")

                    dataSource = ogr.Open(tmp_path + ".geojson", 0)

            else :
                raise Exception("This format of file cannot be loaded")

            multipolygon = ogr.Geometry(ogr.wkbGeometryCollection)
            try :
                layer = dataSource.GetLayer()
            except AttributeError :
                raise Exception(f"The content of {self.path} cannot be read")

            layers = []
            for i in range (dataSource.GetLayerCount()) :
                layer = dataSource.GetLayer(i)
                name = layer.GetName()
                count = layer.GetFeatureCount()
                layerDefinition = layer.GetLayerDefn()
                attributes = []
                for i in range(layerDefinition.GetFieldCount()):
                    fieldName =  layerDefinition.GetFieldDefn(i).GetName()
                    fieldTypeCode = layerDefinition.GetFieldDefn(i).GetType()
                    fieldType = layerDefinition.GetFieldDefn(i).GetFieldTypeName(fieldTypeCode)
                    attributes += [(fieldName, fieldType)]
                for feature in layer :
                    geom = feature.GetGeometryRef()
                    if geom != None :
                        multipolygon.AddGeometry(geom)
                layers += [(name, count, attributes)]

            self.layers = layers
            self.bbox = multipolygon.GetEnvelope()
