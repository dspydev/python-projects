!pip install geopy
!pip install folium

from geopy.geocoders import Nominatim
from geopy.distance import distance
import folium

# Ask for the geographic coordinates of each position
while True:
    try:
        lat1 = float(input("Latitude of the first position (in degrees, between -90 and 90): "))
        if not -90 <= lat1 <= 90:
            raise ValueError("Latitude must be between -90 and 90.")
        lon1 = float(input("Longitude of the first position (in degrees, between -180 and 180): "))
        if not -180 <= lon1 <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        lat2 = float(input("Latitude of the second position (in degrees, between -90 and 90): "))
        if not -90 <= lat2 <= 90:
            raise ValueError("Latitude must be between -90 and 90.")
        lon2 = float(input("Longitude of the second position (in degrees, between -180 and 180): "))
        if not -180 <= lon2 <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        break
    except ValueError as e:
        print("Error:", str(e))
        continue

# Calculate the distance between the two positions
try:
    d = distance((lat1, lon1), (lat2, lon2)).km
except ValueError as e:
    print('Error:', str(e))
    exit()

# Get the country name corresponding to each position
geolocator = Nominatim(user_agent="geoapiExercises")
location1 = geolocator.reverse(f"{lat1}, {lon1}", language="en")
location2 = geolocator.reverse(f"{lat2}, {lon2}", language="en")

if 'address' not in location1.raw or 'country' not in location1.raw['address']:
    country1 = "Unknown"
else:
    country1 = location1.raw['address']['country']

if 'address' not in location2.raw or 'country' not in location2.raw['address']:
    country2 = "Unknown"
else:
    country2 = location2.raw['address']['country']

# Create a map with markers for each position and a red line between the two
m = folium.Map(location=[(lat1 + lat2) / 2, (lon1 + lon2) / 2], zoom_start=4)
folium.Marker([lat1, lon1], tooltip=country1, popup=f"Position 1 ({lat1:.2f}°, {lon1:.2f}°)").add_to(m)
folium.Marker([lat2, lon2], tooltip=country2, popup=f"Position 2 ({lat2:.2f}°, {lon2:.2f}°)").add_to(m)
folium.PolyLine(locations=[(lat1, lon1), (lat2, lon2)], color="red", weight=2, tooltip=f"Distance: {d:.2f} km").add_to(m)

# Add a red icon for the first position marker
icon1 = folium.Icon(color='red', icon='info-sign')
folium.Marker([lat1, lon1], tooltip=country1, popup=f"Position 1 ({lat1:.2f}°, {lon1:.2f}°)", icon=icon1).add_to(m)

# Add a blue icon for the second position marker
icon2 = folium.Icon(color='blue', icon='info-sign')
folium.Marker([lat2, lon2], tooltip=country2, popup=f"Position 2 ({lat2:.2f}°, {lon2:.2f}°)", icon=icon2).add_to(m)

# Adjust the map size to fit the markers
m.fit_bounds(m.get_bounds())

# Display the distance and the map with markers
print("-------------------------------------------------------")
print("Calculating the distance between two geographic positions")
print("-------------------------------------------------------")
print(f"The distance between the two positions is {d:.2f} kilometers.")
print("The first position is indicated by the red marker.")
print("The second position is indicated by the blue marker.")
print(f"Position 1 ({country1}) is located at {lat1:.2f}° latitude and {lon1:.2f}° longitude.")
print(f"Position 2 ({country2}) is located at {lat2:.2f}° latitude and {lon2:.2f}° longitude.")
print("-------------------------------------------------------")

m
