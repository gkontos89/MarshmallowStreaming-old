"""
Grab credentials
"""
import os
from pprint import pprint

from YouTubeTv import YouTubeTv

# Add web driver executables to path
driver_path = os.path.join(os.getcwd(), 'drivers')
key = 'Path' if 'Path' in os.environ else 'PATH'
current_path = os.environ[key]
if driver_path not in current_path:
    os.environ[key] += os.pathsep + driver_path

# Update permissions on the drivers
os.chmod(os.path.join(driver_path, 'chromedriver.exe'), 0o777)

y = YouTubeTv()
data = y.scrape_for_data()
pprint(data)
