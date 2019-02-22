"""
Base class that describes how to scrape cable streaming information for each provider
"""


class StreamingPackage:
    def __init__(self, name):
        self.name = name
        self.price = None
        self.channels = {}
        self.num_simultaneous_streams = None
        self.num_profiles = None
        self.supported_devices = {}
        self.dvr_support = False
        self.dvr_cost = None
        self.additional_channels = {}

    def scrape_for_channels(self):
        raise NotImplementedError()

    def scrape_for_additional_channels(self):
        raise NotImplementedError()

    def scrape_for_price(self):
        raise NotImplementedError()

    def scrape_for_simultaneous_streams(self):
        raise NotImplementedError()

    def scrape_for_num_profiles(self):
        raise NotImplementedError()

    def scrape_for_support_devices(self):
        raise NotImplementedError()

    def scrape_for_dvr_info(self):
        raise NotImplementedError()

    def scrape_for_data(self):
        self.scrape_for_channels()
        self.scrape_for_additional_channels()
        self.scrape_for_price()
        self.scrape_for_simultaneous_streams()
        self.scrape_for_num_profiles()
        self.scrape_for_support_devices()
        self.scrape_for_dvr_info()
        return self.to_json()

    def to_json(self):
        package_info = {
            'name': self.name,
            'pricePerMonth': self.price,
            'channels': self.channels,
            'additionalChannels': self.additional_channels,
            'numSimultaneousStreams': self.num_simultaneous_streams,
            'numProfiles': self.num_profiles,
            'supportedDevices': self.supported_devices,
            'dvrSupport': self.dvr_support,
            'dvrCost': self.dvr_cost
        }
        return package_info
