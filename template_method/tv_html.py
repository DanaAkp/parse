from template_method.abstract_parser import AbstractParser
from lxml import html


class TVHTML(AbstractParser):
    def get_table_tv(self, text_from_file):
        table = []

        tree = html.fromstring(text_from_file)
        list_div_grid = tree.xpath(
            '//div[@class = "p-channels__item js-channel-item js-module" or @class="p-channels__item js-channel-item"]')

        for elem in list_div_grid:
            channel = elem.xpath('div[@class="p-channels__item__info"]/div/a/text()')[0]  # название канала
            buf_in_table = [channel]
            buf_list_dict = []
            buf = elem.xpath(
                'div[@class = "p-programms"]/div/div[@class = "p-programms__item p-programms__item_onair" or @class = "p-programms__item" '
                'or @class = "p-programms__item p-programms__item_has-genre p-programms__item_genre139 js-genre-139"]')

            for i in buf:
                t = i.xpath(
                    'div[@class = "p-programms__item__inner"]/span[@class = "p-programms__item__time"]/span/text()')[0]
                n = i.xpath(
                    'div[@class = "p-programms__item__inner"]/span[@class = "p-programms__item__name"]/span/text()')[0]
                buf_list_dict.append({'time': t, 'name': n})
            buf_in_table.append(buf_list_dict)
            table.append(buf_in_table)
        return table

    def get_type_file(self):
        print('html - файл')
