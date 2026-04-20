import requests
import os

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_coordinates(address):
    """Convert address into latitude & longitude"""
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_MAPS_API_KEY}"
    res = requests.get(url).json()
    if res['status'] == 'OK':
        loc = res['results'][0]['geometry']['location']
        return loc['lat'], loc['lng']
    return None, None

def find_nearby(lat, lng, radius=2000, keyword="shop"):
    """Find nearby shops using Google Places API"""
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&keyword={keyword}&key={GOOGLE_MAPS_API_KEY}"
    res = requests.get(url).json()
    return res.get("results", [])
