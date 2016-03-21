#!/usr/bin/env python

import os
import datetime
import json
from pprint import pprint
from tradegecko import TradeGeckoRestClient

now = datetime.datetime.today()
today = now.strftime('%Y%m%d')
time = now.strftime('%H%M%S')
outfile = "packed_" + today + ".tsv"
tg = TradeGeckoRestClient(os.environ.get("TRADEGECKO_ACCESS_TOKEN", None))

# We don't need json.loads or json.dumps because we want this as a python list to be able to use it
# Get all orders that have a packed_status of "unpacked"
orders = tg.order.filter(packed_status="unpacked")
totalOrders = orders['meta']['total']

with open(outfile, 'w') as f:
   for order in xrange(totalOrders):
      billingAddressID = str(orders['orders'][order]['billing_address_id'])
      shippingAddressID = str(orders['orders'][order]['shipping_address_id'])

      bill = tg.address.get(billingAddressID)
      ship = tg.address.get(shippingAddressID)
      created = str(orders['orders'][order]['created_at'])
      transactionTime = created[11:13] + created[14:16] + created[17:19]
      transactionDate = created[5:7] + created[8:10] + created[0:4]

      orderLine = str(orders['orders'][order]['id']) + "\t" + \
                  str(bill['address']['first_name']) + "\t" + \
                  str(bill['address']['last_name']) + "\t" + \
                  str(bill['address']['address1']) + "\t" + \
                  str(bill['address']['address2']) + "\t" + \
                  "\t" + "\t" + \
                  str(bill['address']['city']) + "\t" + \
                  str(bill['address']['state']) + "\t" + \
                  str(bill['address']['zip_code']) + "\t" + \
                  str(bill['address']['country']) + "\t" + \
                  "\t" + "\t" + \
                  "Q" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "WEB" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  transactionTime + "\t" + \
                  transactionDate + "\t" + \
                  "\t" + "\t" + \
                  str(ship['address']['first_name']) + "\t" + \
                  str(ship['address']['last_name']) + "\t" + \
                  str(ship['address']['address1']) + "\t" + \
                  str(ship['address']['address2']) + "\t" + \
                  "\t" + "\t" + \
                  str(ship['address']['city']) + "\t" + \
                  str(ship['address']['state']) + "\t" + \
                  str(ship['address']['zip_code']) + "\t" + \
                  str(ship['address']['country']) + "\t" + \
                  "1" + "\t" + \
                  "\t" + "\t" + \
                  "0.00" + "\t" + \
                  "0.00" + "\t" + \
                  "0.00" + "\t" + \
                  "-0.00" + "\t" + \
                  "0.00" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t" + \
                  "\t" + "\t\n"
      f.write(orderLine)
   trailerLine = "Trailer Record\t" + str(outfile) + "\t" + str(today) + "\t" + str(time) + "\t" + str(totalOrders) + "\t" + "00001\n" 
   f.write(trailerLine)

# Update packed_status of orders to packed when we send .tsv to fosdick
