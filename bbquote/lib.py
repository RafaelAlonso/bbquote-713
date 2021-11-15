import requests

def get_quote():
  url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
  response = requests.get(url).json()
  
  # "Because I say so. - Walter White"
  # return response[0]['quote'] + ' - ' + response[0]['author']
  return f"\"{response[0]['quote']} - {response[0]['author']}\""