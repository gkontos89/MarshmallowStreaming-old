import os
from pprint import pprint

import requests
from bs4 import BeautifulSoup

from Provider import Provider
from directvnow.DirecTvNowPackage import DirecTvNowPackage


class DirecTvNow(Provider):
    def __init__(self):
        super().__init__("DirecTV Now")

    def scrape_provider_info(self):
        package_res = requests.get('https://cdn.directv.com/content/dam/dtv/prod/website_directvnow/modals/compare-packages.html')
        package_soup = BeautifulSoup(package_res.text, 'html.parser')

        # Grab supported devices separately
        device_res = requests.get('https://cdn.directv.com/content/dam/dtv/prod/website_directvnow/modals/devices.html')
        device_soup = BeautifulSoup(device_res.text, 'html.parser')
        device_tags = device_soup.find_all(name='h2')
        supported_devices = dict()
        for d in device_tags:
            supported_devices[d.text] = True

        header = package_soup.find(name='div', attrs={'class': 'row header'})
        packages = header.find_all(name='div', attrs={'class': 'col-custom col-xs-3 col-sm-2'})
        packages.insert(0, header.find(name='div', attrs={'class': 'col-custom col-xs-3 col-sm-2 first'}))
        channel_rows = package_soup.find_all(name='div', attrs={'class': 'row channel'})
        idx = 0
        for p in packages:
            name = p.find(name='div', attrs={'class': 'title'}).text
            # TODO figure out a better hack
            if 'TODO Y' in name:
                name = 'Todo Y Mas'
            elif 'Go' in name and 'Big' in name:
                name = 'Go Big'

            price = p.find(name='div', attrs={'class': 'price'}).text
            d_package = DirecTvNowPackage(name)
            d_package.price = price
            for r in channel_rows:
                channel_name = r.find(name='div', attrs={'class': 'col-xs-12'}).text.strip()
                # TODO move this hack out
                channel_name = channel_name.replace('.', '')
                channel_name = channel_name.replace('/', '')
                channel_name = channel_name.replace('*', '')
                included_ids = r.find_all(name='span')
                if included_ids[idx]['class'][0] == 'checked':
                    d_package.channels[channel_name] = True

            # Supported devices
            d_package.supported_devices = supported_devices
            self.packages[d_package.name] = d_package
            idx += 0

        return super().scrape_provider_info()


if __name__ == '__main__':
    driver_path = os.path.join(os.getcwd(), '../', 'drivers')
    key = 'Path' if 'Path' in os.environ else 'PATH'
    current_path = os.environ[key]
    if driver_path not in current_path:
        os.environ[key] += os.pathsep + driver_path

    # Update permissions on the drivers
    os.chmod(os.path.join(driver_path, 'chromedriver.exe'), 0o777)

    y = DirecTvNow()
    data = y.scrape_provider_info()
    pprint(data)
