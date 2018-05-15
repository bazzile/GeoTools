# -*- coding: utf-8 -*-

# Import arcpy module
import arcpy
import os
import unicodedata
from collections import defaultdict

target_db = r"U:\PRJ\2017\VNIIGAZ17\5_GIS\1_Arc_Database\vniigaz_25k_clean.gdb"
sxf_export_db = r"U:\PRJ\2017\VNIIGAZ17\5_GIS\0_Panorama_files\sxf2gdb_test.gdb"

arcpy.env.workspace = target_db

geometry_type_list = [
    {'full': 'POINT', 'short': 'pnt'}, {'full': 'LINE', 'short': 'lin'}, {'full': 'POLYGON', 'short': 'pol'}]

layers_dict_list = defaultdict(list)

for (n, dataset) in enumerate(arcpy.ListDatasets()):
    if n > 2:
        break
    print(dataset)
    for fc in arcpy.ListFeatureClasses("*", "", dataset):
        geometry_type = arcpy.Describe(fc).shapeType.encode('ascii', 'ignore')
        print(fc, geometry_type)
        subtypes = arcpy.da.ListSubtypes(fc)
        for stcode, stdict in subtypes.iteritems():
            print('Code: {0}'.format(stcode))
            # layers_dict_list[fc.encode('ascii', 'ignore')].append(stcode)
            layers_dict_list[
                os.path.join(dataset.encode('ascii', 'ignore'), fc.encode('ascii', 'ignore'))].append(stcode)
            # print(os.path.join(dataset.encode('ascii', 'ignore'), fc.encode('ascii', 'ignore')), stcode)

print(layers_dict_list)

dummy_field_names = [
    'SHEET_NUMBER', 'SXF_KEY', 'SHAPE_Length', 'SHAPE_Area', 'OBJECTID', 'SHAPE', 'SxfId', 'RscName', 'UpdateAuthor',
    'UpdateDate', 'UpdateTime']

arcpy.env.workspace = sxf_export_db

fieldMappings = arcpy.FieldMappings()

filled_attr_layer_list = defaultdict(set)

for (n, dataset) in enumerate(arcpy.ListDatasets()):
    for fc in arcpy.ListFeatureClasses("*", "", dataset):
        geometry_type = arcpy.Describe(fc).shapeType
        print("Feature class: {}".format(fc))
        fieldList = [field for field in arcpy.ListFields(fc) if field.name not in dummy_field_names]
        cursor = arcpy.SearchCursor(fc)
        for row in cursor:
            class_id = int(row.getValue('class_id').encode('ascii', 'ignore'))
            for layer_key, classcode_value in layers_dict_list.items():

                print('Class id {} not in {}'.format(class_id, classcode_value))
                # print(key, value, class_id)
                if class_id in classcode_value:
                    print("=" * 80)

                    append_layer = os.path.join(sxf_export_db, dataset, fc)
                    target_layer = os.path.join(target_db, layer_key)
                    print("Appending\nsrc layer: {}\nto target layer: {}".format(append_layer, target_layer))

                    # This object looks like the empty grid of fields
                    # you see when you first open the append tool in the toolbox
                    fieldmappings = arcpy.FieldMappings()

                    # Like when you manually choose a layer in the toolbox and it adds the fields to grid
                    fieldmappings.addTable(target_layer)
                    fieldmappings.addTable(append_layer)

                    #####Lets map fields that have different names!
                    list_of_fields_we_will_map = []
                    # Lets chuck some tuples into the list we made
                    list_of_fields_we_will_map.append(('class_id', 'class_id'))
                    # list_of_fields_we_will_map.append(('SwissBankNo', 'RetirementFundAccNo'))
                    # list_of_fields_we_will_map.append(('Balance', 'Amount'))

                    for field_map in list_of_fields_we_will_map:
                        # Find the fields index by name. e.g 'TaxPin'
                        field_to_map_index = fieldmappings.findFieldMapIndex(field_map[0])
                        # Grab "A copy" of the current field map object for this particular field
                        field_to_map = fieldmappings.getFieldMap(field_to_map_index)
                        # Update its data source to add the input from the the append layer
                        field_to_map.addInputField(append_layer, field_map[1])
                        # We edited a copy, update our data grid object with it
                        fieldmappings.replaceFieldMap(field_to_map_index, field_to_map)

                    # Create a list of append datasets and run the the tool
                    inData = [append_layer]
                    arcpy.Append_management(inData, target_layer, field_mapping=fieldmappings, schema_type='NO_TEST',
                                            )

                    # TODO добавить проверку на геометрию
                    # TODO копировать объект в этот слой

                    print('Done!')

# TODO list items that have no match, list items that has filled attributes

#
#
#             for field in fieldList:
#                 if row.getValue(field.name) is not None:
#                     if field.type == 'String':
#                         print(field.name, row.getValue(field.name).encode('ascii', 'ignore'))
#                         filled_attr_layer_list[fc].add(field.name)
#                     else:
#                         print(field.name, row.getValue(field.name))
#                         filled_attr_layer_list[fc].add(field.name)
#
#
# for layer, fields in filled_attr_layer_list.iteritems():
#     print layer + ': ', ', '.join(fields)
#
#
# print('List of non-empty attributes:')
# for layer, fields in filled_attr_layer_list.iteritems():
#     print layer + ': ', ', '.join(fields)



# for key, value in layers_dict_list.items():
#     if 43200000 in value:
#         print(key)
