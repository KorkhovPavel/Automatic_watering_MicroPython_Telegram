from config import wifi_name, wifi_password
import time


time.sleep(7)
# base function connect wifi https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html

def do_connect(ssid, pwd):
    """
    connection to wifi
    """
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, pwd)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    return True

# wifi connection required
while do_connect(wifi_name, wifi_password) is not True:
    do_connect(wifi_name, wifi_password)
