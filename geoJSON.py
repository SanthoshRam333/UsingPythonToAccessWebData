import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    print(address)
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address':address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure to Retrive ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    results = tree.findall('result')
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    location = js['results'][0]['formatted_address']
    print(location)
