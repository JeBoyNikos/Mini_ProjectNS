import requests
import xmltodict

auth_details = ('jop.corver@student.hu.nl', 'HaL5ccH-NfuwV2-zEXmv8dztt11YKPf9mp-Z8x7r2v1EowBsSXIuMg')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'

response = requests.get(api_url, auth=auth_details)

with open('vetrektijden.xml', 'w') as myXMLFile:
    myXMLFile.write(response.text)

myXMLFile = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen:')
for vertrek in myXMLFile['ActueleVertrekTijden']['VertrekkendeTrein']:
 eindbestemming = vertrek['EindBestemming']
 vertrektijd = vertrek['VertrekTijd'] # 2016-09-27T18:36:00+0200
 vertrektijd = vertrektijd[11:16] # 18:36
 print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)
