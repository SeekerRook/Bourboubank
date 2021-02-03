import dropbox
import os
print("Loading...")
dropbox_access_token= "Q22At0HeNXAAAAAAAAAAEwBD7CXHFR8yG0BUZuCVV-_HGpBfDzyQOj2Lw8mXqXeG"    
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
    username = input("Give Old Password : ")
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
print ("######### WELCOME #########")
newkey = input("Give New Password : ")
client.files_download_to_file(computer_path+my+"password.txt", dropbox_path+my+"password.txt")
chrispassword = open(my+"password.txt","w")
chrispassword.write(newkey)
chrispassword.close()
client.files_upload(open(computer_path+my+"password.txt", "rb").read(), dropbox_path+my+"password.txt",mode=dropbox.files.WriteMode.overwrite)
os.remove(my+"password.txt")

 
