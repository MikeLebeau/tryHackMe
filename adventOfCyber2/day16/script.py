import requests

for i in range(0, 100, 2):
	res = requests.get('http://10.10.245.102:8000/api/' + str(i))
	print("Id: " + str(res.json()['item_id']))
	print("Response: " + str(res.json()['q']))
	#if (res.json().q != "Error. Key not valid!"):
		#print("Le code: " + i)
