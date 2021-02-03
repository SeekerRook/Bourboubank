import dropbox
import os


mysumpath = "chrissum.txt"
mychorespath = "chrislog.txt"
otherlogpath = "evanlog.txt"
othersumpath = "evansum.txt"

dropbox_access_token= "Q22At0HeNXAAAAAAAAAAEwBD7CXHFR8yG0BUZuCVV-_HGpBfDzyQOj2Lw8mXqXeG"    
dropbox_path= "/Application/"
computer_path=""
client = dropbox.Dropbox(dropbox_access_token)

client.files_download_to_file(computer_path+mysumpath, dropbox_path+mysumpath)
client.files_download_to_file(computer_path+mychorespath, dropbox_path+mychorespath)
client.files_download_to_file(computer_path+otherlogpath, dropbox_path+otherlogpath)
client.files_download_to_file(computer_path+othersumpath, dropbox_path+othersumpath)

chrissum = open(mysumpath,"w")
chrissum.write("460")
chrissum.close()
evansum = open(othersumpath,"w")
evansum.write("460")
evansum.close()
chrislog = open(mychorespath,"w")
chrislog.write("")
chrislog.close()
evanlog = open(otherlogpath,"w")
evanlog.write("")
evanlog.close()




client.files_upload(open(computer_path+mysumpath, "rb").read(), dropbox_path+mysumpath,mode=dropbox.files.WriteMode.overwrite)
client.files_upload(open(computer_path+mychorespath, "rb").read(), dropbox_path+mychorespath,mode=dropbox.files.WriteMode.overwrite)
client.files_upload(open(computer_path+otherlogpath, "rb").read(), dropbox_path+otherlogpath,mode=dropbox.files.WriteMode.overwrite)
client.files_upload(open(computer_path+othersumpath, "rb").read(), dropbox_path+othersumpath,mode=dropbox.files.WriteMode.overwrite)
os.remove(mysumpath)
os.remove(mychorespath)
os.remove(otherlogpath)
os.remove(othersumpath)
