import phonenumbers
#from text import number
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
number = input("Enter the phone number: \n")
number = "+91" + number
ch_number = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))
service_provider = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_provider,"en"))