from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
import os
import re

#change url locations as needed
CLASS_PATH=os.path.relpath('client\\class.html')
SCRIPT_PATH=os.path.relpath('client\\scripts.js')
toFind=''
newClassName=''
newClassStartTime=[]
newClassPrice=0.00
tempCounter=0
console='remove'

def findInFile(idToFind,widget,soup):
    location=soup.find(widget, {"id":idToFind})
    return location


def makeTableEntry(tableText,soup):
    tdTag=soup.new_tag('td')
    tdTag.string=str(tableText)
    return tdTag

def addButton(buttonID,soup):
    tdTag=soup.new_tag('td')
    button=soup.new_tag('button',id=toAddList[0],**{'class':"itemButton"})
    button.string=("Reseve Now")
    tdTag.append(button)
    return tdTag

def addToJavaScript(toAddList):
    with open(SCRIPT_PATH,'r') as reader:
        lines=reader.readlines()
    with open(SCRIPT_PATH,'w') as writer:
        for line in lines:
            line=line.replace('// END OF PRODUCT LIST','{ id: \''+toAddList[0]+'\', name: \''+toAddList[0]+'\', price: \''+str(toAddList[2][1])+'\' },\n// END OF PRODUCT LIST')
            writer.write(str(line))

def addAclass(toAddList):  
    html=open(CLASS_PATH)
    soup=bs(html,'html.parser')
    tableEnd=(findInFile('endOfTable','tr',soup))
    newTable=soup.new_tag('tr',id=toAddList[0])
    for item in toAddList:
        newEntry=makeTableEntry(item,soup)
        newTable.append(newEntry)
    newTable.append(addButton(toAddList[0],soup))
    tableEnd.insert_before(newTable)
    with open(CLASS_PATH, "w", encoding='utf-8') as file:
        file.write(str(soup))
    html.close()
    addToJavaScript(toAddList)

def removeAscript(toRemove):
    with open(SCRIPT_PATH,'r') as reader:
        lines=reader.readlines()
    with open(SCRIPT_PATH,'w') as writer:
        for line in lines:
            if(line.strip('\n\t')!='<tr id=\"'+toRemove+'\">'):
                writer.write(str(line))

def removeAclass(toRemove):
    with open(CLASS_PATH,'r') as reader:
        lines=reader.readlines()
    with open(CLASS_PATH,'w') as writer:
        x=0
        for line in lines:
            if(line.strip('\n\t')!='<tr id=\"'+toRemove+'\">'and (0<x or x<6)):
                writer.write(str(line))
            else:
                x=x+1


#print('Do you want to add or remove a class')
#console=input()
if(console=='add'):
    print('What is the name of this class?')
    newClassName=input()
    print('When will this class start? YYYY/MM/DD HH:MM')
    format = "%Y/%m/%d %H:%M" 
    newClassStartTime=datetime.strptime(input(),format)
    print('How many hours will this class last?')
    lenght=float(input())
    newClassDateTime=newClassStartTime+timedelta(hours=lenght)
    print('What is the price of this class?')
    newClassPrice=float(input())
    toAddList=[newClassName,newClassDateTime,['$',50.00]]
    addAclass(toAddList)

elif(console=='remove'):
    print('what class do you want to remove')
    toRemove=input()
    removeAclass(toRemove)

else:
    print('error')
