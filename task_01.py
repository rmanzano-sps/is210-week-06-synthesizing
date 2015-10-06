#!usr/bin/env python
# -*- coding: utf-8 -*-
"""function that can analyze arbitrary lists of families and return a total headcount for your
caterer as well as a total number of tables needed.code"""

def get_party_stats(families, table_size = 6):
    total_guest = 0
    total_table = 0
    for family in families:
        total_guest += len(family)
        total_table += -(-len(family) // table_size)
    return (total_guest, total_table)  
