#!/usr/bin/env python

import datetime
import json
import boto3
import sys
from tradegecko import TradeGeckoRestClient

# Use s3 bucket to get access token for the API and prepare output documents
myBucket = 'fosdick-exports'
s3 = boto3.resource('s3')
s3c = boto3.client('s3')
object = s3.Object(myBucket,'.tg')
access_token = object.get()["Body"].read().decode("utf-8")

# Set up some simple variables for usage throughout
now = datetime.datetime.today()
today = now.strftime('%Y%m%d')
time = now.strftime('%H%M%S')
outdir = "/tmp"
outfilename = "packed_" + today + "_" + time + ".tsv"
outfile = outdir + "/" + outfilename

# Get all orders that have a packed_status of "unpacked"
tg = TradeGeckoRestClient(access_token.rstrip())
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
   trailerLine = "Trailer Record\t" + str(outfilename) + "\t" + str(today) + "\t" + str(time) + "\t" + str(totalOrders) + "\t" + "00001\n" 
   f.write(trailerLine)

htmlBody= "<body><p><center>Log file created at s3://" + myBucket + "/" + outfilename + "<p></body>"

def lambda_handler(event, context):
   try:
      s3c.upload_file(outfile, myBucket, outfilename)
   except:
      htmlBody = "<body><p><center>The file was not properly uploaded to fosdick.<p></body>"
      return htmlHeader + htmlBody + htmlFooter

   header = s3.Object(myBucket,'header.html')
   footer = s3.Object(myBucket,'footer.html')
   htmlHeader = header.get()["Body"].read().decode("utf-8")
   htmlFooter = footer.get()["Body"].read().decode("utf-8")
   return htmlHeader + htmlBody + htmlFooter
