import googlemaps
from datetime import datetime
import os

apikey = os.environ['GOOGLE_MAPS_API_KEY']
gmaps = googlemaps.Client(key=apikey)

# Geocoding and address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

print "anyway so"
print "the geocode_result is {}".format(geocode_result)
print "the reverse_geocode_result is {}".format(reverse_geocode_result)
print "how soon is now? it is {}".format(now)
print "and the directions_result? {}".format(directions_result)
