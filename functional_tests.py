from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase, main
from time import sleep


class NewVisitor(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)
    
    def findRows(self, content):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(content, [row.text.split(':', 1)[1].lstrip() for row in rows])

    def tearDown(self):
        self.browser.quit()
        return super().tearDown()

    def test_startAList_retrieveItLater(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        
        # use a post request to store posts
        posts = ('Buy peacock feathers', 'Use them to make a fly')
        for post in posts:
            inputBox = self.browser.find_element_by_id('id_new_item')
            self.assertEqual(inputBox.get_attribute('placeholder'),
                         'Enter a to-do item')
            inputBox.send_keys(post)
            sleep(1)
            inputBox.send_keys(Keys.ENTER)
            self.findRows(post)
            sleep(1)

if __name__ == '__main__':

    main()
