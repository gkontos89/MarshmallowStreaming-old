from YouTubeTv import YouTubeTv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Set up Firebase credentials
credential = credentials.Certificate('marshmallowstreaming-f47a1-firebase-adminsdk-mxzpy-73d1519c44.json')
firebase_admin.initialize_app(credential=credential, options= {
    'databaseURL': 'https://marshmallowstreaming-f47a1.firebaseio.com/'
})

ref = db.reference('cableStreamingProviders')

# Gather provider data and upload to Firebase
providers = dict()
providers['YouTube TV'] = YouTubeTv()
for key, provider in providers.items():
    provider_json = provider.scrape_provider_info()
    ref.child(provider.name).set(provider_json)


