# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import json
import random
import requests

a = open('auth.json')
auth = json.load(a)


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = auth['TWILIO_ACCOUNT_SID']
auth_token = auth['TWILIO_AUTH_TOKEN']
airtable_key = auth['AIRTABLE_KEY']
airtable_base = auth['AIRTABLE_BASE']
client = Client(account_sid, auth_token)


airtable_get = "https://api.airtable.com/v0/{}/{}?api_key={}".format(airtable_base, "Numbers", airtable_key)
resp = requests.get(airtable_get)
numbers = json.loads(resp.content.decode("utf-8"))
num_set = set()

dry_run = True

if (dry_run):
	num_set = set()
	num_set.add('+14086668054')
else:
	for row in numbers['records']:
		num_set.add(row['fields']['Number'])




airtable_get = "https://api.airtable.com/v0/{}/{}?api_key={}".format(airtable_base, "Texts", airtable_key)
resp = requests.get(airtable_get)
texts = json.loads(resp.content.decode("utf-8"))
r_texts = random.randrange(0, len(texts['records']))

term =  texts['records'][r_texts]['fields']['Term']
definition = texts['records'][r_texts]['fields']['Definition']
sentence = texts['records'][r_texts]['fields']['Sentence']

msg_body = "Hello from Boomer University! \n\n"\
"The word of the day is {}, which means: \n\n"\
"{} \n\n"\
"{}".format(term.upper(), definition.capitalize(),sentence)


for n in num_set:
	print(n)
	message = client.messages \
                    .create(
                         body=msg_body,
                         from_='+12168687855',
                         to=n
                    )

