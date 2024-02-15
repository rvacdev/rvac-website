from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
import os
import re

#change url locations as needed
CLASS_PATH=os.path.abspath('C:\\Users\\pjf08\\Documents\\college classes\\Fall2023\\Capstone\\RVAC website Git\\rvac-overhaul\\client\\class.html')
SCRIPT_PATH=os.path.abspath('scripts.js')
toFind=''
newClassName=''
newClassStartTime=[]
newClassPrice=0.00
tempCounter=0
console='add'

def findInFile(idToFind,widget):
    html=open(CLASS_PATH)
    soup=bs(html,'html.parser')
    location=soup.find(widget, {"id":idToFind})
    print(location)
    return location

def replaceTableEnd():
    pass

def addAclass(newClassName,newClassDateTime,newClassPrice):
    with open(CLASS_PATH, "w", encoding = 'utf-8') as file:    
        tableEnd=(findInFile('endOfTable','tr'))
        newEntry=(bs(('<tr id=' + newClassName +'><td>' + newClassName+'</td><td>' + str(newClassDateTime)+'</td><td> $' + str(newClassPrice)+'</td><td> <button id=' + newClassName+' class = "itemButton">Reseve Now</button></td></tr>'),'html.parser'))
        print(tableEnd)
        print(newEntry)
        file.write(str(tableEnd.insert_before(newEntry)))

def removeAclass(console):
    toRemove=findInFile('deleteThis','tr')


###print('Do you want to add or remove a class')
###console=input()
if(console=='add'):
    '''print('What is the name of this class?')
    newClassName=input()
    print('When will this class start? YYYY/MM/DD HH:MM')
    format = "%Y/%m/%d %H:%M" 
    newClassStartTime=datetime.strptime(input(),format)
    print('How many hours will this class last?')
    lenght=float(input())
    newClassDateTime=newClassStartTime+timedelta(hours=lenght)
    print('What is the price of this class?')
    newClassPrice=float(input())
    '''
    date_string_2 = "2021/09/01 14:30:00"
    format_2 = "%Y/%m/%d %H:%M:%S"
    date_2 = datetime.strptime(date_string_2, format_2)
    addAclass('newClassName',date_2,50.00)

elif(console=='remove'):
    removeAclass(console)

else:
    print('error')
