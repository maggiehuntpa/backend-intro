import requests

url = "https://currency-converter5.p.rapidapi.com/currency/convert"

currency_1 = "GBP" #feel free to change these
currency_2 = "USD"

user_input = input(f'How many {currency_1} would you like to convert to {currency_2}?') #this will ask you what number you would like to convert and take it as input

print(f'You would like to convert {user_input} {currency_1} to {currency_2}')

querystring = {"format":"json","from":currency_1,"to":currency_2,"amount": user_input,"language":"en"}

headers = {
	"x-rapidapi-key": "INSERT API KEY HERE", #insert your key as a string here but  DO NOT COMMIT IT TO GITHUB
	"x-rapidapi-host": "currency-converter5.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())