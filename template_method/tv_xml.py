from template_method.abstract_parser import AbstractParser
from xml.etree import ElementTree


class TVXML(AbstractParser):
    def read_file(self):
        with open(self.file, 'rt', encoding='utf-8') as file:
            tree = ElementTree.parse(file)
        return tree

    def get_type_file(self):
        print('xml - файл')
