#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

form= ''
action= 'index_action.py'

def createText(value, var):
    return value + '<input type="text" name="'+var+'"/>  <br />'

def createRadio(opt, var):
    return '<input type="radio" name="'+ var +'" value="'+ opt +'" />'+opt

vars= []

f= file('./config/config.txt','r')
for line in f:
    if line.startswith('::'):
        data= line[2:].rstrip().split('::')
        name= data[0]
        typ= data[1]
        if typ == 'textarea':
            vars.append('var' + str((len(vars)+1)))
            form= form + createText(name, vars[len(vars)-1])
        elif typ.startswith('radio'):
            form= form + name
            vars.append('var' + str((len(vars)+1)))
            for opt in typ[typ.find('(')+1:typ.find(')')].strip().split(','):
                opt= opt.strip()
                form= form + createRadio(opt, vars[len(vars)-1])
            form= form + '<br/>'
        else:
            pass 
f.close()

html= '<form action="'\
    + action + '" method="post" accept-charset="utf-8">'\
    + form\
    + '<input type=hidden name="inputCount" value="'+ str(len(vars)) +'" />'\
    + '<input type="submit" value="Submit" /></form>'

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Co-Excel</title>'
print '</head>'
print '<body>'
#print 'Hello World'
print html
print '</body>'
print '</html>'

