from boltiot import Bolt
api_key = "e9a57e96-679d-4ab3-988b-e7a95ad54702"
device_id  = "BOLT8022282"
mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
print (response)
