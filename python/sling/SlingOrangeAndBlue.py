import os
from pprint import pprint

from selenium import webdriver

from StreamingPackage import StreamingPackage


class SlingOrangeAndBlue(StreamingPackage):
    def __init__(self):
        super().__init__("Sling Orange And Blue")
        self.web_driver = webdriver.Chrome()

    def scrape_for_channels(self):
        try:
            self.web_driver.get('https://www.sling.com/#dyn-grid-plan-tab-3-y-1')
            channel_list = self.web_driver.find_element_by_id('channelList')
            for item in channel_list.find_elements_by_tag_name('li'):
                image_tag = item.find_element_by_tag_name('img')
                self.channels[image_tag.get_attribute('alt')] = True
        except Exception as e:
            self.web_driver.close()
            raise e

    def scrape_for_additional_channels(self):
        pass

    def scrape_for_price(self):
        try:
            self.web_driver.get('https://www.sling.com/#dyn-grid-plan-tab-3-y-1')
            plan_tab = self.web_driver.find_element_by_xpath("//a[@href='#dyn-grid-plan-tab-3-y-1']")
            cost_title = plan_tab.find_element_by_tag_name('h3')
            self.price = int(cost_title.text[1:])
        except Exception as e:
            self.web_driver.close()
            raise e

    def scrape_for_simultaneous_streams(self):
        self.num_simultaneous_streams = 4

    def scrape_for_num_profiles(self):
        self.num_profiles = 1

    def scrape_for_support_devices(self):
        try:
            self.web_driver.get('https://www.sling.com/#dyn-grid-plan-tab-3-y-1')
            device_carousel = self.web_driver.find_element_by_class_name('js-device-carousel-large')
            for item in device_carousel.find_elements_by_tag_name('img'):
                self.supported_devices[item.get_attribute('alt')] = True
        except Exception as e:
            self.web_driver.close()
            raise e

    def scrape_for_dvr_info(self):
        # https://www.sling.com/value/dvr
        self.dvr_cost = 5
        self.dvr_support = '50 hours of recording'


if __name__ == '__main__':
    driver_path = os.path.join(os.getcwd(), '../', 'drivers')
    key = 'Path' if 'Path' in os.environ else 'PATH'
    current_path = os.environ[key]
    if driver_path not in current_path:
        os.environ[key] += os.pathsep + driver_path

    # Update permissions on the drivers
    os.chmod(os.path.join(driver_path, 'chromedriver.exe'), 0o777)

    y = SlingOrangeAndBlue()
    data = y.scrape_for_data()
    pprint(data)