import ftplib

# Connect to my VM

f = ftplib.FTP("192.168.2.166")
# set IP address
try:
    # username and password for login
    f.login("root", "toor")
    # expect welcome
    print(f.getwelcome())
    #f.delete("test")
    print(f.dir())
    f.set_pasv(1)
    #fstorbinary("STOR test", open("test", "rb"))
    #print(f.dir())
except Exception as e:
    print("Exeption:", e)
finally:
    f.close()
