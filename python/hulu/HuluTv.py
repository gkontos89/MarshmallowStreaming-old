from Provider import Provider
from hulu.HuluTvPackage import HuluTvPackage


class HuluTv(Provider):
    def __init__(self):
        super().__init__('Hulu TV')
        self.packages['Hulu TV Package'] = HuluTvPackage()


