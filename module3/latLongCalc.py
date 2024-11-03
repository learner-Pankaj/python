import math

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Radius of Earth in kilometers (use 6371 for kilometers or 3956 for miles)
    radius_of_earth_km = 6371
    distance = radius_of_earth_km * c

    return distance

# Example usage
lat1 = float(input("Enter latitude of first location: "))
lon1 = float(input("Enter longitude of first location: "))
lat2 = float(input("Enter latitude of second location: "))
lon2 = float(input("Enter longitude of second location: "))

# Calculate distance
distance = haversine(lat1, lon1, lat2, lon2)
print(f"Distance between the two locations: {distance:.2f} km")
