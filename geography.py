#import replit
#replit.clear()
#the above is specifically for the website i used (replit.com), you can ignore it
import random
print("Welcome to my US geography quiz!")
tf1=0
while (tf1==0):
  lengthQuestionList=int(input("How many questions do you want?"))
  if(not(lengthQuestionList>0 and lengthQuestionList<12)):
   print("That will not work, at least 1 question, at most 11 questions!!!")
  else:
    tf1=1
#print("here1")
questionList=[]
userAnswers=[]
alreadyChoosenNumbers=[]
actualAnswers={0:3, 1:4, 2:4, 3:2, 4:4, 5:3, 6:1, 7:2, 8:3, 9:1, 10:3}
#correct is 0, wrong is 1
correctOrWrong=[]
def question0():
  userAnswers.append(int(input("What is the only triply landlocked state in the US?\n1: Kansas\n2:Iowa\n3:Nebraska\n4:South Dakota\n")))
def question1():
  userAnswers.append(int(input("What is the state in which the most Easternmost point, by longitude, is located?\n1:Hawaii\n2:Maine\n3:New York\n4:Alaska\n")))
def question2():
  userAnswers.append(int(input("What is the only great lake entirely in the US?\n1:Lake Huron\n2:Lake Superior\n3:Lake Erie\n4:Lake Michigan\n")))
def question3():
  userAnswers.append(int(input("How many Rhode Islands can fit into Alaska?\n1:32\n2:425\n3:1049\n4:None of the above\n")))
def question4():
  userAnswers.append(int(input("Which state is closest to New York City?\n1:Connecticut\n2:Massachusetts\n3:Connecticut\n4:New Jersey\n")))
def question5():
  userAnswers.append(int(input("Which state does Oregon not border?\n1:California\n2:Idaho\n3:Wyoming\n4:Washington\n")))
def question6():
  userAnswers.append(int(input("Which became a state first Alaska or Hawaii?\n1:Alaska by a few months\n2:Hawaii by a few days\n3:No-one knows\n4:Hawaii by a few months\n")))
def question7():
  userAnswers.append(int(input("What was the first state admitted? (not counting the original 13)\n1:Kentucky\n2:Vermont\n3:Maine\n4:Tennesse\n")))
def question8():
  userAnswers.append(int(input("Which became a state first, North or South Dakota?\n1:North Dakota by a few seconds\n2:South Dakota by a few days\n3:No-one knows\n4:North Dakota by a few weeks\n")))
def question9():
  userAnswers.append(int(input("Maine has more borders with Canadian provinces then with US states?\n1:True\n2:False\n3:I don't know\n4:What's a province\n")))
def question10():
  userAnswers.append(int(input("Which state looks like a rectangle?\n1:Nevada\n2:Idaho\n3:Kansas\n4:Missouri\n")))
def questionOrderGiver(questionsNumber):
  i=0
  while(i<questionsNumber):
    global alreadyChoosenNumbers
    randNum=random.randrange(0,11)
    alreadyChoosenNumbers.append(randNum)
    #print("a")
    if(len(alreadyChoosenNumbers)!=len(set(alreadyChoosenNumbers))):
      alreadyChoosenNumbers=list(set(alreadyChoosenNumbers))
      i=i-1
    i=i+1
  #this should be 3b
  #random.shuffle(alreadyChoosenNumbers)
  #print(alreadyChoosenNumbers)
def questionInList(numList):
  for i in range(len(numList)):
    if (numList[i]==0):
      questionList.append(question0)
    elif (numList[i]==1):
      questionList.append(question1)
    elif (numList[i]==2):
      questionList.append(question2)
    elif (numList[i]==3):
      questionList.append(question3)
    elif (numList[i]==4):
      questionList.append(question4)
    elif (numList[i]==5):
      questionList.append(question5)
    elif (numList[i]==6):
      questionList.append(question6)
    elif (numList[i]==7):
      questionList.append(question7)
    elif (numList[i]==8):
      questionList.append(question8)
    elif (numList[i]==9):
      questionList.append(question9)
    elif (numList[i]==10):
      questionList.append(question10)
  #random.shuffle(questionList)
def questionGiver(questions):
  for i in range(len(questions)):
    print("Question "+str(i+1)+":")
    questions[i]()
#alreadyChoosenNumbers and userAnswers
def answerCheck(questions,answers):
  for i in range(len(questions)):
    theUserAnswer=answers[i]
    if (theUserAnswer==actualAnswers[questions[i]]):
      correctOrWrong.append(0)
    elif (theUserAnswer>4 or theUserAnswer<1):
      correctOrWrong.append(2)
    else:
      correctOrWrong.append(1)
  #print(alreadyChoosenNumbers)
  #print(correctOrWrong)
questionOrderGiver(lengthQuestionList)
#print("here2")
questionInList(alreadyChoosenNumbers)
#print("here3")
questionGiver(questionList)
#print("here4")
answerCheck(alreadyChoosenNumbers, userAnswers)
def gettingPercentageCorrect(checkingList):
  theTotalCorrectAnswers=0
  for i in range(len(checkingList)):
   #print("b1")
   if (checkingList[i]==0):
      theTotalCorrectAnswers+=1
      #print("b2")
  #global thePercentageCorrect
  decimalPercentage=(theTotalCorrectAnswers/len(checkingList))
  thePercentageCorrect=100*decimalPercentage
  print(f"You got {thePercentageCorrect:.2f}% correct.")
  if (thePercentageCorrect>59.5):
    print("Congratulations, you passed!!!")
  else:
    print("Unfortunately, you did not pass!!!")
#3c
gettingPercentageCorrect(correctOrWrong)
#print(f"You got {thePercentageCorrect:.2f}% correct.")
for j in range(len(correctOrWrong)):
  if (correctOrWrong[j]==0):
    correctOrWrong[j]="Correct"
  elif (correctOrWrong[j]==2):
    correctOrWrong[j]="Wrong, an invalid input was entered"
  else:
    correctOrWrong[j]="Wrong"
#print(correctOrWrong)
for k in range(len(correctOrWrong)):
  print("You got question #"+str(k+1)+" "+correctOrWrong[k])
