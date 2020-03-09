import requests

if __name__ == '__main__':
	#url = 'http://pokeapi.co/api/v2/pokemon-form/'
	url = 'http://localhost:8080/dikrom_system/Escuela'
	response = requests.get(url)
	if response.status_code == 200:

		pleyload = response.json()
		results = pleyload.get('results',[])

		if results:
			for pokemon in results:
				name = pokemon['name']
				print(name)
