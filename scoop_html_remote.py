from json2html import *
import json
import io

data = open('remote_results.json','r')
jsonFile = data.read()
foo = json.loads(jsonFile)
table_attr = {"style" : "width:100%", "class" : "table table-striped"}
html = json2html.convert(foo,table_attributes=table_attr)

with io.open("remote_results.html", "w", encoding="utf-8") as ht:
    ht.write(html)