# -*- coding: utf-8 -*-
import arcpy

import os

workspace = r"U:\PRJ\2017\SNIIGIMS17\3_Ready_for_Deliver\100k\ЦММ\1. База Данных\N44040_otkr.gdb"

domains = arcpy.da.ListDomains(workspace)

for domain in domains:
    if domain.name.upper().startswith('SEM'):
        print('Domain name: {0}'.format(domain.name))
        arcpy.DeleteDomain_management(workspace, domain.name)
        print('Deleted')
