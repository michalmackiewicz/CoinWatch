#!/usr/bin/python3

import urllib.request
import json
import sqlite3
from datetime import date, datetime

def add_to_base(crypto, value, created=datetime.now()):
  db = sqlite3.connect('rates.db')
  # Get a cursor object
  cursor = db.cursor()
  # Check if table does not exist and create it
  cursor.execute("CREATE TABLE IF NOT EXISTS "+crypto+" (id INTEGER PRIMARY KEY, created timestamp, value REAL)")

  cursor.execute("INSERT INTO "+crypto+"(created, value) VALUES(?,?)", (created, value))

  db.commit()

  db.close()


def get_value(crypto, fiat):

  url = "https://bitbay.net/API/Public/"+crypto+fiat+"/ticker.json"

  response = urllib.request.urlopen(url)
  data = response.read()
  result = data.decode('utf-8')
  result_dict = json.loads(result)
  return result_dict['average']

def main():

  print("Average values from bitbay")
  current_time = datetime.now()
  cryptos = ["BTC","ETH","LSK","LTC","GAME","DASH","BCC"]

  for crypto in cryptos:
    val = get_value(crypto,"PLN")
    print(crypto+" "+str(val))
    add_to_base(crypto, val, current_time)

if __name__ == '__main__':
  main()
