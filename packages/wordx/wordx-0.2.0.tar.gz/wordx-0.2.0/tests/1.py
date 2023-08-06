import sys
sys.path.append(r'd:\git\inspirare6\wordx\src')
from wordx.sheet import Sheet

sheet = Sheet('123.docx')
# sheet.save_resource('document.xml', 'haha.xml')

sheet.add_footer('123')
sheet.save('3.docx')
exit()
sheet.add_document_relations([{'id': '1', 'type': 'image', 'target': 'media/1.png'}])
sheet.save('2.docx')
exit()
rst = sheet.make_relations([{'id': '1', 'type': 'image', 'target': 'media/1.png'}])
print(rst)