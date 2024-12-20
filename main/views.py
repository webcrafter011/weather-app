from django.shortcuts import render
from pexels_api import API

# import json to load json data to python dictionary
import json

# urllib.request to make a request to api
import urllib.request

PEXELS_API_KEY = 'YOUR_PEXELS_API_KEY_HERE'

def index(request):
    city_image_url = None
    if request.method == "POST":
        city = request.POST["city"]
        """ api key might be expired use your own api_key 
			place api_key in place of appid ="your_api_key_here " """

        # source contain JSON data from API

        source = urllib.request.urlopen(
            "http://api.openweathermap.org/data/2.5/weather?q="
            + city
            + "&appid=YOUR_OPENWEATHER_API_KEY_HERE"
        ).read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data["sys"]["country"]),
            "coordinate": str(list_of_data["coord"]["lon"])
            + " "
            + str(list_of_data["coord"]["lat"]),
            "temp": f"{list_of_data['main']['temp'] - 273.15:.2f} ",
            "pressure": str(list_of_data["main"]["pressure"]),
            "humidity": str(list_of_data["main"]["humidity"]),
            "city_name": city.title(),  # Add this line to include city name
        }
        
        # Fetch city image from Pexels API
        api = API(PEXELS_API_KEY)
        api.search(city, page=1, results_per_page=1)
        photos = api.get_entries()
        if photos:
            city_image_url = photos[0].medium

        data['city_image_url'] = city_image_url
        print(data)
    else:
        data = {}
    return render(request, "index.html", data)
