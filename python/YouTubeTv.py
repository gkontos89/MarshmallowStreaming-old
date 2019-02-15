from selenium import webdriver

from ScrapeInstructions import ScrapeInstructions


class YouTubeTv(ScrapeInstructions):
    def __init__(self):
        super().__init__('YouTube TV')

    def scrape_for_channels(self):
        self.web_driver.get('https://tv.youtube.com/welcome/open/')
        network_matrix = self.web_driver.find_element_by_class_name('network-matrix__cells')
        network_cells = network_matrix.find_elements_by_class_name('network-matrix__cells-cell')
        for network_cell in network_cells:
            div = network_cell.find_element_by_tag_name('div')
            channel = div.get_attribute('aria-label')
            print(channel)
            self.channels[channel] = True

    def scrape_for_price(self):
        # self.web_driver.get('https://tv.youtube.com/welcome/open/')
        pass

