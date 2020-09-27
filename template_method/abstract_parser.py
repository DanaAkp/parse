from abc import ABCMeta, abstractmethod


class AbstractParser(metaclass=ABCMeta):
    def __init__(self, file: str):
        self.file = file

    def read_file(self):
        with open(self.file, 'rt', encoding='utf-8') as file:
            text = file.read()
        return text

    def get_table_tv(self, text_from_file):
        tree = text_from_file

        list_channel = []
        for node in tree.iter('channel'):
            id = node.attrib.get('id')
            child = node.find('./display-name')
            name = child.attrib.get('lang')
            text = child.text
            if name and text:
                list_channel.append({'id': id, 'lang': name, 'name': text})

        list_programm = []
        for node in tree.iter('programme'):
            start = node.attrib.get('start')
            stop = node.attrib.get('stop')
            channel = node.attrib.get('channel')

            child = node.find('./title')
            name_programm = child.text

            start = start[8:10]
            stop = stop[8:10]

            list_programm.append({'id_channel': channel, 'name': name_programm,
                                  'start': start, 'stop': stop})

        table = []
        for chan in list_channel:
            buf = [chan['name']]
            buf_list_dict = []
            for prog in list_programm:
                if chan['id'] == prog['id_channel']:
                    buf_list_dict.append({'time': prog['start'] + '-' + prog['stop'], 'name': prog['name']})
            buf.append(buf_list_dict)
            table.append(buf)

        return table

    def print_table(self):
        table = self.get_table_tv(self.read_file())
        for i in table:
            print(i[0])
            for j in i[1]:
                print(j['time'], j['name'])
            break

    @abstractmethod
    def get_type_file(self):
        pass
