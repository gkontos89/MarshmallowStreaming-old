from StreamingPackage import StreamingPackage


class PhiloGreen(StreamingPackage):
    def __init__(self):
        super().__init__('Philo Green')

    def scrape_for_channels(self):
        raise NotImplementedError()

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
