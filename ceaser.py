import sys
print("1)encrypt data\n2)decrypt data\n3)decrypt data by other methods\n")
a=int(input("enter choice\n"))
def save_enc_data(data):
	f2=open("out.txt","w")
	f2.write(data)
	print("data saved successfully to out.txt file\n")
def encryption():
	encryptedtext=""
	text=raw_input("enter file name for encrypt\n")
	try:
		f1=open(text.strip()).read()
		
	except:
		print("WRONG FILE NAME OR EXTENSION")
		sys.exit(0)
	key=int(input("enter key\n"))
	print("your plain text is:"+f1+"\n")
	for i in range(0,(len(f1)-1)):
		encryptedtext+=chr(((ord(f1[i]))+key)%255)
	print(encryptedtext+"\n")
	save_enc_data(encryptedtext)
def normal_decryption():
	decryptedtext=""
	text=raw_input("enter file name for decrypt\n")
	try:
		f1=open(text.strip()).read()
		
	except:
		print("WRONG FILE NAME OR EXTENSION")
		sys.exit(0)
	key=int(input("enter key\n"))
	for i in range(0,(len(f1))):
		decryptedtext+=chr(((ord(f1[i]))-key)%255)
	print(decryptedtext+"\n")
def decryption(key,text):
	decryptedtext=""
	try:
		f1=open(text.strip()).read()
		
	except:
		print("WRONG FILE NAME OR EXTENSION")
		sys.exit(0)
	for i in range(0,(len(f1))):
		decryptedtext+=chr(((ord(f1[i]))-key)%255)
	print(decryptedtext+"\n")
	return decryptedtext
def savedata(data):
	filename=raw_input("enter file for save data")
	f1=open(filename.strip(),"w")
	f1.write(data)
def wordfinding(data):
	counter=0
	l1=['a', 'about', 'after', 'all', 'also', 'an', 'and', 'any', 'as', 'at', 'back', 'be', 'because', 'but', 'by', 'can', 'come', 'could', 'day', 'do', 'even', 'first', 'for', 'from', 'get', 'give', 'go', 'good', 'have', 'he', 'her', 'him', 'his', 'how', 'I', 'if', 'in', 'into', 'it', 'its', 'just', 'know', 'like', 'look', 'make', 'me', 'most', 'my', 'new', 'no', 'not', 'now', 'of', 'on', 'one', 'only', 'or', 'other', 'our', 'out', 'over', 'people', 'say', 'see', 'she', 'so', 'some', 'take', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'think', 'this', 'time', 'to', 'two', 'up', 'us', 'use', 'want', 'way', 'we', 'well', 'what', 'when', 'which', 'who', 'will', 'with', 'work', 'would', 'year', 'you', 'your']
	for i in l1:
		if((i.upper() in data)or(i.lower() in data)):
			counter+=1
	if(counter>=10):
		print("data found successfully\n")
		print(data+"\n")
		savedata(data)
		return 1
	return 0
	
def mostfrequentword(filename):
	try:
		f1=open(filename.strip()).read()
	except:
		print("wrong input file\n")
		sys.exit(0)
	return max(set(f1),key=f1.count)
if(a==1):
	encryption()
elif(a==2):
	normal_decryption()
elif(a==3):
	text=raw_input("enter file name for decrypt\n")
	typeofattack=int(input("1)Interactive mode\n2)automatic mode\n3)frequency attack\n"))
	if(typeofattack==1):
		for key in range(0,256):
			dtext=decryption(key,text)
			response=int(input("IS IT IN READABLE FORM\n1)yes\t2)no\n"))
			if(response==1):
				savedata(dtext)
				break
			elif(response==2):
				continue
			else:
				print("you enteresd wrong data it will be continue\n")
				continue
	elif(typeofattack==2):
		for key in range(0,256):
			dtext=decryption(key,text)
			result=wordfinding(dtext)
			if(result==1):
				break
				
	elif(typeofattack==3):
		print("it only works for data which is in alphabetic not for special symbol or others(if key is under 26 and plain text is in alphabetic and cipher in alphabetic)\n")
		alphabeticdata=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		frequencydata=['e','t','a','o','i','n','s','r','h','d','l','u','c','m','f','y','w','g','p','b','v','k','x','q','j','z']
		frequentocuurencedata=mostfrequentword(text)
		print("frequent character",frequentocuurencedata)
		lo=frequentocuurencedata.lower()
		for i in frequencydata:
			try:
				index1=alphabeticdata.index(frequentocuurencedata.lower())
			except:
				print("cipher contain special symbol or digits this attack will not work")
				sys.exit(0)	
			index2=alphabeticdata.index(i)
			key=index1-index2
			data=decryption(key,text)			
			response=int(input("is it readable form?\n1)yes\n2)no\n"))
			if(response==1):
				savedata(data)
				break
			
	else:
		print("wrong choice")
		sys.exit(0)
else:
		print("wrong choice")
		sys.exit(0)
