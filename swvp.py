import requests
from bs4 import BeautifulSoup
import re

response = requests.get('https://support.apple.com/en-us/100100')
try:
    response.raise_for_status()
except Exception as exc:
    print(f'There was a problem: {exc}')

soup = BeautifulSoup(response.text, 'html.parser')
latest_versions = soup.find_all(string=re.compile("latest version"))
version_num_pattern_obj = re.compile(r'(\d{2})(\.\d+)?(\.\d+)?')
iOS_match_obj = version_num_pattern_obj(latest_versions[0])
macOS_match_obj = version_num_pattern_obj(latest_versions[1])

if macOS_match_obj.group() == platform.mac_ver()[0]:
    print("macOS is up to date.")
elif macOS_match_obj.group() > platform.mac_ver()[0]:
    print(f"You need to update macOS. The current version is {macOS_match_obj.group()}")
else:
    print("... Error of some kind?")

