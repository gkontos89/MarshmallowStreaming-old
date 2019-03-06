from StreamingPackage import StreamingPackage


class DirecTvNowPackage(StreamingPackage):
    def __init__(self, name):
        super().__init__(name)

    def scrape_for_channels(self):
        pass

    def scrape_for_additional_channels(self):
        pass

    def scrape_for_price(self):
        pass

    def scrape_for_simultaneous_streams(self):
        self.num_simultaneous_streams = 3

    def scrape_for_num_profiles(self):
        self.num_profiles = 1

    def scrape_for_support_devices(self):
        pass

    def scrape_for_dvr_info(self):
        self.dvr_cost = 0
        self.dvr_support = '20 free hours of DVR storage'
