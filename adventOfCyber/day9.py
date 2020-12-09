import requests

print('Hello World');

url = 'http://10.10.169.100:3000'

req = requests.get(url)
result = req.json()['value']

while True:
	next = req.json()['next']
	print('[+] next url: ' + url + '/' + next)
	print('----> ' + req.text)
	req = requests.get(url + '/' + next)
	next = req.json()['next']

	if(next == 'end'):
		break;
	else:
		result += req.json()['value']


print('------------------------------------------')
print('result: ' + result)
print(req.json())
