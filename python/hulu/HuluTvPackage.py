from pprint import pprint

import requests
from bs4 import BeautifulSoup

from StreamingPackage import StreamingPackage


class HuluTvPackage(StreamingPackage):
    def __init__(self):
        super().__init__('Hulu Tv Package')

    def scrape_for_channels(self):
        res = requests.get('https://www.hulu.com/live-tv')
        soup = BeautifulSoup(res.text, 'html.parser')
        network_list = soup.find(name='div', attrs={'class': 'network-list'})
        for channel_icon in network_list.find_all('img'):
            self.channels[channel_icon['alt']] = True

    def scrape_for_premium_channels(self):
        res = requests.get('https://www.hulu.com/live-tv')
        soup = BeautifulSoup(res.text, 'html.parser')
        value_props = soup.find_all(name='div', attrs={'id': 'value-props'})[1]
        container = value_props.find(name='div')
        for prop in container.find_all(name='div', recursive=False):
            prop_name = prop.find(name='img')['alt']
            details = prop.find_all(name='div')[2].text
            cost = details[details.find('$'): details.find('/month') + len('/month')]
            self.premium_channels[prop_name] = cost

    def scrape_for_price(self):
        res = requests.get('https://www.hulu.com/live-tv')
        soup = BeautifulSoup(res.text, 'html.parser')
        plans = soup.find(name='div', attrs={'id': 'plans'})
        header = plans.find(name='h4')
        price_string = header.text
        self.price = float(price_string[1:-1])

    def scrape_for_simultaneous_streams(self):
        self.num_simultaneous_streams = 2

    def scrape_for_num_profiles(self):
        self.num_profiles = 1

    def scrape_for_support_devices(self):
        res = requests.get('https://www.hulu.com/live-tv')
        soup = BeautifulSoup(res.text, 'html.parser')
        for device_title in soup.select('p[class*="supported-devices--device-title"]'):
            self.supported_devices[device_title.text] = True

    def scrape_for_dvr_info(self):
        self.dvr_support = True
        self.dvr_cost = 15

    def scrape_for_add_ons(self):
        pass


if __name__ == '__main__':
    y = HuluTvPackage()
    data = y.scrape_for_data()
    pprint(data)
