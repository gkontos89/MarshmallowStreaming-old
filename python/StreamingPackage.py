"""
Base class that describes how to scrape cable streaming information for each provider
"""
import os

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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
        self.web_driver = None

    def get_web_driver_wait_handle(self, driver=None, element_type=By.ID, element_string=None, multiple=False, timeout=15):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        if not driver:
            driver = self.web_driver

        if multiple:
            return WebDriverWait(driver=driver, timeout=timeout, ignored_exceptions=ignored_exceptions) \
                .until(expected_conditions.presence_of_all_elements_located((element_type, element_string)))
        else:
            return WebDriverWait(driver=driver, timeout=timeout, ignored_exceptions=ignored_exceptions)\
                .until(expected_conditions.presence_of_element_located((element_type, element_string)))

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
        if self.web_driver is not None:
            self.web_driver.close()

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
