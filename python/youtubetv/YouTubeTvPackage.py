from pprint import pprint

from bs4 import BeautifulSoup
import requests

from StreamingPackage import StreamingPackage


class YouTubeTvPackage(StreamingPackage):
    def __init__(self):
        super().__init__('YouTube TV')

    def scrape_for_channels(self):
        res = requests.get('https://tv.youtube.com/welcome/open/')
        soup = BeautifulSoup(res.text, 'html.parser')
        network_matrix_header = soup.find(name='div', attrs={'class': 'network-matrix__header'})
        network_table = network_matrix_header.find_next_sibling()
        for network_item in network_table.find_all('li'):
            channel = network_item.find('div')['aria-label']
            self.channels[channel] = True

    def scrape_for_premium_channels(self):
        res = requests.get('https://tv.youtube.com/welcome/open/')
        soup = BeautifulSoup(res.text, 'html.parser')
        additional_networks_text = soup.find(name='p', text='Additional networks')
        additional_networks_table = additional_networks_text.find_next_sibling()
        for network_item in additional_networks_table.find_all('li'):
            channel_div = network_item.find('div')
            channel_name = channel_div['aria-label']
            cost = channel_div.find_next_sibling().text
            self.premium_channels[channel_name] = cost

    def scrape_for_price(self):
        self.price = 40

    def scrape_for_simultaneous_streams(self):
        self.num_simultaneous_streams = 3

    def scrape_for_num_profiles(self):
        self.num_profiles = 6

    def scrape_for_support_devices(self):
        self.supported_devices = {
            'Chromecast': True,
            'Roku': True,
            'Apple TV': True,
            'Xbox One': True
        }

    def scrape_for_dvr_info(self):
        self.dvr_cost = 0
        self.dvr_support = 'Cloud DVR with no storage limits'

    def scrape_for_add_ons(self):
        pass



if __name__ == '__main__':
    y = YouTubeTvPackage()
    data = y.scrape_for_data()
    pprint(data)