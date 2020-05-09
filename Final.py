

###For testing purposes
###use https://www.guerrillamail.com/inbox 
###set the address to Python@sharklasers.com


import argparse
import smtplib
import requests

from bs4 import BeautifulSoup

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}

domain = 'https://www.amazon.com'

URL = 'https://www.amazon.com/Stonemaier-Games-STM900-Wingspan-Game/dp/B07MC9JN56/ref=sr_1_1?dchild=1&keywords=wingspan&qid=1588433425&rnid=2470954011&sr=8-1'

# this works don't mess with it...
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, features="lxml")
title = soup.select("#productTitle")[0].get_text().strip()
   #print(tag.contents[0])
   #print(blah)
   #print(i)
   #print(i.get_text())
   #print(i.get_text())
amazonprice = int(soup.select("#priceblock_ourprice")[0].get_text().strip()[1:-3])

# argparse
parser = argparse.ArgumentParser("This program is a web bot that scrapes amazon for the price of wingspan. Please note you must set up the email you send with --send and the e-mail you recieve with -s and a price you are looking for with -p for this to work.")
group = parser.add_mutually_exclusive_group()


# Set up email
# set up sending email and password normally I would store in the file this way I don't have to give my own
group.add_argument("-s","--saveemail", help="Use this option to write to set your e-mail")
group.add_argument("-del","--deleteemail",  help="Use this option to delete your email")
group.add_argument("-w","--whatemail",  action='store_true', help="Use this option to display what email you have saved")
group.add_argument("--emailme", action='store_true', help="send test email")
group.add_argument("-send","--setsendingemail",  action='store_true', help="Use this to set the email you send from. Set up to be sent from gmail")
group.add_argument("-epass", "--setsendemailpass",  action='store_true', help="Use this to set your sending email password")

group.add_argument("-set", "--setprice",  help="Use this to set the price threshold you want to be notified with")
group.add_argument("-p", "--price", action='store_true', help="Use this to tell you what your current price threshold is")

args = parser.parse_args()
# store email in plain text (yes I know this is bad)
if args.saveemail:
    f = open("saveemail.txt", "w")
    f.write(args.saveemail)
    f.close()

# Store sending email 
if args.setsendingemail:
    f = open("sendemail.txt", "w")
    f.write(args.setsendingemail)
    f.close()

# Store sending email password
if args.setsendemailpass:
    f = open("sendemailpass.txt", "w")
    f.write(args.setsendemailpass)
    f.close()



# delete email file
if args.deleteemail:
    f = open('saveemail.txt', "w")
    f.truncate()
    f.close()

# show what price you have set
if args.whatemail:
    f = open("saveemail.txt", "r")
    print(f.read())
    f.close()


# price threshold
if args.setprice:
    setprice = args.setprice
    f = open("price.txt", "w")
    f.write(setprice)
    f.close()

# show what price you have set
if args.price:
    f = open("price.txt", "r")
    print(f.read())
    f.close()

# opening sendemail.txt convert to variable to use in email script
def sending_email():
    f = open("sendemail.txt", "r")
    sendemail = f.read()
    f.close()
    return sendemail

sendmail = sending_email()

def send_pass():
    f = open("sendemailpass.txt", "r")
    sendpass = f.read()
    f.close()
    return sendpass

emailpass = send_pass()




# sends test email to the email stored 
if args.emailme:
    f = open("saveemail.txt", "r")
    email_me = f.read()
    f.close()
    li = [email_me] 
  
    for dest in li: 
        s = smtplib.SMTP('https://www.guerrillamail.com/inbox', 587) 
        s.starttls() 
        s.login(sendmail, "python") 
        message = "Is this thing on??"
        s.sendmail(sendmail, dest, message) 
        s.quit() 



# price comparison
def price_thresh():
    f = open("price.txt", 'r')
    my_price = f.read()
    
    f.close()
    return my_price

myprice = int(price_thresh())


# compare price and send email if needed 
if amazonprice <= myprice:
    
    f = open("saveemail.txt", "r")
    email_deal = f.read()
    f.close()
    li = [email_deal] 
  
    for dest in li: 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("python@sharklasers.com", "python") 
        message = "price alert"
        s.sendmail("python@sharklasers.com", dest, message) 
        s.quit()
        print("price alert email sent")



