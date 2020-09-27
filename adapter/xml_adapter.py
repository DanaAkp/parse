from template_method.tv_html import TVHTML
from template_method.tv_xml import TVXML


class XMLAdapter(TVHTML):   # сюда отправляем xml файл
    def __init__(self, file: str):
        super().__init__(file)
        self.xml_ = TVXML(file)

    def read_file(self):
        return self.xml_.read_file()

    def get_table_tv(self, text_from_file):
        return self.xml_.get_table_tv(text_from_file)
