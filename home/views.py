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
	
	#train_from_text(chatbot,'/home/mayank/Desktop/crops/coffee.txt')
	response = chatbot.get_response('tell me something about coffee')

	return HttpResponse(response)




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
	lat = 12
	lon = 80
	for i in range(0,20):
		#getWeather(lat,lon)
		lon = lon+0.25



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

	