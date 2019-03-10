import os
from pprint import pprint

from selenium import webdriver

from StreamingPackage import StreamingPackage


class PhiloGreen(StreamingPackage):
    def __init__(self):
        super().__init__('Philo Green')

    def scrape_for_channels(self):
        self.web_driver = webdriver.Chrome()
        self.web_driver.get('https://try.philo.com/')
        green_lineup = self.web_driver.find_elements_by_class_name('lineup-ud95d')[0]
        self.price = green_lineup.find_element_by_class_name('price-1M_hC').text
        channels = green_lineup.find_elements_by_class_name('channel-SzvkI')
        for channel in channels:
            self.channels[channel.find_element_by_class_name('name-v22eT').get_attribute('textContent')] = True

    def scrape_for_premium_channels(self):
        pass

    def scrape_for_price(self):
        # Covered in scrape for channels
        pass

    def scrape_for_simultaneous_streams(self):
        self.num_simultaneous_streams = 3

    def scrape_for_num_profiles(self):
        self.num_profiles = 1

    def scrape_for_support_devices(self):
        self.supported_devices = {
            'Apple TV': True,
            'Google Chromecast': True,
            'Amazon Fire TV': True,
            'Roku': True
        }

    def scrape_for_dvr_info(self):
        self.dvr_cost = 0
        self.dvr_support = 'Unlimited shows, saved for 30 days'

    def scrape_for_add_ons(self):
        pass


if __name__ == '__main__':
    driver_path = os.path.join(os.getcwd(), '../', 'drivers')
    key = 'Path' if 'Path' in os.environ else 'PATH'
    current_path = os.environ[key]
    if driver_path not in current_path:
        os.environ[key] += os.pathsep + driver_path

    # Update permissions on the drivers
    os.chmod(os.path.join(driver_path, 'chromedriver.exe'), 0o777)
    y = PhiloGreen()
    data = y.scrape_for_data()
    pprint(data)