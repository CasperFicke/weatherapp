from django.shortcuts import render

import os

# home view
def home(request):
  import json
  import requests
  meteoserver_apikey = os.getenv('METEOSERVER_APIKEY')
  api_request = requests.get("https://meteoserver.nl/api//getij.php?lat=52.4577508&long=4.3891164&key=" + meteoserver_apikey)
  try:
    standenlijst = []
    api_result = json.loads(api_request.content)
    standenlijst = api_result['jsongetij'][1]['tijden']
  except Exception as e:
    api_result = "Error..."
  return render(request, 'home.html', {'api_result': api_result, 'standenlijst': standenlijst})

# about view
def about(request):
  return render(request, 'about.html', {})