#!/usr/bin/python3

import urllib.request
import json

def get_value(crypto, fiat):

  url = "https://bitbay.net/API/Public/"+crypto+fiat+"/ticker.json"

  response = urllib.request.urlopen(url)
  data = response.read()
  result = data.decode('utf-8')
  result_dict = json.loads(result)
  return result_dict['average']

def main():

  print("Average values from bitbay")
  print(get_value("BTC","PLN"))
  print(get_value("ETH","PLN"))
  print(get_value("LSK","PLN"))
  print(get_value("LTC","PLN"))
  print(get_value("GAME","PLN"))
  print(get_value("DASH","PLN"))
  print(get_value("BCC","PLN"))


if __name__ == '__main__':
  main()

