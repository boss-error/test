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

url = "https://lionkingdx.com/VENO/xapi/l.php" 

    #custom post data 
payload = {
 "request_body": "w=MTYzMDk1NjEwMjE5MA&x=VlRBd2RGRlVSWGRPVlZsTlZGVTFUV3BCZWs5VWF6Vk9la0YzVFVF&y=ZnVjaw&z=ZnVjaw"
}



# Adding empty header as parameters are being sent in payload
headers = { 
  
 "Connection": "keep-alive",

   "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; SM-A105F Build/QP1A.190711.020)"

  }



  

  
            
i =0
for i in range(1): 
 g = requests.post( url, data=(payload), headers=headers)
 print(i)
 print(g)
 print(g.content)
 