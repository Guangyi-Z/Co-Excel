# -*- coding: utf-8 -*-
#!/usr/bin/python

from openpyxl import load_workbook

wb= load_workbook('/Users/janfan/Downloads/437.xlsx')
ws=wb.get_active_sheet()
print ws.title

isEnd=False
for row in ws.rows:
    if row[0].value is None:
        break
    for cell in row:
        print cell.value,
    print