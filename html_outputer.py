# encoding=utf-8
class HtmlOutputer:
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        fout = open('output.txt',"w",encoding="utf-8")
        fout.write("<!DOCTYPE html>")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<tb>%s</tb>"% data['url'].encode('utf-8'))
            fout.write("<tb>%s</tb>"% data['title'].encode('utf-8'))
            fout.write("<tb>%s</tb>"% data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()