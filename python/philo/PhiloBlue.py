from pprint import pprint

import requests
from bs4 import BeautifulSoup

from StreamingPackage import StreamingPackage


class PhiloBlue(StreamingPackage):
    def __init__(self):
        super().__init__('Philo Blue')

    def scrape_for_channels(self):
        res = requests.get('https://try.philo.com/')
        soup = BeautifulSoup(res.text, 'html.parser')
        i = soup.find('div',attrs={'id': 'mount'})

        lineup_class = soup.find_all(name='div', attrs={'class': 'lineup-ud95d'})
        price = lineup_class.find(name='span', attrs={'class': 'price-1M_hC'}).text
        pass

    def scrape_for_premium_channels(self):
        pass

    def scrape_for_price(self):
        raise NotImplementedError()

    def scrape_for_simultaneous_streams(self):
        self.num_simultaneous_streams = 3

    def scrape_for_num_profiles(self):
        self.num_profiles = 1

    def scrape_for_support_devices(self):
        raise NotImplementedError()

    def scrape_for_dvr_info(self):
        self.dvr_cost = 0
        self.dvr_support = 'Unlimited shows, saved for 30 days'

    def scrape_for_add_ons(self):
        pass

if __name__ == '__main__':
    y = PhiloBlue()
    data = y.scrape_for_data()
    pprint(data)