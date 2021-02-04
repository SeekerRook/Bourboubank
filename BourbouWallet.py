from tkinter import *
import dropbox
import os

dropbox_access_token= "8ir-9dbTA8oAAAAAAAAAAcLaEySyI34UiJqFhPLCYR4xUGry83woZWxS8f5N5uV5"    
dropbox_path= "/Application/"
computer_path=""
client = dropbox.Dropbox(dropbox_access_token)


client.files_download_to_file(computer_path+"chrispassword.txt", dropbox_path+"chrispassword.txt")
chrispassword = open("chrispassword.txt","r")
chriskey = chrispassword.read()
chrispassword.close()
client.files_upload(open(computer_path+"chrispassword.txt", "rb").read(), dropbox_path+"chrispassword.txt",mode=dropbox.files.WriteMode.overwrite)
os.remove("chrispassword.txt")
client.files_download_to_file(computer_path+"evanpassword.txt", dropbox_path+"evanpassword.txt")
evanpassword = open("evanpassword.txt","r")
evankey = evanpassword.read()
evanpassword.close()
client.files_upload(open(computer_path+"evanpassword.txt", "rb").read(), dropbox_path+"evanpassword.txt",mode=dropbox.files.WriteMode.overwrite)
os.remove("evanpassword.txt")

valid = False
while (valid == False):
    username = input("Give Password : ")
    if username == evankey:
        my = "evan"
        other ="chris"
        valid = True
    elif username == chriskey:
        my = "chris"
        other = "evan"
        valid = True
    else: 
        print ("Wrong")
 



mysumpath = my+"sum.txt"
mychorespath = my+"log.txt"
otherlogpath = other+"log.txt"
othersumpath = other+"sum.txt"

def Download():
   client.files_download_to_file(computer_path+mysumpath, dropbox_path+mysumpath)
   client.files_download_to_file(computer_path+mychorespath, dropbox_path+mychorespath)
   client.files_download_to_file(computer_path+otherlogpath, dropbox_path+otherlogpath)
   client.files_download_to_file(computer_path+othersumpath, dropbox_path+othersumpath)





def Upload():
    client.files_upload(open(computer_path+mysumpath, "rb").read(), dropbox_path+mysumpath,mode=dropbox.files.WriteMode.overwrite)
    client.files_upload(open(computer_path+mychorespath, "rb").read(), dropbox_path+mychorespath,mode=dropbox.files.WriteMode.overwrite)
    client.files_upload(open(computer_path+otherlogpath, "rb").read(), dropbox_path+otherlogpath,mode=dropbox.files.WriteMode.overwrite)
    client.files_upload(open(computer_path+othersumpath, "rb").read(), dropbox_path+othersumpath,mode=dropbox.files.WriteMode.overwrite)
    os.remove(mysumpath)
    os.remove(mychorespath)
    os.remove(otherlogpath)
    os.remove(othersumpath)


    
    
    
    
    
    



root = Tk()
root.title("BourbouBank")
root.geometry("400x400")
#root.iconbitmap("resource/BourbouWallet.ico")
print("Downloading Data from the Cloud...")
Download()



mysumfile = open(mysumpath,'r')
mysum = int(mysumfile.read())
mysumfile.close()
#down = Button(root, text = "Download", command = Download)
#down.pack()
#up = Button(root, text = "Upload", command = Upload)
#up.pack()
   
lbl = Label(root, text = "Add new Chore")
points =Label(root,text = "You currently have : " + str(mysum) +" Brb") 

chores = [
    "ΔΙΑΦΟΡΑ",
    "ΠΙΑΤΑ",
    "ΣΚΟΥΠΑ",
    "ΣΦΟΥΓΓΑΡΙΣΜΑ",
    "ΠΛΥΝΤΗΡΙΟ",
    "ΑΠΛΩΜΑ",
    "ΣΙΔΕΡΟ",
    "ΣΚΟΥΠΙΔΙΑ",
    "SUPER-MARKET",
    "ΤΑΚΤΟΠΟΙΗΣΗ",
    "Κ. ΨΥΓΕΙΟΥ",
    "ΠΑΝΤΖΟΥΡΙΑ",
    "ΤΖΑΜΙΑ",
    "ΜΠΑΝΙΟ",
    "ΚΟΥΖΙΝΑ"]
chorepoints = [0,20,40,40,25,30,25,10,20,10,20,40,40,40,10]
    

clicked = StringVar()
clicked.set (chores[0])
choice = clicked.get()

    
drop = OptionMenu(root, clicked, *chores)

mylabel = Label(root,text = "BourbouBank")


def choosecom():
    choice = clicked.get()
    selectionNr = chores.index(choice)
    deltapoints = chorepoints[selectionNr]
    lb1 = Label(root , text = "Chore : " )
    chorelb = Label(root, text = choice)
    lb2 = Label(root, text = "Price(Brb) : ")
    chorepoint = Entry(root)
    
    
    def confirm ():
        
        mysumf = open(mysumpath,"r")
        mysumold = int(mysumf.read())
        mysumf.close()
        othersum = open(othersumpath,"r")
        othersumold = int(othersum.read())
        othersum.close()


        mysumf = open(mysumpath,"w")
        mychores = open(mychorespath,"a")
        otherlog =open(otherlogpath,"a")
        othersum = open(othersumpath,"w")

        
        mysumnew = mysumold + int(chorepoint.get()) 
        mysumf.write(str(mysumnew))
        mychores.write(choice + " " + str(chorepoint.get())+ '\n')
        otherlog.write(choice + " " + str(-1*int(chorepoint.get()))+ '\n')
        othersumnew = othersumold - int(chorepoint.get()) 
        othersum.write(str(othersumnew))


        mysumf.close()
        mychores.close()
        otherlog.close()
        othersum.close()
        lb1.destroy()
        chorelb.destroy()
        lb2.destroy()
        chorepoint.destroy()
        Confirm.destroy()
        mysumf = open(mysumpath,"r")
        mysum = int(mysumf.read())
        mysumf.close()
        points.destroy()
        pointsnew = Label(root,text ="You now have : " + str(mysum) +" Brb") 
        pointsnew.pack()
        



     
    Confirm = Button(root, text = "Confirm",command = confirm)
    lb1.pack()
    chorelb.pack()
    lb2.pack()
    chorepoint.pack()
    chorepoint.insert(0,deltapoints)
    Confirm.pack()
    




  
choose = Button(root, text = "Choose", command = choosecom)

mylabel.pack()

lbl.pack()
drop.pack()
choose.pack()

points.pack()
root.mainloop()
print ("Saving Changes Don't Close ....")
Upload()

 
