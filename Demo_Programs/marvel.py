#https://developer.marvel.com/account

import requests
import hashlib
import json
from tkinter import *

#def getKeys():
	#keys = open("key.txt", "r")
	#publicKey = keys.readline().strip()
	#privateKey = keys.readline().strip()
	#keys.close()
	#key = [privateKey, publicKey]
	#return key

publicKey = '4bedff009bc72c6cb7f8341184d44917'
privateKey = "ceb64c2671d4e35f3cdf1d601a84c9a7bc219a88"
key = [privateKey, publicKey]

def getHash(publicKey, privateKey):
	key = "1" + privateKey + publicKey
	result = hashlib.md5(key.encode())
	return result.hexdigest()


publicKey = key[1]
result = getHash(key[1], key[0])

url = "https://gateway.marvel.com:443/v1/public/characters?nameStartsWith=T&orderBy=name&ts=1&apikey="+publicKey+"&hash="+result
response = requests.get(url)
data = json.loads(response.text)

page = Tk()
page.title("Marvel API Characters")
page.geometry("800x1000")

fr = Frame(page, width = 800, height = 1000)
fr.pack()

e = Entry(fr)
e.pack()






def find():
        for character in data['data']['results']:
                if e.get() == character['name']:
                        text.config(text = character['name'] + character['description'])

b = Button(fr,text='enter',command=find)
b.pack()

text= Label(fr, text=" ")
text.pack()
                        
        





"""
url = "https://gateway.marvel.com:443/v1/public/characters?name=hulk&ts=1&apikey="+publicKey+"&hash="+result
response = requests.get(url)
#print (response.text)

data = json.loads(response.text)
hulk_name = data['data']['results'][0]['name']
hulk_des = data['data']['results'][0]['description']
print (hulk_name + " | " + hulk_des)"""











for character in data['data']['results']:
	print (character['name'])
	print (character['thumbnail'])
	


