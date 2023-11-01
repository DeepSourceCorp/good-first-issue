from geopy.geocoders import Nominatim

def get_location_from_ip(ip_address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(ip_address)
    if location:
        return location.latitude, location.longitude
    else:
        return None

if __name__ == "__main__":
    ip_address = "8.8.8.8"  # Example IP address (Google's DNS)
    location = get_location_from_ip(ip_address)
    if location:
        print(f"Latitude: {location[0]}, Longitude: {location[1]}")
    else:
        print("Unable to retrieve location.")
