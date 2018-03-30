from googletrans import Translator

import urllib
from urllib.request import urlopen



def get_in_languages(text):
	translator = Translator()
	hindi = translator.translate(text,dest="hi")
	telgu = translator.translate(text,dest="te")
	tamil = translator.translate(text,dest="ta")
	languages = {}
	languages['hindi'] = hindi.text
	languages['telgu'] = telgu.text
	languages['tamil'] = tamil.text
	print(languages)
	return languages
