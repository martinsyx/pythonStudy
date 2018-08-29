import urllib
import re
class Spider():
    url = "https://www.panda.tv/cate/lol"
    root_pattern  = '<div class="video-info">([\S\s]*?)</div>'
    def __fetch_content(self):
        r =urllib.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls)
       
        # print(htmls)
        return htmls
    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        print(root_html)
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)

spider = Spider()
spider.go()