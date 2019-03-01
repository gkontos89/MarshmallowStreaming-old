import os

from hulu.HuluTv import HuluTv
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
credential = credentials.Certificate('marshmallowstreaming-f47a1-firebase-adminsdk-mxzpy-73d1519c44.json')
firebase_admin.initialize_app(credential=credential, options= {
    'databaseURL': 'https://marshmallowstreaming-f47a1.firebaseio.com/'
})

ref = db.reference('cableStreamingProviders')

# Gather provider data and upload to Firebase
providers = dict()
providers['YouTube TV'] = YouTubeTv()
providers['PlayStation Vue'] = PlayStationVue()
providers['Hulu'] = HuluTv()
providers['Sling'] = Sling()
for key, provider in providers.items():
    provider_json = provider.scrape_provider_info()
    ref.child(provider.name).set(provider_json)


