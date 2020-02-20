import numpy as np
cipher=""
a="abcdefghijklmnopqrstuvwxyz0123456789"
a=list(a)
print(a)
choice=int(raw_input("enter 1 for encryption and 2 for decryption"))
if(choice==1):
	def save_data():
		f1=open("cipher.txt","w+")
		f1.write(cipher)
	key=raw_input("enter key")
	keylist=[]
	k=0
	size1=len(key)
	key=key.lower()
	while(k<size1):
		if(key[k] not in a):
			key=key.replace(key[k],"")
			size1=len(key)
		else:
			k=k+1
			continue
	print(key)
	def indexof(data):
		for i in range(0,6):
			for j in range(0,6):
				if(data==keylist[i][j]):
					     return i,j
	for i in range(0,len(key)):
		if key[i] not in keylist:
			keylist.append(key[i])
	for i in a:
		if i not in keylist:
			keylist.append(i)
	print(keylist)
	keylist=np.array(keylist)
	keylist=keylist.reshape(-1,6)
	print(keylist)
	plaintext=open("plaintext.txt").read()
	size=len(plaintext)
	k=0
	size1=len(plaintext)
	plaintext=plaintext.lower()
	
	print("ptext",plaintext)
	while(k<size1):
		if(plaintext[k] not in a):
			plaintext=plaintext.replace(plaintext[k],"")
			size1=len(plaintext)
		else:
			k=k+1
			continue
	print(plaintext)
	def same_row_col_diff(r1,r2,c1,c2):
		global cipher
		if(r1==r2):
			c1=(c1+1)%6
			c2=(c2+1)%6
			cipher=cipher+keylist[r1][c1]+keylist[r1][c2]
		elif(c1==c2):
			r1=(r1+1)%6
			r2=(r2+1)%6
			cipher=cipher+keylist[r1][c1]+keylist[r2][c1]			
		else:
			cipher=cipher+keylist[r1][c2]+keylist[r2][c1]			

	i=0
	size=len(plaintext)
	while(i<size):
			i1=a.index(plaintext[i])
				
			try:
				i2=a.index(plaintext[i+1])
				if(i1==i2):
					plaintext=plaintext[0:i+1]+"x"+plaintext[i+1:]
					size=len(plaintext)
				else:
					plaintext=plaintext[0:i+1]+plaintext[i+1:]
				i=i+2
				continue

			except:
				plaintext=plaintext[0:i+1]+"z"
	print(plaintext)
	for i in range(0,len(plaintext),2):
		r1,c1=indexof(plaintext[i])
		r2,c2=indexof(plaintext[i+1])
		print(r1,r2,c1,c2)
		same_row_col_diff(r1,r2,c1,c2)	
	
	print(cipher)
	save_data()
elif(choice==2):
	p_decryption_text=""
		
	key=raw_input("enter key")
	keylist=[]
	k=0
	size1=len(key)
	key=key.lower()
	while(k<size1):
		if(key[k] not in a):
			key=key.replace(key[k],"")
			size1=len(key)
		else:
			k=k+1
			continue
	print(key)
	for i in range(0,len(key)):
		if key[i] not in keylist:
			keylist.append(key[i])
	for i in a:
		if i not in keylist:
			keylist.append(i)
	keylist=np.array(keylist)
	keylist=keylist.reshape(-1,6)
	f1=open("cipher.txt").read()
	def indexof(data):
		for i in range(0,6):
			for j in range(0,6):
				if(data==keylist[i][j]):
					     return i,j
	def same_row_col_diff_decryption(r1,r2,c1,c2):
		global cipher,p_decryption_text
		if(r1==r2):
			c1=(c1-1)%6
			c2=(c2-1)%6
			p_decryption_text=p_decryption_text+keylist[r1][c1]+keylist[r1][c2]
		elif(c1==c2):
			r1=(r1-1)%6
			r2=(r2-1)%6
			p_decryption_text=p_decryption_text+keylist[r1][c1]+keylist[r2][c1]			
		else:
			p_decryption_text=p_decryption_text+keylist[r1][c2]+keylist[r2][c1]
	for i in range(0,len(f1),2):
		r1,c1=indexof(f1[i])
		r2,c2=indexof(f1[i+1])
		same_row_col_diff_decryption(r1,r2,c1,c2)
	
	p_decryption_text=p_decryption_text.replace("x","")
	p_decryption_text=p_decryption_text.replace("z","")
	print(p_decryption_text)
		
else:
	print("wrong choice")

