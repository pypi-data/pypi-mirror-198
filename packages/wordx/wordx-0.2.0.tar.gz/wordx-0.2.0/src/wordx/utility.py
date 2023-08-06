from lxml import etree
from lxml.builder import E


class ResourceUtility:
    def get_resource(self, res):
        return self.get(f'word/{res}')

    def add_resource(file_path, file_bytes):
        self.add(f'word/{file_path}', file_bytes)

    def add_media(self, filename, file_bytes):
        self.add_resource(f'media/{filename}', file_bytes)

    def get_document(self):
        return self.get_resource('document.xml')

    def save_resource(self, res_path, file_path):
        data = self.get_resource(res_path)
        with open(file_path, 'wb') as f:
            f.write(data)


class RelationUtility:
    def get_relations(self, xml_file):
        return self.get(f'word/_rels/{xml_file}.rels') 

    def get_document_relations(self):
        return self.get_relations('document.xml')

    def save_relations(self, xml_file, relations):
        relations_path = f'word/_rels/{xml_file}.rels'
        self.replace(relations_path, relations)

    def add_relations(self, xml_file, relations_data):
        relations_path = f'word/_rels/{xml_file}.rels'
        relations = self.get_relations(xml_file)
        if relations:
            relation_tree = etree.fromstring(relations)
        else:
            template = b"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                <Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"></Relationships>"""
            relation_tree = etree.fromstring(template)
        for relation_data in relations_data:
            relation_id = relation_data['id']
            relation_type = f"http://schemas.openxmlformats.org/officeDocument/2006/relationships/{relation_data['type']}"
            relation_target = relation_data['target']
            relation_element =  E.Relationship(Id=str(relation_id), Type=relation_type, Target=relation_target)
            relation_tree.append(relation_element)
        relations = etree.tostring(relation_tree)
        self.save_relations(xml_file, relations)
        return self

    def add_document_relations(self, relations_data):
        return self.add_relations('document.xml', relations_data)
