'''
Your local university's Raptors fan club maintains a register of its active members on a .txt document. 
Every month they update the file by removing the members who are not active. You have been tasked with 
automating this with your python skills. Given the file currentMem, Remove each member with a 'no' in 
their inactive coloumn. Keep track of each of the removed members and append them to the exMem file. 
Make sure the format of the original files in preserved. (Hint: Do this by reading/writing whole lines 
and ensuring the header remains ) 
'''
#Need random generator to create fictinal data file
from random import randint as rnd
#Define necessary text files
currentMem = members.txt
exMem = inactive.txt
#need a new variable to assign if memeber is active or not
#we want to keep it same hence tuple is best choice
act = ('yes','no')

#create a function that generates two files members.txt and inactive.txt
def generateFiles(current, past):
  #fill the file with current members
  with open(current,'w+') as writeMod:
    writeMod.write('Member ID Registration Date Active'\n)
    #format the data for visualization
    data = '{:<9} {:<16} {:<6}'
    #create 30 random members
    for rowNum in range(30):
      date = str(rnd(2018,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,26))
      writeMod.write(data.format(rnd(10000,99999),date,act[rnd(0,1)])
                     
  #fill the file with inactive members
  with open(past,'w+') as writeMod:
    writeMod.write('Member ID Registration Date Active'\n)
    #format the data for visualization
    data = '{:<9} {:<16} {:<6}'
    #create 5 random members
    for rowNum in range(5):
      date = str(rnd(2018,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,26))
      writeMod.write(data.format(rnd(10000,99999),date,act[1])   
                     
#Now call the function to create files
generateFiles(currentMem,exMem)

#Write function to update dayly these two files
def updateDayly(currentList,inactiveList):
   #open two files at the same time and revise them
   with open(currentList,'w+') as writeFile
      with open(inactiveList,'a+') as appendFile
          #Make sure the position of write
          writeFile.seek(0)
          #make copy of all data from currentLsit
          lists = currentList.readlines()
          #store header and remove it from lists
          header = lists[0]
          lists.pop(0)
          #check lists and store all inactive members
          inactive = [row for row in lists if ('no' in row)]
          #above lines can be replaced by the lines below
          '''
            for member in members:
                if('no' in member):
                    inactive.append(member)
          '''
          #Make sure the position of write                  
          writeFile.seek(0)
          #put the header back
          writeFile.write(header)
          #go over lists
          for row in lists:
               if(row in inactive):
                     appendFile.write(row)
               else:
                     writeFile.write(row)
          #the rest of the writeFile will be cleaned
          writeFile.truncate()

#create input parameters for updateDayly function
currentMem = members.txt
exMem = inactive.txt
updateDayly(currentMem,exMem)
                     
                     
#print two files for debugging
with open(currentMem,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exMem,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
