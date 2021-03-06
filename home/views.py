from django.shortcuts import render,HttpResponse,render_to_response,redirect
from chatterbot import ChatBot
from home.models import Weather
import json
from urllib.request import urlopen
from chatterbot.trainers import ListTrainer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from translator import get_in_languages
from .models import Soil,answer,post_question
from .forms import farmer_signup,discuss_form,comment_form
from django.template import RequestContext
import pandas as pd
# Create your views here.




	# from chatterbot import ChatBot

	# chatbot = ChatBot(
	#         'Agribot',
	#         trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
	#     )

	# # Train based on the english corpus
	# chatbot.train("chatterbot.corpus.english")
	# return HttpResponse('done training')

def train_from_text(chatbot, path):
    conversation = []
    with open(path, 'r') as f:
        while True:
            line1 = f.readline()
            line2 = f.readline()
            if not line2:
                break
            else:
                conversation.append(line1)
                conversation.append(line2)
    chatbot.set_trainer(ListTrainer)
    chatbot.train(conversation)


def test(request):
	print("test")
	chatbot = ChatBot(
    'Agribot',
    trainer='chatterbot.trainers.ListTrainer'
	)
	
	train_from_text(chatbot,'/home/mayank/Desktop/crops/wheat.txt')
	#response = chatbot.get_response('tell me something about coffee')

	return HttpResponse("done")




# this function generates soil profile by using SoilGrids API 


def getWeather(lat,lon):
	url = "https://api.darksky.net/forecast/7ed498b034dd29bc99c446de31588b03/"+str(lat)+","+str(lon)
	v = urlopen(url).read()
	v = json.loads(v.decode('utf-8'))
	i = v['currently']
	
	o = Weather()	
	o.lat = lat
	o.lon = lon
	timestamp = i['time']
	precipIntensity =  i['precipIntensity']
	precipProbability =  i['precipProbability']
	dewPoint =  i['dewPoint']
	humidity =  i['humidity']
	pressure =  i['pressure']
	windSpeed =  i['windSpeed']
	cloudCover =  i['cloudCover']
	uvIndex =  i['uvIndex']
	ozone =  i['ozone']    

	o.timestamp = timestamp
	o.precipIntensity = precipIntensity
	o.precipProbability = precipProbability
	o.dewPoint = dewPoint
	o.humidity = humidity
	o.pressure = pressure
	o.windSpeed = windSpeed
	o.cloudCover = cloudCover
	o.uvIndex = uvIndex
	o.ozone = ozone
	o.save()

def save_weather(request):
	lt=[12.0,12.25,12.5,12.75,13.0,13.25,13.5,13.75,14.0,14.25,14.5,14.75,15.0,15.25,15.5,15.75,16.0,16.25]
	ln=[80.0,80.25,80.5,80.75,81.0,81.25,81.5,81.75,82.0,82.25,82.5,82.75,83.0,83.25,83.5,83.75,84.0,84.25,84.5,84.75]

	for i in lt:
		for j in ln:
			getWeather(i,j)
	



def index(request):
	return render(request,'home/index_new.html')


@csrf_exempt
def chat_query(request):
	chatbot = ChatBot(
    'Agribot',
    trainer='chatterbot.trainers.ListTrainer'
	)
	
	query_obj = json.loads(request.body.decode('utf-8'))
	text = str(query_obj['query'])
	response = {}
	try:
		response["english"] = str(chatbot.get_response(text))
	except:
		response["english"] = "I dont know what you are saying"
	x = get_in_languages(response["english"])
	response["tamil"] = x["tamil"]
	response["hindi"] = x["hindi"]
	response["telgu"] = x["telgu"]

	return JsonResponse(response)


def chat_admin(request):
	return render(request,'home/admin_chat.html')

def administrator(request):
	return render(request,'home/ADMINISTRATOR.html')

def index(request):
	return render(request,'home/index_new.html')

def contact(request):
	return render(request,'home/contact.html')

def weather(request):
	return render(request,'home/weather.html')



def signup(request):
	context=RequestContext(request)
	registered=False
	if request.method=='POST':	
		
		form=farmer_signup(data=request.POST)

		if form.is_valid():
			form.save()
			registered=True
			
			return redirect('/home/')
		else:
			print(form.errors)

	else:
		form=farmer_signup()
	return render_to_response('home/signup.html',{'form':form,'registered':registered},context)


def ask_question(request):
  context=RequestContext(request)
  registered=False
  if request.method=='POST':	

    form=discuss_form(data=request.POST)

    if form.is_valid():
      form.save()
      registered=True
      return redirect('/home/post/')
    else:
      print(form.errors)

  else:
    form=discuss_form()

  return render_to_response('home/forum.html',{'form':form,'registered':registered},context)

def post(request):
  post=post_question.objects.all()
  post2 = answer.objects.all()
  return render(request,'home/forum.html',{'post':post,'post2':post2})


