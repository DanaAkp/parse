from template_method.tv_xml import TVXML
from template_method.tv_html import TVHTML

from adapter.xml_adapter import XMLAdapter

from facade.API import API_TV

# h = TVHTML('html_/test.html')
# h.print_table()
# h.get_type_file()
#
# x = TVXML('xml_/xmltv.xml')
# x.print_table()
# x.get_type_file()
#
# adapt = XMLAdapter('xml_/xmltv.xml')
# adapt.print_table()
# adapt.get_type_file()

api = API_TV('html_/test.html')
