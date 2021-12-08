import requests
import random

def start():
	oo = '1qaz2wsx3edc4rfv5tgb6yhn7ujm8k9ol0p'
	while True :
		user = str("". join(random.choice(oo) for i in range(4)))
		url = 'https://www.instagram.com/accounts/login/ajax/'
		h={
		'Host': 'www.instagram.com',
		'User-Agent': 'my-app/0.0.1',
		'Accept': '*/*',
		'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
		'Accept-Encoding': 'gzip, deflate, br',
		'X-CSRFToken': '5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect',
		'X-Instagram-AJAX': '1d6caaf37cd2',
		'X-IG-App-ID': '936619743392459',
		'X-ASBD-ID': '437806',
		'X-IG-WWW-Claim': '0',
		'Content-Type': 'application/x-www-form-urlencoded',
		'X-Requested-With': 'XMLHttpRequest',
		'Content-Length': '347',
		'Origin': 'https://www.instagram.com',
		'Connection': 'keep-alive',
		'Referer': 'https://www.instagram.com/accounts/login/',
		'Cookie': 'ig_did=7B796F1F-ADE7-429C-8ADB-9B131663E5E4; datr=2kDRYNWmjctteBSnOqogPrxv; csrftoken=5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect; mid=YNIa4QALAAGoeESFP8axY9NfC9t3; ig_nrcb=1',
		'TE': 'Trailers'}
		data = {
		'username': f'{user}',
		'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:password'
		}
		req = requests.post(url, headers=h, data=data)
		if '"user":true' in req.text:
			print (f"{user} ❌")
		elif '"message":"Please wait a few minutes before you try again."'in req.text:
			print("wait few minutes before try again ⚙️🛠️")
			exit()
		else :
			print (f"{user} ✅")
start()
