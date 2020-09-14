from django.shortcuts import render

import os

# home view
def home(request):
  import json
  import requests
  meteoserver_apikey = os.getenv('METEOSERVER_APIKEY')
  if request.method == "POST":
    zipcode = request.POST['zipcode']
    api_request = requests.get("https://meteoserver.nl/api//getij.php?"+ zipcode + "&key=" + meteoserver_apikey)
    try:
      standenlijst = []
      api_result = json.loads(api_request.content)
      standenlijst = api_result['jsongetij'][1]['tijden']
    except Exception as e:
      api_result = "Error..."
    
    if api_result['jsongetij'][0]['plaats'] == "IJmuiden Buitenhaven":
      category_color = "usg"
    else:
      category_color = "good"

    return render(request, 'home.html', {'api_result': api_result, 'category_color': category_color, 'standenlijst': standenlijst})
  else:
    # den helder: lat=52.971683&long=4.781498
    # IJmuiden  : lat=52.4577508&long=4.3891164
    api_request = requests.get("https://meteoserver.nl/api//getij.php?lat=52.4577508&long=4.3891164&key=" + meteoserver_apikey)
    try:
      standenlijst = []
      api_result = json.loads(api_request.content)
      standenlijst = api_result['jsongetij'][1]['tijden']
    except Exception as e:
      api_result = "Error..."
    
    if api_result['jsongetij'][0]['plaats'] == "IJmuiden Buitenhaven":
      category_color = "usg"
    else:
      category_color = "good"

    return render(request, 'home.html', {'api_result': api_result, 'category_color': category_color, 'standenlijst': standenlijst})

# about view
def about(request):
  return render(request, 'about.html', {})