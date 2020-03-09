import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/post'
	playload = {'nombre':'Sergio','Curso':'Python','nivel':'intermedio'}

	response =  requests.post(url, data=json.dumps(playload))

	#json post se encarga de serializarlos
	#data entonces nosotros debemos de serializarlos
	print(response.url)

	if response.status_code == 200:
		print(response.content)
