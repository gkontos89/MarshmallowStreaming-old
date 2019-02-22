class Provider:
    def __init__(self, name):
        self.name = name
        self.packages = dict()

    def scrape_provider_info(self):
        for package_key, package in self.packages.items():
            package.scrape_for_data()

        return self.to_json()

    def to_json(self):
        package_json = dict()
        for package_key, package in self.packages.items():
            package_json[package_key] = package.to_json()
        return {
            'name': self.name,
            'packages': package_json
        }

