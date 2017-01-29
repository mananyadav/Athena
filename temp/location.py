import urllib2
import json

# Automatically geolocate the connecting IP
f = urllib2.urlopen('http://freegeoip.net/json/')
json_string = f.read()
f.close()
location = json.loads(json_string)
#print(location)
location_city = location['city']
print 'City : ' + location_city
location_state = location['region_name']
print 'State : ' + location_state
location_country = location['country_name']
print 'Country : ' + location_country
#location_zip = location['zipcode']
