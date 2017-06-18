import requests
import json
import serial
import time
from bs4 import BeautifulSoup
from multiprocessing import Pool

comport = serial.Serial('/dev/ttyACM1',9600)

sensor = []
led = ""
i = 0

def modif(tag,value):
    url = 'http://qrtalk-1155.appspot.com/storeavalue'
    payload = {'tag': tag, 'value': value,'fmt':'html'}
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
 
    r = requests.post(url, params=payload, headers=headers)

def getvalue():
    url = 'http://qrtalk-1155.appspot.com/getvalue'
    payload = {'tag': 'led', 'fmt':'html'}
    headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = requests.post(url, params=payload, headers=headers)
    return r.content

def getHTML():
    soup = BeautifulSoup(getvalue(),"html.parser")
    isLed = False
    for text in soup.find_all("td"):
        if isLed:
            led = text.text
        if text.text == 'led':
            isLed = True
        else:
            isLed = False
    return led
pool = Pool(processes=1)
while True:
    time.sleep(0.5)
    if i >= 10:
        print(sensor)
        modif("sensor",str(sensor))
        sensor = []
        i = 0
        led = getHTML()
    if led.replace('"', "") == "Apagar Luz":
        print("hmmmmm")
        comport.write('l'.encode())
    else:
        print("tatatatat")
        comport.write('d'.encode())
    tag = str(comport.readline())
    print(tag)
    if tag[0] == 's':
        sensor.append(int(tag[1:]))
    i = i +1
