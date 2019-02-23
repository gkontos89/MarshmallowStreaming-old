import os
import time
from pprint import pprint
from selenium import webdriver

from StreamingPackage import StreamingPackage


class PlayStationVueElite(StreamingPackage):
    def __init__(self):
        super().__init__('Elite')
        self.web_driver = webdriver.Chrome()

    def scrape_for_channels(self):
        try:
            self.web_driver.get('https://www.playstation.com/en-us/network/vue/channels/?dl=elite')
            # Set location to Chicago
            location_selector = self.web_driver.find_element_by_xpath("//span[@class='item location ']")
            location_selector.click()
            zip_field = self.web_driver.find_element_by_id('zipfield')
            zip_field.send_keys('60074')
            submit_button = self.web_driver.find_element_by_xpath("//input[@value='Update']")
            submit_button.click()
            time.sleep(4)
            # TODO:  sleeps suck, but can't figure this one out

            # Scrape data
            logos_container = self.web_driver.find_element_by_css_selector('.logos-container.clear')
            channels_divs = logos_container.find_elements_by_tag_name('div')
            for channel_div in channels_divs:
                class_name = channel_div.get_attribute('class')
                if 'active' in class_name:
                    channel_name = channel_div.find_element_by_tag_name('img').get_attribute('name')
                    channel_name = channel_name.replace(' logo', '')
                    self.channels[channel_name] = True

            pass
        except Exception as e:
            self.web_driver.close()
            raise e

    def scrape_for_additional_channels(self):
        pass

    def scrape_for_price(self):
        self.price = 59.99

    def scrape_for_simultaneous_streams(self):
        # https://www.playstation.com/en-us/network/vue/faq/supported-devices-and-set-up/#simultaneous-streaming
        self.num_simultaneous_streams = 5

    def scrape_for_num_profiles(self):
        # https://www.playstation.com/en-us/network/vue/faq/subscription/
        self.num_profiles = 10

    def scrape_for_support_devices(self):
        # https://www.playstation.com/en-us/network/vue/faq/supported-devices-and-set-up/
        self.supported_devices = {
            'Amazon Fire TV': True,
            'Roku': True,
            'Apple TV': True,
            'Playstation': True,
            'Google Chromecast': True
        }

    def scrape_for_dvr_info(self):
        # https://www.playstation.com/en-us/network/vue/faq/features/
        self.dvr_cost = 0
        self.dvr_support = '500 episodes, stored for 28 days'


if __name__ == '__main__':
    driver_path = os.path.join(os.getcwd(), '../', 'drivers')
    key = 'Path' if 'Path' in os.environ else 'PATH'
    current_path = os.environ[key]
    if driver_path not in current_path:
        os.environ[key] += os.pathsep + driver_path

    # Update permissions on the drivers
    os.chmod(os.path.join(driver_path, 'chromedriver.exe'), 0o777)

    pva = PlayStationVueElite()
    data = pva.scrape_for_data()
    pprint(data)
