import requests
import json
import random
import time
import random
import threading
import sys
import random
import ssl
import datetime
Intn = random.randint

url = "https://lionkingdx.com/VENOM/files/vietnam2/rep.sh" 
payload = {
 "ver":2,"key":"fuck","secret":"fuck","hwid":"TWVtOiAxNzY2IE1CCltwZXJzaXN0LnN5cy50aW1lem9uZV06IFtBZnJpY2EvQ2Fpcm9dCltyby5ib290LnNlcmlhbG5vXTogW1JGOE0zMjY5REhQXQpbcm8uYm9vdGxvYWRlcl06IFtBMTA1RkREVTNCVEYxXQpbcm8uYnVpbGQuZmluZ2VycHJpbnRdOiBbc2Ftc3VuZy9hMTBkZC9hMTA6MTAvUVAxQS4xOTA3MTEuMDIwL0ExMDVGRERVM0JURjE6dXNlci9yZWxlYXNlLWtleXNdCltyby5wcm9kdWN0LmxvY2FsZV06IFtlbi1HQl0KW3JvLnNlcmlhbG5vXTogW1JGOE0zMjY5REhQXQo="
}



# Adding empty header as parameters are being sent in payload
headers = { 
  
 "Connection": "keep-alive",
   
#  "Host": "drmenv-auth.furygod.com",
   "user-agent": "PRDownloader",
#    "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,*/*;q\u003d0.8",
#    "accept-language": "en-GB,zh-Hans-CN;q\u003d0.7,ar-EG;q\u003d0.3",
#    "accept-encoding": "gzip, deflate, br",
#    "cookie": "cf_clearance=92dmY251_PpqS4MJ.aEOJXSr74fT3.CC1NQz1Zwecr4-1630945786-0-250",
#    "upgrade-insecure-requests": "1",
 #   "te": "trailers",
   

        
  #   "User-Agent":  'Go-http-client/' + str(Intn(0, 1000)) + '.' + str(Intn(0, 99999))  
 }



  

  
            
for _ in range(10000000000000000): 
 g = requests.get(url, headers=headers)
 

 print(g.content)
 print(g)
 