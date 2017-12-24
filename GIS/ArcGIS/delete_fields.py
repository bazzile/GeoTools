# -*- coding: utf-8 -*-
import arcpy

import os

workspace = r"U:\PRJ\2017\SNIIGIMS17\3_Ready_for_Deliver\25k\ЦММ\1. База Данных\25k_otkr.gdb\Annotations"

fields = arcpy.ListFields(workspace)

for i, field in enumerate(fields):
    print field.name, i

