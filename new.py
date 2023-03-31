import requests
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'100',
  'convert':'USD',
  'sort': 'volume_24h',
  'sort_dir': 'desc'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'YOUR_API',
}

try:
  response = requests.get(url, params=parameters, headers=headers)
  data = json.loads(response.text)
  # Get the top 10 trading coins based on volume
  top_coins = []
  for d in data['data']:
    if len(top_coins) == 10:
      break
    top_coins.append((d['symbol'], d['quote']['USD']['volume_24h']))
  # Print the top 10 coins
  for coin in top_coins:
    print(coin[0], coin[1])
except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.TooManyRedirects) as e:
  print(e)
