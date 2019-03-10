import os
from pprint import pprint

from directvnow.DirecTvNow import DirecTvNow
from hulu.HuluTv import HuluTv
from philo.Philo import Philo
from playstationvue.PlayStationVue import PlayStationVue
from sling.Sling import Sling
from youtubetv.YouTubeTv import YouTubeTv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Set up the driver path
driver_path = os.path.join(os.getcwd(), 'drivers')
key = 'Path' if 'Path' in os.environ else 'PATH'
current_path = os.environ[key]
if driver_path not in current_path:
    os.environ[key] += os.pathsep + driver_path

# Update permissions on the drivers
os.chmod(os.path.join(driver_path, 'chromedriver.exe'), 0o777)

# Set up Firebase credentials
credential = credentials.Certificate('marshmallowstreaming-f47a1-firebase-adminsdk-8vumk-d61e8ea8ad.json')
firebase_admin.initialize_app(credential=credential, options={
    'databaseURL': 'https://marshmallowstreaming-f47a1.firebaseio.com/'
})

ref = db.reference('cableStreamingProviders')

# Gather provider data and upload to Firebase
providers = dict()
providers['YouTube TV'] = YouTubeTv()
providers['PlayStation Vue'] = PlayStationVue()
providers['Hulu'] = HuluTv()
providers['Sling'] = Sling()
providers['DirecTvNow'] = DirecTvNow()
providers['Philo'] = Philo()
for key, provider in providers.items():
    provider_json = provider.scrape_provider_info()
    pprint(provider_json)
    ref.child(provider.name).set(provider_json)


