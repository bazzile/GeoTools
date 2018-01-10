# -*- coding: utf-8 -*-
import arcpy
from arcpy import env
import os

root_dir = r'F:\BANS17\1_Empty'
dst_dir = r'F:\BANS17\EMP'

# iterate over directories in root_dir
for dirname in [dirname for dirname in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, dirname))]:
    merged_shape = os.path.join(dst_dir, dirname + '.shp')
    if os.path.isfile(merged_shape):  # checking if contents have already been merged
        print('Merged shape {} already exists, skipping...'.format(dirname + '.shp'))
    else:
        env.workspace = os.path.join(root_dir, dirname)
        shplist = arcpy.ListFeatureClasses('*.shp')
        print('Merging files in {}'.format(dirname))
        arcpy.Merge_management(shplist, merged_shape)
