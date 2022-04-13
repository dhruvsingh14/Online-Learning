#################
# simple apis 2 #
#################

##################
# speech to text #
##################

from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = "https://stream.watsonplatform.net/speech-to-text/api"

# loading in api key for speech to text
iam_apikey_s2t = "rPefdvQT6151MxnEkVRUSiVlBUlD8BilOXx-OVegsm0H"

# utilizing authenticator service to convert speech to text
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
print(s2t)

# downloading audio file
#wget -O PolynomialRegressionandPipelines.mp3  https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3

# since again wget is acting funny, i will do without, and download manually
# import wget
# url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3'
# wget.download(url, 'C:/Users/drewn/Desktop/python_for_data_science-master/wk4/simple_apis/NewFileName.mp3')

filename='PolynomialRegressionandPipelines.mp3'

# reads audio file in binary mode

# commenting out the following code block b/c it takes a while to run
# and doesn't determine the block following it

#with open(filename, mode="rb") as wav:
#    response = s2t.recognize(audio=wav, content_type='audio/mp3')
#response.result

# extracting file in the form of a dictionary
from pandas.io.json import json_normalize
# json_normalize(response.result['results'], "alternatives")
# response

# converting recognized text to data dictionary, extracting element
# recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
# printing type
# type(recognized_text)

#######################
# language translator #
#######################
from ibm_watson import LanguageTranslatorV3

url_lt = 'https://gateway.watsonplatform.net/language-translator/api'
apikey_lt='KIHdhuqRVPHbmMeBsAi0CIvoQooOY_AGQYXGxbYE6Kaq'
version_lt='2018-05-01'

# getting language translator functionality set up
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
print(language_translator)

# getting languages that can be translated to
from pandas.io.json import json_normalize
json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")


















# in order to display plot within window
# plt.show()
