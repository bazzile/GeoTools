import os
import shapefile
import re

# in_folder = r'C:\Users\lobanov\Desktop\Inbox\temp\test'
in_folder = r'U:\PRJ\2017\SOCHI17\4_Архивные_материалы\ГИПРОГОР\500_планшеты\привязка'
footprint_file = r"U:\PRJ\2017\SOCHI17\11_ArcGIS_project\Data\tiles_500.shp"

sf = shapefile.Reader(footprint_file)
shapes = sf.shapes()
size_set = set()
counter = 0
for dirpath, dirnames, filenames in os.walk(in_folder):
    for filename in filenames:
        if re.match('.*-эл\.bmp$', filename, re.IGNORECASE) is not None:
            counter += 1
            print(filename)
            size = os.path.getsize(os.path.join(dirpath, filename))
            size_set.add(size)
            # for i, record in enumerate(sf.records()):
            #     if record[2] == filename:
            #         x = int(round(shapes[i].bbox[0]))
            #         y = int(round(shapes[i].bbox[3]))
            #         print(record, x, y, shapes[i].bbox)
            #         a = 0.04232839956829745
            #         d = 0
            #         b = 0
            #         e = -0.04232973662532756
            #         c = x - 30
            #         f = y + 30
            #         with open(os.path.join(dirpath, os.path.splitext(filename)[0] + '.wld'), 'w') as wf:
            #             wf.write('\n'.join([str(item) for item in [a, d, b, e, c, f]]) + '\n')
            #         break
print(size_set)
print('total files:' + str(counter))
print('unique types:' + str(len(size_set)))
#
#
# for i, record in enumerate(sf.records()):
#     print(record, shapes[i].bbox)
#     dx = shapes[i].bbox[2] - shapes[i].bbox[0]
#     dy = shapes[i].bbox[3] - shapes[i].bbox[1]
#     dx1 = 5906
#     # dx1 = 85000 - 84750
#     dy1 = -5906
#     # dy1 = 21500 - 21750
#     # a = dx / dx1
#     a = 0.04232839956829745
#     d = 0
#     b = 0
#     # e = dy / dy1
#     e = -0.04232973662532756
#
#
#     print(a, e)
#     break
