from template_method.tv_xml import TVXML
from template_method.tv_html import TVHTML


class API_TV:
    def __init__(self, file: str):
        self.file = file
        self.parser = self.get_parser()
        self.get_average_time(self.get_difference_time())

    def is_html(self):
        if self.file.find('.html'):
            return True
        return False

    def get_parser(self):
        if self.is_html():
            return TVHTML(self.file)
        return TVXML(self.file)

    def get_table(self):
        return self.parser.get_table_tv(self.parser.read_file())

    def get_difference_time(self):
        time = []
        table = self.get_table()
        for i in table:
            buf = [i[0]]
            buf_list = []
            l = i[1]
            for j in range(1, len(l)):
                h = int(l[j]['time'][:2])-int(l[j-1]['time'][:2])
                m = int(l[j]['time'][3:5])-int(l[j-1]['time'][3:5])
                buf_list.append(h * 60 + m)
            buf.append(buf_list)
            time.append(buf)

        return time

    def get_average_time(self, time):
        for i in time:
            buf = 0
            if len(i[1]) != 0:
                for j in i[1]:
                    buf += abs(j)
                print(i[0], ": ", buf/len(i[1]))
