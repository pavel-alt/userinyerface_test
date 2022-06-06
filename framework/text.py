from framework.base_element import BaseElement


class Text(BaseElement):
    def read_text(self):
        return self.find_element_by_xpath().text
