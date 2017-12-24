# -*- coding: utf-8 -*-
import arcpy
from arcpy import env

env.workspace = r'P:\WORLD_TILE'
shp = 'FUTURE_TILE_ID.shp'

# SHAPE@ - system field with geometry
fields = ['tile_id', 'SHAPE@']

with arcpy.da.UpdateCursor(shp, fields) as cur:
    for row in cur:
        ext = row[1].extent
        LL = ext.lowerLeft
        ll_lon, ll_lat = int(LL.X), int(LL.Y)
        if ll_lat >= 0:
            n_or_s = 'N'
        else:
            n_or_s = 'S'
        if ll_lon >= 0:
            e_or_w = 'E'
        else:
            e_or_w = 'W'

        full_name = n_or_s + str(abs(ll_lat)).zfill(3) + e_or_w + str(abs(ll_lon)).zfill(3) + '_AVE_DSM.tif'
        row[0] = full_name
        cur.updateRow(row)
