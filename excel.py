# -*- coding: utf-8 -*-
#!/usr/bin/python

from openpyxl import load_workbook

wb= load_workbook('/Users/janfan/Downloads/437.xlsx')
ws=wb.get_active_sheet()
print ws.title

name='张广怡'
phone='1234567890'
isStay='T'

for row in ws.rows:
    if row[0].value is None:
        row[0].value=name
        row[1].value=phone
        row[2].value=isStay
        break
wb.save('/Users/janfan/Downloads/437.xlsx')        