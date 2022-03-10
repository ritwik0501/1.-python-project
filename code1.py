#get details of mobile number 😉
import phonenumbers
from test import number
""""test is a file name where i store my phone number with 
country code in number variable 😊😊😊""" 

from phonenumbers import geocoder
ch_nmber=phonenumbers.parse(number, "CH") #here we store the country name
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier #carrier use for service provider name like jio ,vi
service_name=phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_name, "en"))
#i give my jio number but it does not show,i think they did not develop the option for jio😟