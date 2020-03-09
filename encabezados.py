import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/post'
	payload = {'nombre':'sergio','curso':'python','nivel':'intermedio'}
	headers = {'Conten-Type':'application/json', 'access-token':'123'}

	response = requests.post(url, data=json.dumps(payload), headers= headers)
	print(response.url)

	if response.status_code == 200:
		#print(response.content)
		headers_response = response.headers #dic
		server = headers_response['Server']
		print(server)
