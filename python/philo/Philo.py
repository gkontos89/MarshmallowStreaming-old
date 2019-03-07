from Provider import Provider
from philo.PhiloBlue import PhiloBlue
from philo.PhiloGreen import PhiloGreen


class Philo(Provider):
    def __init__(self):
        super().__init__("Philo")
        self.packages['Philo Blue'] = PhiloBlue()
        self.packages['Philo Green'] = PhiloGreen()

