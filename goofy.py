sounds=["gnome","whatsapp","slip","boom","if you want more sounds, go to the website, open devtools, click on network tab, click on the sound and you should see the name of the sound (for example, boom.wav)"]
user_sounds=[]
print("sounds:",sounds)
while True:
    sound=str(input("sound (and pitch):\nexample: gnome -1\nfor positive pitch, gnome 1\n\nor maybe you want the same sound repeated, do this:\nexample: gnome =1337\n----"))
    if sound == "":
    	break
    user_sounds.append(sound)

file = open("out","w+")

for sound in user_sounds:
	sound_ = sound.split()[0]
	pitch_ = sound.split()[1]
	print("Sound:"+sound_)
	print("Pitch: "+pitch_)
	if pitch_.startswith("="):
		file.write(sound_+pitch_+"|") #pitch is times
	else:
		file.write(sound_+"@"+pitch_+"|") 

file.close() #after the for loop, close the file

