#import webbrowser
#webbrowser.open('https://www.google.com/maps/place/870+Valencia+St/@37.7590311,-122.4215096,17z/data=!3m1!4b1!4m2!3m1!1s0x808f7e3dadc07a37:0xc86b0b2bb93b73d8.')
#print('How are you?')
#feeling = input()
#if feeling.lower() == 'great':
#   print('I feel great too.')
#else:
#   print('I hope the rest of your day is good.')
#def isPhoneNumber(text):
#   if len(text) != 12:

#return False
#   for i in range(0, 3):
#       if not text[i].isdecimal():
#            return False
#   if text[3] != '-':
#       return False
# for i in range(4, 7):
#       if not text[i].isdecimal():
 #           return False
#  if text[7] != '-':
#      return False
#   for i in range(8, 12):
#       if not text[i].isdecimal():
#            return False
#   return True
#
#print('Is 415-555-4242 a phone number?')
#print(isPhoneNumber('415-555-4242'))
#print('Is Moshi moshi a phone number?')
#print(isPhoneNumber('Moshi moshi'))
#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

#import webbrowser, sys
#if len(sys.argv) > 1:
#    # Get address from command line.
#    address = ' '.join(sys.argv[1:])
#webbrowser.open('https://www.google.com/maps/place/' + address)    

#import pandas as pd
#df = pd.read_csv('state_au.csv')
#print(df)

#PDF FORMAT LLESSPMMMMMM,MM,,,,,,,,,,

#import PyPDF2
#file = open('baby.pdf','rb')
#pdfReader = PyPDF2.PdfReader(file)
#total = len(pdfReader.pages)
#print(total)
#page = pdfReader.pages[0]
#print(page.extract_Text)

#import pyinputplus as pyip
#def addsUpToTen(numbers):
#    numberList = list(numbers)
#    for i, digit in enumerate(numbersList):
#        numbersList[i] = int(digit)
#    if sum(numberList) !=10:
#        raise Exception('The digits must add up to 10, not %s.' %(sum(numberList)))
#    return int(number) 
#response = pyip.inputCustom(addsUpToTen)   


#from pathlib import Path
#myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
#for filename  in myFiles:
#    print(Path(r'C:\Users\Al', filename))

#from pathlib import Path
#p = Path('spam.txt')
#print(p.write_text('Hello, world'))

#import requests
#res = requests.get('https://automatetheboringstuff.com/2e/chapter12/')
#print(res.text[:250])


#debugging



#ages = [26,33,34,23,35,38,39]
#ages.sort()
#print(ages)

#market_2nd = {'ns': 'green', 'ew': 'red'}
#mission_16th = {'ns': 'red', 'ew': 'green'}


#def switchLights(stoplight):
 #   for key in stoplight.keys():
  #      if stoplight[key] == 'green':
   #         stoplight[key] = 'yellow'
    #    elif stoplight[key] == 'yellow':
     #       stoplight[key] = 'red'
      #  elif stoplight[key] == 'red':
       #     stoplight[key] = 'green'

#print(switchLights(mission_16th))


import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')