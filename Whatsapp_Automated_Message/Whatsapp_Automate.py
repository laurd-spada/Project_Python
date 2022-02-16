#This package must be installed before the code can be properly executed
# pip install pywhatkit

import pywhatkit
special_number = input("Please enter a number you wouldlike to automate messages to: ")
special_message = input("Enter the special message you want automated")
time = int(input("Enter the time to start calculating from. e.g Hour, Minute - 12, 30 : "))

pywhatkit.sendwhatmsg(special_number, special_message, time)