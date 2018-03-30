from django.shortcuts import render,HttpResponse
from chatterbot import ChatBot
# Create your views here.



	# from chatterbot import ChatBot

	# chatbot = ChatBot(
	#         'Agribot',
	#         trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
	#     )

	# # Train based on the english corpus
	# chatbot.train("chatterbot.corpus.english")
	# return HttpResponse('done training')




def test(request):
	print("test")
	chatbot = ChatBot(
    'Agribot',
    trainer='chatterbot.trainers.ListTrainer'
	)
	# Get a response to the input text 'How are you?'
	response = chatbot.get_response('How you doing?')

	return HttpResponse(response)
