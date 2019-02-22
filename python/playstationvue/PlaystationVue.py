from Provider import Provider


class PlaystationVue(Provider):
    def __init__(self):
        super().__init__('Playstation Vue')
        self.packages['Access']
        self.packages['Core']
        self.packages['Elite']
        self.packages['Ultra']