print('This project uses the DRK library')
sendingstatus = ''
try:
  from replit import db
except:
  print('We highly reccomend that you use replit for this library')
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '?', ',', '<', '>', '/', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '[', ']', '{', '}', '\\', '|', '"', "'", ':', ';', '~', '`', ' ']
email = os.getenv('email')
password = os.getenv('password')

def makeFile(name, data):
  file = open(name, 'w')
  file.write(data)

def makeFolder(name):
  try:
    os.makedirs(name)
  except:
    x = 1

def ask(question):
  output = input(question + '? ')
  return output

#def updateFile(path1, path2):
  #if not old == open(path2).read():
    #old = open(path1).read()
    #makeFile(path2, old)

def options(question, optionList):
  options = ''
  answer = ''
  for i in range(0,len(optionList)):
    options = options + optionList[i] + '/'
  while not answer in optionList:
    answer = input(question + ' (' + options + '): ')
    if not answer in optionList:
      print('We are sorry, but that is not option. Try again and make sure capitalization and spelling is correct')
  return answer

def database(name):
  answer = input('You can run: (Add/Search/Remove) ')
  if answer == 'Add':
    db[name].append(input('What would you like to add? '))
  elif  answer == 'Search':
    answer = input('What would you like to search for? (If you want to look for everything, just type \'*\') ')
    answerlist = list()
    for i in range(0,len(db[name])):
      if answer in db[name][i] or answer == '*':
        answerlist.append('File #' + str(i) + ': ' + db[name][i])
      print('%'+str(round(float(i + 1)/float(len(db[name])) * 100.0))+' searched')
    if not answer in db[name] and not answer == '*':
      print('We could not find anything along the lines of \'' + answer + '\'')
    else:
      print('')
      print('Answers:')
      print('')
      for i in range(0,len(answerlist)):
        print(answerlist[i])
      print('')
  elif  answer == 'Remove':
    answer = int(input('What number file would you like to remove '))
    print('Removing '+db[name][answer]+'...')
    del db[name][answer]
    print('File #' + str(answer)+' has been removed')
  else:
    print('We are sorry, but that is not command. Try again and make sure capitalization and spelling is correct')

def databaseAdd(name,data):
  db[name].append(data)

def databaseSearch(name,quarry):
  output = list()
  for i in range(0,len(db[name])):
    if quarry in db[name][i] or quarry == '*':
      output.append(i)
  return output

def databaseRemove(name, fileNumber):
  del db[name][fileNumber]

def databaseGet(name, fileNumber):
  output = db[name][fileNumber]
  return output

def encode(data,amount):
  output = ''
  for i in range(0,len(data)):
    for x in range(0, len(alphabet)):
      encoded = x + amount + i
      while encoded > len(alphabet):
        encoded -= len(alphabet)
      if alphabet[x] == data[i]:
        output = output + alphabet[encoded]
  return output

def decode(data,amount):
  output = ''
  for i in range(0,len(data)):
    for x in range(0, len(alphabet)):
      encoded = x - amount - i
      while encoded < 0:
        encoded += len(alphabet)
      if alphabet[x] == data[i]:
        output = output + alphabet[encoded]
  return output

def sendEmail(sendmsg, to, sub):
  try:
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = to
    msg['Subject'] = sub

    msg.attach(MIMEText(sendmsg, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
  except:
    debugLog('sendEmail','An uknown error occured')
  try:
    server.login(email, password)
  except:
    debugLog('sendEmail','Failed to login')
  try:
    text = msg.as_string()
  except:
    debugLog('sendEmail','Failed to convert messages')
  try:
    server.sendmail(email, to, text)
  except:
    debugLog('sendEmail','Failed to send email')
  try:
    server.quit()
  except:
    debugLog('sendEmail','Failed to log out')

def debugLog(catagory,message):
  print('Error in DRK library: ' + catagory + ': ' + message)
