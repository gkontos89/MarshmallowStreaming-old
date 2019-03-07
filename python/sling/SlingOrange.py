import os
from pprint import pprint

from selenium import webdriver

from StreamingPackage import StreamingPackage


class SlingOrange(StreamingPackage):
    def __init__(self):
        super().__init__("Sling Orange")

    def scrape_for_channels(self):
        try:
            self.web_driver = webdriver.Chrome()
            self.web_driver.get('https://www.sling.com/#dyn-grid-plan-tab-1-m-1')
            channel_list = self.web_driver.find_element_by_id('channelList')
            for item in channel_list.find_elements_by_tag_name('li'):
                image_tag = item.find_element_by_tag_name('img')
                self.channels[image_tag.get_attribute('alt')] = True
        except Exception as e:
            self.web_driver.close()
            raise e

    def scrape_for_premium_channels(self):
        pass

    def scrape_for_price(self):
        try:
            self.web_driver.get('https://www.sling.com/#dyn-grid-plan-tab-1-m-1')
            plan_tab = self.web_driver.find_element_by_xpath("//a[@href='#dyn-grid-plan-tab-1-m-1']")
            cost_title = plan_tab.find_element_by_tag_name('h3')
            self.price = int(cost_title.text[1:])
        except Exception as e:
            self.web_driver.close()
            raise e

    def scrape_for_simultaneous_streams(self):
        # https://help.sling.com/en/support/solutions/articles/33000218992-can-i-watch-sling-tv-on-multiple-devices-at-the-same-time-
        self.num_simultaneous_streams = 1

    def scrape_for_num_profiles(self):
        self.num_profiles = 1

    def scrape_for_support_devices(self):
        try:
            self.web_driver.get('https://www.sling.com/#dyn-grid-plan-tab-1-m-1')
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

    def scrape_for_add_ons(self):
        self.add_ons = {
            'Sling Orange': {
                'cost': 5,
                'channels': {
                    'NBA TV': True,
                    'ESPN U': True,
                    'NHL Network': True,
                    'SEC Network': True,
                    'ESPNEWS': True,
                    'Tennis Channel': True,
                }
            },
            'Sling Blue': {
                'Red Zone': True,
                'NBA TV': True,
                'Golf': True,
                'NHL Network': True,
                'Tennis Channel': True,
                'Olympic Channel': True,
            }
        }


if __name__ == '__main__':
    driver_path = os.path.join(os.getcwd(), '../', 'drivers')
    key = 'Path' if 'Path' in os.environ else 'PATH'
    current_path = os.environ[key]
    if driver_path not in current_path:
        os.environ[key] += os.pathsep + driver_path

    # Update permissions on the drivers
    os.chmod(os.path.join(driver_path, 'chromedriver.exe'), 0o777)

    y = SlingOrange()
    data = y.scrape_for_data()
    pprint(data)