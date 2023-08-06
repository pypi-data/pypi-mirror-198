import datetime
import cv2
import os
import pyttsx3 
import pywhatkit as kt
import playsound as ps
import requests
import qrcode
from pytube import YouTube
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup
from datetime import date,datetime
from playsound import playsound
from tkinter import *
from tkinter import colorchooser
from AppOpener import open

engine = pyttsx3.init() 

err='\n \U0000274C Something Went Wrong \U0000274C\n'

def functions():
	l=['translate()','ytmp4()','ytmp3()','cqrcode()','dqrcode()','restr()','relist()','retuple()','clist()','ctuple()','cdict()','cset()','pickcolor()','openapp()','search()','playsong()','restart_system()','shutdown_system()','datetoday()','timenow()','say()','openfile()','weathernow()','setvoice()','voicerate()']
	print(f'Available Functions : {l}')

def translate(content,language):
	translated = GoogleTranslator(source='auto', target=language.lower()).translate(content)
	return translated

def ytmp4(link):
	yt = YouTube(link)
	stream = yt.streams.get_highest_resolution()
	stream.download()
	print('\n\U0001F3AC Video Saved Successfully \U00002714\n')
	
def ytmp3(link):
	yt = YouTube(link)
	video = yt.streams.filter(only_audio=True).first()
	ofile = video.download(output_path=".")
	b, ext = os.path.splitext(ofile)
	file = b + '.mp3'
	os.rename(ofile, file)
	print('\n\U0001F3B6 Audio Saved Successfully \U00002714\n')
	
def cqrcode(data,filename):
	img = qrcode.make(data)
	img.save(filename)
	print('\nQrcode Saved Successfully \U00002714\n')
	
def dqrcode(filepath):
	image = cv2.imread(filepath)
	detector = cv2.QRCodeDetector()
	data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
	return data
	
def info():
	print('\nThis Pydule is Created by D.Tamil Mutharasan \U0001F608\n')

def restr(oldstr,index,newstr):
	if isinstance(oldstr,str):
		new=''
		for i in range(len(oldstr)):
			if i==index:
				new+=newstr
			else:
				new+=oldstr[i]
		return new
	else:
		print(err)	

def reSet(oldset,element,newelement):
	if isinstance(oldset,set):
		new=set()
		for i in oldset:
			if i==element:
				new.add(newelement)
			else:
				new.add(i)
		return new				
	else:
		print(err)	

def relist(oldlist,index,newlist):
	if isinstance(oldlist,list):
		new=[]
		for i in range(len(oldlist)):
			if i==index:
				new+=[newlist]
			else:
				new+=[oldlist[i]]
		return new
	else:
		print(err)	

def retuple(oldtup,index,newtup):
	if isinstance(oldtup,tuple):
		new=tuple()
		for i in range(len(oldtup)):
			if i==index:
				new+=(newtup,)
			else:
				new+=(oldtup[i],)
		return new
	else:
		print(err)	

def clist(mx):
	List=[]
	print('Enter Values One by One \U0001F447\n')
	for i in range(mx):
		l=eval(input(f'Enter {i+1} Value :'))
		List.append(l)
	print('\nList Created Successfully \U00002714\n')
	return List

def ctuple(mx):
	Tuple=()
	print('Enter Values One by One \U0001F447\n')
	for i in range(mx):
		t=eval(input(f'Enter {i+1} Value :'))
		Tuple+=(t,)
	print('\nTuple Created Successfully \U00002714\n')
	return Tuple

def cdict(mx):
	Dict={}
	for i in range(mx):
		key=eval(input(f'Enter the Key of No.{i+1} Element :'))
		value=eval(input(f'Enter the Value of No.{i+1} Element :'))
		Dict[key]=value
	print('\nDictionary Created Successfully \U00002714')	
	return Dict

def cset(mx):
	Set=set()
	print('Enter Values One by One \U0001F447\n')
	for i in range(mx):
		s=eval(input(f'Enter {i+1} Values : '))
		Set.add(s)
	print('\nSet Created Successfully \U00002714')	
	return Set

def pickcolor():
	root=Tk()
	root.geometry('250x100')
	root.title('Color Picker')
	def n():
		c=colorchooser.askcolor(title='CP')
		print(c)
	b=Button(root,text='Pick Color',command=n).pack()
	root.mainloop()				
	
def openapp(app_name):
	open(app_name)
	
def search(content):
	kt.search(content)	
	print('\nSearching \U0001F50E...\n')		
	
def playsong(song_path):
	playsound(song_path)
	
def restart_system():
	print('\nRestarting the System \U0001F4BB...\n')		
	os.system("shutdown /r /t 1")
	
def shutdown_system():
	print('\nShutting Down Your System \U0001F4BB...\n')
	return os.system("shutdown /s /t 1")
	
def datetoday():
	d=date.today()
	return d
	
def timenow():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S %p")
	return current_time
	
def say(content):	
	engine.say(content)
	engine.runAndWait()  
	
def openfile(path):
	os.startfile(path)
	print('OPENING...')

def weathernow(place):
	headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

	def weather(city,place):
	    city = city.replace(" ", "+")
	    res = requests.get(
	        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
	    soup = BeautifulSoup(res.text, 'html.parser')
	    location = soup.select('#wob_loc')[0].getText().strip()
	    time = soup.select('#wob_dts')[0].getText().strip()
	    info = soup.select('#wob_dc')[0].getText().strip()
	    weather = soup.select('#wob_tm')[0].getText().strip()
	    details=['City Name : '+place,location,info,weather+'°C']
	    return details
	city = place+" weather"
	return weather(city,place)

def setvoice(num):
	voices=engine.getProperty('voices')
	engine.setProperty('voice',voices[num].id)	

def voicerate(num):
		engine.setProperty('rate',num)