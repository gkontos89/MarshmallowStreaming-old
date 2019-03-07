from StreamingPackage import StreamingPackage


class DirecTvNowPackage(StreamingPackage):
    def __init__(self, name):
        super().__init__(name)

    def scrape_for_channels(self):
        pass

    def scrape_for_premium_channels(self):
        self.premium_channels['HBO'] = '$5/month'
        self.premium_channels['Cinemax'] = '$5/month'
        self.premium_channels['SHOWTIME'] = '$8/month'
        self.premium_channels['STARZ'] = '$8/month'

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

    def scrape_for_add_ons(self):
        pass
