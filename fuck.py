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

url = "https://iqarabian.net" 
payload = {
 "ver":2,"key":"fuck","secret":"fuck","hwid":"TWVtOiAxNzY2IE1CCltwZXJzaXN0LnN5cy50aW1lem9uZV06IFtBZnJpY2EvQ2Fpcm9dCltyby5ib290LnNlcmlhbG5vXTogW1JGOE0zMjY5REhQXQpbcm8uYm9vdGxvYWRlcl06IFtBMTA1RkREVTNCVEYxXQpbcm8uYnVpbGQuZmluZ2VycHJpbnRdOiBbc2Ftc3VuZy9hMTBkZC9hMTA6MTAvUVAxQS4xOTA3MTEuMDIwL0ExMDVGRERVM0JURjE6dXNlci9yZWxlYXNlLWtleXNdCltyby5wcm9kdWN0LmxvY2FsZV06IFtlbi1HQl0KW3JvLnNlcmlhbG5vXTogW1JGOE0zMjY5REhQXQo="
}



# Adding empty header as parameters are being sent in payload
headers = { 
  
 "Connection": "keep-alive",
   
#  "Host": "drmenv-auth.furygod.com",
# "user-agent": "Mozilla/5.0 (Android 10; Mobile; rv:85.0) Gecko/85.0 Firefox/85.0",
  "Host": "iqarabian.net",
    "user-agent": "Mozilla/5.0 (Android 10; Mobile; rv:85.0) Gecko/85.0 Firefox/85.0",
    "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,*/*;q\u003d0.8",
    "accept-language": "en-GB,zh-Hans-CN;q\u003d0.7,ar-EG;q\u003d0.3",
  #  "accept-encoding": "gzip, deflate, br",
    #"cookie": "vDDoS\u003d242eadb001abb5783c03292e3e52ac85",
    "upgrade-insecure-requests": "1",
    "te": "trailers",
  "cookie": "__tawkuuid=e::iqarabian.net::iCVaLriZPGfxwL0IqxCru54PHjXL1CtViBa2q68qOlN70HXHbrPgqT1x/2Lm1r5l::2;__ddg1=lahFhA4gXdgXPha62h5I;__ddgid=ronDgV4SHtolEx95;__ddg2=Rc65jLGHP2NcZVxv;XSRF-TOKEN=eyJpdiI6Ilg4Y3NoVWlqQ0NkNXhLbVlXZkdWUFE9PSIsInZhbHVlIjoiSmozOG9mbE1nOVRJZGg1WDl3c1VVMEpmVzRwY2dhK3dISm1sRDk5RjFGTU43R1REbnpGSUFwTzdNN1MrbFZkWjNjQThpNHlPNU9Tek5QVjgxWjc0N2tzd1plT0l6YzFtbkg0WWpkcXdBbzd5U3ROOTA5b0c1UmtaMUROTlkzVDUiLCJtYWMiOiJhOTI2MTEyMDNiMDU1MjFiNDQ5YjNiMjM2YWNiMjM5MjkzMjZjODZlYWJmYjI3MTQ2NzYxN2NkNGJkYTdjZDgwIn0%3D;laravel_session=eyJpdiI6Im92K1hTa2pBZDRaYXloUzVkTDZRM0E9PSIsInZhbHVlIjoiR3dQQmxqc0lpVmdhbVdlM1U2cGVCVHVrSldzeWhzaDMyOGgzSXQwc2NjUjJIN0VhSDVJR2pXZHByYTFXem9vSkZ0RUJJMXVHR21RU1EvbXc4ZkpiZHoxaHdtQUhPYjNrNjRjN0VwUURoWWs0UWxaUzFiR0RNNlFMYmthNXhOcm0iLCJtYWMiOiJhZDdlMDFjZjhmY2U0MjUxOGY4NWEzMGQ0NTI0MDFiMDZlOTNjNTdkMTU2NTI5MWZkNTkwOTljYzQxYzlmYjk1In0%3D;vDDoS=242eadb001abb5783c03292e3e52ac85",
#    "upgrade-insecure-requests": "1",
 #   "te": "trailers",
   

        
  #   "User-Agent":  'Go-http-client/' + str(Intn(0, 1000)) + '.' + str(Intn(0, 99999))  
 }



  

  
            
for _ in range(1): 
 g = requests.get(url, headers=headers)
 

 print(g.content)
 print(g)
 