from Provider import Provider
from playstationvue.PlayStationVueAccess import PlayStationVueAccess
from playstationvue.PlayStationVueCore import PlayStationVueCore
from playstationvue.PlayStationVueElite import PlayStationVueElite
from playstationvue.PlayStationVueUltra import PlayStationVueUltra


class PlayStationVue(Provider):
    def __init__(self):
        super().__init__('Playstation Vue')
        self.packages['Access'] = PlayStationVueAccess()
        self.packages['Core'] = PlayStationVueCore()
        self.packages['Elite'] = PlayStationVueElite()
        self.packages['Ultra'] = PlayStationVueUltra()
