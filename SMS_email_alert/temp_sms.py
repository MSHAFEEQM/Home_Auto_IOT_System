
import conf, json, time
from boltiot import Sms, Bolt
minimum_limit = 300 
maximum_limit = 370
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)

while True: 
    print ("Reading sensor value")
    response = mybolt.analogRead('A0') 
    data = json.loads(response)
    sensor = int(data['value'])
    Temperature=(100*sensor)/1024 
    print("Sensor value is: {:0.2f} ºC ".format(Temperature))
    try: 
        sensor_value = int(data['value'])
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("The Current temperature sensor value is {:0.2f} ºC ".format(Temperature))
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)

