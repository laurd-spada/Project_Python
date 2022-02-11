import phonenumbers
import folium
from phonenumbers import geocoder

KEY = '139003be6fb640db8ebaa8daaa2d70a2'
number = input("Enter a mobile number with the country code included. E.g '+234********' : ")

userNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(userNumber, "en")

print(yourLocation)

# Get service provider

from phonenumbers import carrier

serviceProvider = phonenumbers.parse(number)
print(carrier.name_for_number(serviceProvider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(KEY)

query = str(yourLocation)

results = geocoder.geocode(query)

# if you wish to see the complete provided data form the opencage api cancel the comment on line 30
# print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))

# save map in html file

myMap.save("myloaction.html")
