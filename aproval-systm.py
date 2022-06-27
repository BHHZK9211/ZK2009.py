def main_apv():
    os.system('clear')
    ak="Z_K_9211"
    logo()
    os.system('xdg-open https://www.Facebook.com/zkkhan9211')
    try:
        key1=open('/data/data/com.termux/files/usr/bin/.zeeshan-cov', 'r').read()
    except IOError:
        os.system("clear")
        logo()
        print ("[*]--------------------------------------------------------------")
        print ("  Your Token Is Not Approved Already")
        print ("[*]--------------------------------------------------------------")
        print ("           THIS TOOL IS PAID RS 350")
        print ("           THIS IS YOUR KEY BRO")
        print ("[*]--------------------------------------------------------------")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid)
        print ("[*]--------------------------------------------------------------")
        kok=open('/data/data/com.termux/files/usr/bin/.zeeshan-cov', 'w')
        kok.close()
        print ("")
        print ("")
        print ("     Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("[*]--------------------------------------------------------------")
        time.sleep(6) 
        os.system("xdg-open https://wa.me/+923125939861")
    r1=requests.get("https://github.com/BHHZK9211/ZK2009.py").text
    if key1 in r1:
    
        R()
    else:
        os.system("clear")
        os.system('xdg-open https://Facebook.com/zkkhan9211')
        logo()
        print ("[*]--------------------------------------------------------------")
        print ("  Your Token Is Not Approved Already")
        print ("[*]--------------------------------------------------------------")
        print ("          THIS IS YOUR KEY BRO")
        print ("[*]--------------------------------------------------------------")
        print ("")
        print ("          YOUR KEY : "+ak+key1)
        print ("[*]--------------------------------------------------------------")
        print ("     Copy Key And Sent Me WP Approvel Your Key ")
        print ("[*]--------------------------------------------------------------")
        time.sleep(3.5)
        #Numbr chnge krlyna
        os.system("xdg-open https://wa.me/+923125939861")
