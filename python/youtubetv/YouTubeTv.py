from Provider import Provider
from youtubetv.YouTubeTvPackage import YouTubeTvPackage


class YouTubeTv(Provider):
    def __init__(self):
        super().__init__('YouTube TV')
        self.packages['YouTube TV Package'] = YouTubeTvPackage()

