from wordx.fake_zip import FakeZip
from wordx.utility import ResourceUtility, RelationUtility
from lxml import etree
from lxml.builder import E
from io import BytesIO
import random


class WordFile(FakeZip, ResourceUtility, RelationUtility):
	def __init__(self, file_path):
		super().__init__(file_path)

	def add_footer(self, footer, relations=None):
		footer_relation_id = random.randint(1000,9999)
		footer_file = f'footer{footer_relation_id}.xml'
		footer_path = f'/word/{footer_file}'
		self.add(footer_path, footer)
		self.register_xml({'path': footer_path,'type': 'footer'})
		self.add_document_relations([{
			'id': footer_relation_id,
			'type': 'footer',
			'target': footer_file
		}])
		if relations:
			self.add_relations(footer_file, relations)
		return f'rId{footer_relation_id}'

	def add_header(self, header_data, header_rels=None):
			header_id = random.randint(1000,9999)
			header_file = f'header{header_id}.xml'
			header_path = f'/word/{header_file}'
			self.add(header_path, header_data)
			self.register_xml({'path': header_path,'type': 'header'})
			self.merge_rels([{
				'id': f'rId{header_id}',
				'type': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/header',
				'target': header_file

			}])
			if header_rels:
				self.add_relations(header_file, header_rels)
			return f'rId{header_id}'

	def register_xml(self, xml_data):
		xml_path = xml_data['path']
		xml_type = xml_data['type']
		content_type_xml = self.get('[Content_Types].xml')
		content_type_tree = etree.fromstring(content_type_xml)
		content_type = f'application/vnd.openxmlformats-officedocument.wordprocessingml.{xml_type}+xml'
		content_type_new_element = E.Override(PartName = xml_path, ContentType = content_type)
		content_type_tree.append(content_type_new_element)
		content_type_xml = etree.tostring(content_type_tree)
		self.replace('[Content_Types].xml', content_type_xml)
		return self
	
	def merge(self, wf):
		"""合并文档
		wf1 = WordFile('cover.docx')
		wf2 = WordFile('catalog.docx')
		rst = wf1.merge(wf2)
		"""
		# 合并资源文件
		wf_rels = wf.make_mask_rels()
		for rels in wf_rels:
			filename = 'word/' + rels['target']
			content = wf.get(filename)
			filename_ = 'word/' + rels['target_']
			self.add(filename_, content)
		# 合并资源映射
		new_rels = self.merge_mask_rels(wf_rels)
		self.replace('word/_rels/document.xml.rels', new_rels)
		# 替换资源id
		document2 = wf.get_document().decode()
		for rels in wf_rels:
			document2 = document2.replace(rels['id'], rels['id_'])
		wf = WordFile(wf.replace('word/document.xml', document2))
		# 合并document
		document1 = self.get_document()
		document2 = wf.get_document()
		etree1 = etree.fromstring(document1)
		etree2 = etree.fromstring(document2)
		etree1_body = etree1[0]
		etree2_body = etree2[0]
		sect_pr = etree1_body[-1]
		etree1_body.remove(sect_pr)
		for element in etree2_body:
			etree1_body.append(element)
		self.replace('word/document.xml', etree.tostring(etree1).decode())
