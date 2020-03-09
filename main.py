import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/get'
	args = {'nombre':'Sergio','Curso':'Python'}
	response = requests.get(url, params=args)
	print(response.url)
	if response.status_code == 200:
		"""
		content = response.content
		response_json = response.json() #Dic
		origin = response_json['origin']
		print(content)
		print(origin)
		"""
		response_json = json.loads(response.text)
		origin = response_json['origin']
		print(origin)

