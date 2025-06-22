#!/bin/python3
from pyngrok import ngrok
import os
import keyboard
import readline, glob
import sys
import paperclip
import getpass
import pexpect
os.system("clear")
#COLORS
# Python program to print 
# colored text and background 
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 
def prHighLight(skk): print("\033[103m {}\033[00m" .format(skk))
##Auto dir complete ##
def complete(text, state):
    return (glob.glob(text+'*')+[None])[state]



file_holder = []
command_list = []
weblist = []
show_files = []


#check Ngrok token
def token_check():
    pass


# HTTP SERVER 
def http_server():
    child = pexpect.spawn("/bin/bash")
    child.sendline("cd /var/www/html")
    child.sendline(f"python -m SimpleHTTPServer {port}")
    
    prYellow('Press "q" if your files are uplaoded successsfully')
    prRed('Press "ctrl+c" to force stop')
    print(f'''
HTTP Server : {new_ip}
Hope, you have specified a right path or paths.

    ''')
    intrupt(weblist)


# A function to send or to recive Files
def sendrev():
    global askforsr
    global port
    global new_ip
    
    prPurple("@luckythandel")
    askforsr = input(f'''
        ---Actions---
    
    (1.) Send
    (2.) Receive
    (3.) Exit
    Choose one - [1,2,3]
    \n==> ''')
    if askforsr == "1":
        
        port = input("\n[+] Port\n==> ")
        new_ip = ngrok.connect(port, "http")
        #TAB AUTO Complete
        readline.set_completer_delims(' \t\n;')
        readline.parse_and_bind("tab: complete")
        readline.set_completer(complete)
        filenames = input("\n[+] FILENAME: ")
        #END
        if len(filenames) == 0:
        
            prRed("Not valid Input, Try again.\n")
            sendrev()
        
        else:
            
            print("Your files have been selected!")
            splited_files = filenames.split(" ")
                      
            for one_file in range(0,len(splited_files[:])):
                
                file_holder.append(splited_files[one_file])
                web_file = os.path.basename(splited_files[one_file])
                weblist.append(web_file)                
                prGreen(f"Your file is: {weblist[one_file]}\n")
                new_file = file_holder[one_file]
                os.system(f"cp -r {new_file} /var/www/html")
                global realfile
                realfile = weblist[one_file]
                
                Command1 = f'''
   [+] Run This Command On The Server 
    ==> wget {new_ip}/{realfile}      
                    '''
                    

                prLightPurple(Command1)
                
            else:

                http_server()
            
            
    elif askforsr == "2":
        print("\nYou have chosed to recieve files\n")

        prGreen("What would you like to use to recieve File.")     
        
        ques2 = input('''
            (1.) Netcat
            (2.) Wget
            (3.) curl
            choose one - [1,2,3]
            \n==>''')
        
        
        ques3 = input("\nFile name to saved as\n==> ")
        
        if ques2 == "1":
            prYellow('''       
                             ###WARNING###
        Script won't check if the File exist or if the host is down or not.
        You will need to check it yourself. provide correct information to 
        downlaod the files.
        
            ''')
            token = input("[+] Ngrok Token\n==> ")
            
            ngrok.set_auth_token(token)
            ques5 = input("\nPort\n==> ")
            new_ip = ngrok.connect(int(ques5), 'tcp')
            new_ip1 = new_ip.split("/")
            ngrok_ip = new_ip1[2]            
            new_ip2 = ngrok_ip.split(":")
            ngrok_ip2 = new_ip2[0]
            ngrok_port = new_ip2[1]

            prLightPurple(f'''
            
    [+] Run This Command On Server: 
    ==> nc {ngrok_ip2} {ngrok_port} < <File Path>


            ''')
            child = pexpect.spawn("/bin/bash")
            child.sendline(f"nc -lvp {ques5} > {ques3} ")
            child.interact()

            prGreen("Your file is downloaded!")
            ngrok.kill()
            exit(0)
           
            
        
        elif ques2 == "2":
            server_ip = input("\nServer Address [exp: http://example.in/]\n==> ")
            if server_ip.endswith("/"):
                os.system(f"wget {server_ip}{ques3}")
            else:
                os.system(f"wget {server_ip}/{ques3}")
                

        elif ques2 == "3":
            server_ip = input("\nServer Address [exp: http://example.in/]\n==> ")
            if server_ip.endswith("/"):
                os.system(f"curl {server_ip}{ques3}")
            else:
                os.system(f"curl {server_ip}/{ques3}")
        else:
            prRed("\nPress Ctrl+c to exit\n")
            exit(0)

    else:
        prGreen("Exiting...")
        exit(0)


def intrupt(arg1):
  
    while True:

        if keyboard.is_pressed("q"):
            
            for remove_file in range(0,len(arg1[:])):
                print(arg1[remove_file])
                os.chdir("/var/www/html")
                os.system('pwd')
                os.system(f"rm -r {arg1[remove_file]}")

            prYellow("\n[+] All the files have been removed from the /var/www/html\n")
            ngrok.kill()
            exit(0)
         
            

sendrev()







