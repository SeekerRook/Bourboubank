from tkinter import *
import dropbox
import os
dropbox_access_token= "8ir-9dbTA8oAAAAAAAAAAcLaEySyI34UiJqFhPLCYR4xUGry83woZWxS8f5N5uV5"    
dropbox_path= "/Application/"
computer_path=""
client = dropbox.Dropbox(dropbox_access_token)
root = Tk()
root.title("BourbouPrint")
root.geometry("400x400")
#root.iconbitmap("resource/BourbouPrint.ico")
usernamec = StringVar()
usernamec.set("None")
namel = Label(root, text = "Name : ")
namel.pack()
namedrop = OptionMenu(root,usernamec,"Christoforos","Evangelos")
namedrop.pack()
filetypec = StringVar()
filetypec.set("None")
filetypel = Label(root, text = "File : ")
filetypel.pack()
filedrop = OptionMenu(root,filetypec,"Total Sum","All movement")
filedrop.pack()




def Download():
    
    if str(usernamec.get()) == "Christoforos":
        username = "chris"
    elif str(usernamec.get())== "Evangelos":
        username = "evan"
    else :
        username = ""   
    if str(filetypec.get()) == "Total Sum":
        filetype = "sum"
    elif str(filetypec.get())== "All movement":
        filetype = "log"
    else :
        filetype = ""

    if (username == "" or filetype == "" ):
        error = Tk()
        error.title("ERROR")
        text = Label(error, text = "Select Name and Filetype")
        text.pack()
    else :  

        mysumpath = username + filetype +".txt"
        mysumpathd = username + filetype +"Copy.txt"
        client.files_download_to_file(computer_path+mysumpathd, dropbox_path+mysumpath)
        Success = Label (root, text = "Successful Download to : "+mysumpathd)
        Success.pack()


down = Button(root , text = "Download Selection",command = Download)
down.pack() 
root.mainloop()  
