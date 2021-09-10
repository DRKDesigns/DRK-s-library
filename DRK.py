print('This project uses the DRK library')
def ask(question):
  answer = input(question + '? ')

def options(question, optionList):
  options = ''
  answer = ''
  for i in range(0,len(optionList)):
    options = options + optionList[i] + '/'
  while not answer in optionList:
    answer = input(question + ' (' + options + '): ')
    if not answer in optionList:
      print('We are sorry, but that is not option. Try again and make sure capitalization and spelling is correct')
      clear = False
