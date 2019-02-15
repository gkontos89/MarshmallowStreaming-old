"""
Base class that describes how to scrape cable streaming information for each provider
"""
from selenium import webdriver


class ScrapeInstructions:
    def __init__(self, provider_name):
        # provider information
        self.provider_name = provider_name
        self.price = None
        self.channels = {}
        self.num_simultaneous_streams = None
        self.num_profiles = None
        self.supported_devices = {}
        self.dvr_support = False
        self.dvr_cost = None
        self.additional_channels = {}

        # web driver
        self.web_driver = webdriver.Chrome()

    def scrape_for_channels(self):
        raise NotImplementedError()
    #
    # def scrape_for_additional_channels(self):
    #     raise NotImplementedError()

    def scrape_for_price(self):
        raise NotImplementedError()

    # def scrape_for_simultaneous_streams(self):
    #     raise NotImplementedError()
    #
    # def scrape_for_num_profiles(self):
    #     raise NotImplementedError()
    #
    # def scrape_for_support_devices(self):
    #     raise NotImplementedError()
    #
    # def scrape_for_dvr_info(self):
    #     raise NotImplementedError()

    def scrape_for_data(self):
        self.scrape_for_channels()
        self.scrape_for_price()
        # self.scrape_for_simultaneous_streams()
        # self.scrape_for_num_profiles()
        # self.scrape_for_support_devices()
        # self.scrape_for_dvr_info()
        self.web_driver.close()
        return self.get_fire_base_format()

    def get_fire_base_format(self):
        info = {
            self.provider_name: {
                'price': self.price,
                'channels': self.channels,
                'additionalChannels': self.additional_channels,
                'numSimultaneousStreams': self.num_simultaneous_streams,
                'numProfiles': self.num_profiles,
                'supportedDevices': self.supported_devices,
                'dvrSupport': self.dvr_support,
                'dvrCost': self.dvr_cost
            }
        }
        return info
