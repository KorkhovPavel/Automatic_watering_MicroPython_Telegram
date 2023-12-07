from machine import Pin, ADC
from time import sleep
from machine import deepsleep
from urequests import get
from config import *


def send_message(message_text):
    """
    send message telegram
    message_text - text message
    """
    url = "https://api.telegram.org/bot"+TOKEN+"/sendMessage?chat_id="+chat_id+'&text='+message_text
    response = get(url)
    response.close()

def moisture_sensor_check(max_val):
    """
    checking soil moisture
    max_val - max value soil moisture(it is different for each plant) 
    """
    moisture_sensor = ADC(Pin(soil_moisture_sensor))
    moisture_sensor.width(ADC.WIDTH_10BIT)
    moisture_sensor.atten(ADC.ATTN_11DB)
    res = ""
    sleep(0.1)
    if moisture_sensor.read()>max_val:
        sleep(0.1)
        res = '+ '+str(moisture_sensor.read())
    else:
        sleep(0.1)
        res =  '- ' + str(moisture_sensor.read())
    return res

    
def relay_on_sec(sec_on):
    """
    Turn on the relay and pump for a certain number of seconds.
    Attention! This setting is individual and is selected for each case separately.
    sec_on - number of seconds of relay and pump operation
    """
    relay = Pin(relay_pin, Pin.OUT)
    sleep(1)
    relay.value(0)
    sleep(sec_on)
    relay.value(1)
    sleep(1)
    
    

def main():
    msg = ''
    if '+' in moisture_sensor_check(1000):
        msg = 'start:'+ moisture_sensor_check(1000)[2:]
        relay_on_sec(3)
        msg = msg + ' | '+ 'finish:'+moisture_sensor_check(1000)[2:]
        send_message(msg) 


print('start')
main()

print('finish')
sleep(5)

print('deep_sleep')
deepsleep(1000*deepsleep_sec)

