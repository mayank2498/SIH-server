from django.shortcuts import render,HttpResponse
from chatterbot import ChatBot
from home.models import Weather
import json
from urllib.request import urlopen
from chatterbot.trainers import ListTrainer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from translator import get_in_languages
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
	x = v['hourly']['data']
	for i in x:
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
	return render(request,'home/index.html')


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

	