import qrunner

from page.web_page import PatentPage


class TestPatentSearch(qrunner.TestCase):

    def start(self):
        self.page = PatentPage(self.driver)

    def test_pom(self):
        """pom模式代码"""
        self.open()
        self.page.search_input.set_text('无人机')
        self.page.search_submit.click()
        self.assert_in_page('无人机')


if __name__ == '__main__':
    qrunner.main(platform='web', host='https://patents.qizhidao.com/')

