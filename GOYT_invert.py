import xlrd
from collections import OrderedDict
import json

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('Education Programs.xlsx')
sh = wb.sheet_by_index(0)

header = sh.row_values(0)

import string
def star_num(header):
    knot=[]
    for j in range(len(header)):
        if header[j].lower().rfind('program name')!=-1:
            knot.append(j)
    return

def end_num(header):
    knot=[]
    for j in range(len(header)):
        if header[j].lower().rfind('sex')!=-1:
            knot.append(j)
    return

def records(header, row_values):  # org = org[rownum]
    org = {}
    pro_start = star_num(header)
    pro_end = end_num(header)
    prog = []

    for i in range(0, min(pro_start)):
        if row_values[i] !='':
            org[header[i]]= row_values[i]

    for j in range(len(pro_end)):
        sub_start = pro_start[j]
        sub_end = pro_end[j]

        if row_values[sub_start] != '':
            sub_prog = {}

            for k in range(sub_start, sub_end+1):
                if row_values[k] !='':
                    sub_prog[header[k]] = row_values[k]

            prog.append(sub_prog)


    org['programs'] = prog

    return org

list_org = []
for i in range(1,sh.nrows):
    list_org.append(records(header, sh.row_values(i)))
mydata = {"GOYT": list_org}

j = json.dumps(mydata)

# Write to file
with open('data.json', 'w') as f:
    f.write(j)

