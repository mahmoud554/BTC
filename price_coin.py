import requests
import time
import os
#مكاتب

#trakos
os.system('pip install requests')
os.system('pip install pyTelegramBotAPI')
os.system('pip install telebot')
os.system('clear')
#المتغيرات

api_key = "f8c94451-c200-46ee-8f82-18bb7b8eb206"
bot_key ="1781705386:AAG4QHbBfy0gPBM4Dm46dyELU1poHSW4Ekk"
chat_id = "1689060322"
limit = 43000
time_interval = 60 * 60

#functhion

def get_price():
		url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
		parameters={
		"start" :"1",
		"limit": "10",
		"convert": "USD"
		}
		
		
		
		
		headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
  }

#انشاء طلب من موقع coin market cup

		response = requests.get(url,headers=headers,params=parameters).json()
		btc_price = response["data"] [0]["quote"]["USD"]["price"]
		
		return btc_price
		
def send_update(chat_id , msg):
		url = f"https://telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
		requests.get(url)
	
	
def main():
		while True:
			price=get_price
			if price<limit:
			send_update(chat_id ,f"price btc now:{price}")
			time.sleep(2)
main()		
	