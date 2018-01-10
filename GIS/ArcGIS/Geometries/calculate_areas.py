# -*- coding: utf-8 -*-
import arcpy
from arcpy import env

env.workspace = r'F:\BANS17\1_Empty\1'
shp = 'N000E009_AVE_DSM.shp'

fc = shp
# arcpy.AddField_management(fc,"area","Double")
expression1 = "{0}".format("!Shape!.getArea('GEODESIC', 'SQUAREKILOMETERS')")
print(arcpy.CalculateField_management(fc, "Shape", expression1, "PYTHON", ))