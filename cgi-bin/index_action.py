#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules for CGI handling 
from openpyxl import load_workbook
import cgi
import os
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import read_conf

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
print form.getvalue('inputCount')

vars= []
while True:
    var= 'var' + str(len(vars) + 1)
    if None == form.getvalue(var, default=None):
        break;
    vars.append(var)

# Open and update the excel file
excel_file= read_conf.read_config('excel_file')
wb= load_workbook(excel_file)
ws=wb.get_active_sheet()

# Add the new row
for row in ws.rows:
    if row[0].value is None:
        count= 0
        for key in vars:
            value= form.getvalue(key, default=None)
            row[count].value=value
            count+= 1
        break

# Seve the updated file
wb.save(excel_file)

print "Content-type:text/html\r\n\r\n"
print "<html>"
print '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h1>"

print '<h2>Successfully updated the excel file!</h2>'
for var in vars:
    print "<p>%s</p>" % form.getvalue(var)

print "</h1>"
print "</body>"
print "</html>"