def add_comment(request,ans_id):
  form2=discuss_form()
  ans=get_object_or_404(post_question,pk=ans_id)
  form=comment_form(request.POST)
  print(form.is_valid())
  if form.is_valid():
    user_name=form.cleaned_data['user_name']
    comment=form.cleaned_data['comment']
    add=answer()
    add.user_name=user_name
    add.comment=comment
    add.pub_date = datetime.datetime.now()
    ob=post_question.objects.get(id=ans_id)
    add.ques=ob
    add.save()
    return redirect('/home/post/')

  return render(request, 'home/forum.html', {'ans': ans, 'form': form,'form2':form2})

def singleblog(request):
    return render(request,'home/singleblog.html')

def blog(request):
    return render(request,'home/blog.html')






def dashboard(request):
	return render(request,'home/dashboard.html')


def organic_farming(request):
	return render(request,'home/organic_farming.html')


from rapidconnect import RapidConnect
import json
from urllib.request import urlopen

def get_weather(city):
	rapid = RapidConnect("default-application_5a68be4ce4b09c6b06da6c08", "551285ee-2f7d-45e2-8471-bc4aaae024ed")
	result = rapid.call('YahooWeatherAPI', 'getWeatherForecast', { 
	'location': city	,
	'filter': ['item.condition,item.forecast'] 
	})
	return result


@csrf_exempt
def weather_forecast(request):
	city = 'Raipur'
	print("City detected : ",city)
	results = get_weather(city)
	print(results)
	forecast = []
	for i in range(0,10):
		entry = {}
		entry['high'] = results['query']['results']['channel'][i]['item']['forecast']['high']
		entry['low'] = results['query']['results']['channel'][i]['item']['forecast']['low']
		entry['text'] = results['query']['results']['channel'][i]['item']['forecast']['text']
		entry['day'] = results['query']['results']['channel'][i]['item']['forecast']['day']
		entry['date'] = results['query']['results']['channel'][i]['item']['forecast']['date']
		text = results['query']['results']['channel'][i]['item']['forecast']['text']
		try:
			weather_img = Weather.objects.get(type=text)
		except:
			print("not for : ",text)	
		entry['image'] = ""
		forecast.append(entry)

	#print(forecast)
	return render(request,'home/weather_forecast.html',{'forecast':forecast})


def getCity(lat,lon):
   url = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyBdWsMTk1r9z49-_Nh0XIq4kisJ2T49gsY&"
   url += "latlng=%s,%s&sensor=false" % (lat,lon)
   v = urlopen(url).read()
   v = json.loads(v.decode('utf-8'))
 
   for i in range(0,len(v["results"][0]['address_components'])):
       if "locality" in v["results"][0]['address_components'][i]['types'] :
           try:
               x = float(v["results"][0]['address_components'][i]["long_name"])
               return v["results"][0]['address_components'][i]["long_name"]
           except:
               break
   return v["results"][0]['address_components'][1]["long_name"]        


import numpy as np
import pickle
import sklearn
@csrf_exempt
def predict(request):
	
	lat = request.POST.get('lat')
	lon = request.POST.get('lon')
	city = getCity(lat,lon)
	print(city)
	result = pd.read_csv("/home/mayank/Desktop/SIH_ExtremeCoders/result.csv")
	select = result[result.lat==float(lat)]
	select = select[select.lon==float(lon)]
	select = select.drop_duplicates(subset='crop')
	x = list(select['crop'][:5])
	output = {}
	ans = " "
	ans = ans + "\n"
	ans = ans + str(city) + "    :    "
	ans = ans + "\n"
	output['city'] = city
	output['crops'] = x 

	for i in x:
		ans = ans + str(i) + " "
		ans = ans + "\n"
	filename = '/home/mayank/Desktop/SIH_ExtremeCoders/Saved_Models/scaler.pkl'
	filename1 = '/home/mayank/Desktop/SIH_ExtremeCoders/Saved_Models/kmeans.pkl'

	sc_X = pickle.load(open(filename, 'rb'))
	kmeans = pickle.load(open(filename1, 'rb'))
	X_check = np.array([14.75,    0.0012,    0.03,    76.41,    0.8    ,1010.06,    14.81,    0.89,    7    ,277.34,    80.5,    10,    12,    14,    2,    5,    45,    227445,10])
	X_scaled = sc_X.transform(X_check.reshape(1,-1))
	centroid=kmeans.predict(X_scaled)

	dis=kmeans.cluster_centers_[centroid]
	water = sc_X.inverse_transform(dis-X_scaled)
	water_req = water[0][18]/X_check[18]
	water_req = water_req*100
	ans = ans + str(water_req) + " percent Water "
	output['water'] = water_req*100
	print(output)
	return HttpResponse(ans)
