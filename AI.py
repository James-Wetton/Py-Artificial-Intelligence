import time
import random
import os
import sys
import pybase64
from string import ascii_lowercase
from collections import Counter
x = 1


usernamecheck = 0 
while usernamecheck == 0:
    try:
        print("To restart, type \'quit()\' in any field")
        time.sleep(x)
        foo = ['Have we spoken before? ', 'Wait, have we spoken before? ', 'Have we met? ']
        ask = random.choice(foo)
        os.system("say . " + ask)
        used = input(ask)
        time.sleep(x)
        if used == ('quit()'):
            pass
        if used in ('Y', 'Yes', 'y', 'yes'):
            username = input("What's your name again? ")
            if os.path.exists(username + '.txt'):
                time.sleep(x)
                print("I thought I remembered you!")
                time.sleep(2)
                f = open(username + '_password.txt', 'r')
                enterpass = f.readline()
                enterpass = pybase64.standard_b64decode(enterpass)
                enterpass = str(enterpass)
                enterpass = enterpass[2:]
                enterpass = enterpass[:-1]
                correctpass = 0
                while correctpass == 0:
                    temppassword = input("Please enter your password: ")
                    if temppassword == enterpass:
                        correctpass = correctpass + 1
                    else:
                        print("Incorrect password. Please try again.")
                        time.sleep(x)
                        

                time.sleep(x) 
                f = open(username + '.txt', 'r')
                name = f.readline()
                age = f.readline()
                colour = f.readline()
                print("\n")
                print("Your name is " + name + "and you're " + str(age) + " ")
                print("Your favourite colour is " + colour)
                correct = input("Am I right? ")
                if correct in ('Y', 'y', 'Yes', 'yes'):
                    print("I thought so...")
                    f.close()
                    f = open(username + '.txt', 'a')
                else:
                    time.sleep(x)
                    print("I'm sorry")
                    time.sleep(x)
                    print("Please make an account")
                    time.sleep(x)
                    print("Rebooting...")
                    time.sleep(2)
                    print("\n \n")
                    pass
            else:
                time.sleep(x)
                print("Sorry, I don't remember anybody called " + username)
                
        else:
            name = input("What's your name? ")
            time.sleep(x)
            if name == ('quit()'):
                pass
            else:
                print("Nice to meet you " + name + "!")
                f = open(name + '.txt', 'w')
                f.write(name + '\n')
                time.sleep(x)
        
                age = input("How old are you? ")
                time.sleep(x)
        
                print("You are already " + str(age) + " years old!")
                f.write(str(age) + '\n')
                time.sleep(x)
            
                colour = input("So, " + name + " , what's your favourite colour? ")
                time.sleep(x)
        
                print("I really love " + colour + " too !")
                f.write(colour + '\n')
                f.close()

                time.sleep(2)

                print("Hey, I think to keep your data secure, we should add a password.")
                makepass = 0
                while makepass == 0:
                    f = open(name + '_password.txt', 'w')
                    time.sleep(2)
                    password = str(input("What would you like your password to be? \nP.S. make it something you will remember...\nmake it at least 5 letters long "))
                    f.write(password)
                    f.close()
                    f = open(name + '_password.txt', 'r')
                    characters = 0
                    for line in f:
                        characters = characters + len(line)
                        
                    if characters > 4:
                        print("Great! I don't think anyone will crack that one...")
                        f.close()
                        makepass = 1
                        time.sleep(x)
                    else:
                        time.sleep(x)
                        print("I think that is going to be to easy to crack! Please make it at least 5 letters long")
                        pass
                f = open(name + '_password.txt', 'w')
                encodedpass = password.encode('utf-8')
                cr = pybase64.standard_b64encode(encodedpass)
                cr = cr.decode('utf-8')
                print("Encrypting password...")
                f.write(cr)
                f.write('\n')
                time.sleep(x)
                f.close()
                print()
            
    except KeyboardInterrupt:
        break
        
        

    


