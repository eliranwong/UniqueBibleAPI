import sys, requests, pprint
import urllib.parse

cmd = urllib.parse.quote(" ".join(sys.argv[1:]))

url = f"https://bible.gospelchurch.uk/json?cmd={cmd}"

response = requests.get(url)
response.encoding = "utf-8"
data = response.json()

pprint.pprint(data)