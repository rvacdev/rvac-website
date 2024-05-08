import PySimpleGUI as sg
import os

#change url locations as needed
CLASS_PATH=os.path.relpath('client\\templates\\class.html')
SCRIPT_PATH=os.path.relpath('client\\static\\JS\\scripts.js')


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
        reader.close()
    with open(SCRIPT_PATH,'w') as writer:
        for line in lines:
            line=line.replace('// END OF PRODUCT LIST',
                              '{ id: \''+toAddList[0]+
                              '\', name: \''+toAddList[0]+
                              '\', price: \''+str(toAddList[2])+
                              '\', quantity: 0 },\n\t\t// END OF PRODUCT LIST')
            writer.write(str(line))
        writer.close()

def addAclass(toAddList):  
    with open(CLASS_PATH,'r') as reader:
        lines=reader.readlines()
        reader.close()
    with open(CLASS_PATH,'w') as writer:
        for line in lines:
            if('<tr id="endOfEventTable"></tr>'in line):
                writer.write(
                    '\t\t\t\t\t<tr id=\"'+ toAddList[0] +'\">\n'+
                    '\t\t\t\t\t\t <td>'+ toAddList[0] +'</td>\n'+
                    '\t\t\t\t\t\t <td>'+ toAddList[1] +'</td>\n'+
                    '\t\t\t\t\t\t <td>$'+ toAddList[2] +'</td>\n'+
                    '\t\t\t\t\t\t <td><button id=\"'+ toAddList[0] +'\" class = \"itemButton\">Reseve Now</button></td>\n'+
                    '\t\t\t\t\t</tr>\n'+
                    '\t\t\t\t\t<tr id="endOfEventTable"></tr>\n'
                )
            else:
                writer.write(str(line))
        writer.close()
    addToJavaScript(toAddList)

def removeAscript(toRemove):
    with open(SCRIPT_PATH,'r') as reader:
        lines=reader.readlines()
        reader.close()
    with open(SCRIPT_PATH,'w') as writer:
        for line in lines:
            if('{ id: '+toRemove+', name:' in line):
                pass
            else:
                writer.write(str(line))
        writer.close()

def removeAclass(toRemove):
    with open(CLASS_PATH,'r') as reader:
        lines=reader.readlines()
        reader.close()
    with open(CLASS_PATH,'w') as writer:
        x=0
        for line in lines:
            if(toRemove not in line and not(0<x<6)):
                writer.write(str(line))
            else:
                x=x+1
        writer.close()
    removeAscript(toRemove)


layout = [[sg.Text('Would you like to add or remove an event')],
          [sg.Button('Add'), sg.Button('Remove')]]

# Create the Window
window = sg.Window('Add or Remove an event', layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the Cancel button
    if event == "Add" or event == "Remove" or event == sg.WIN_CLOSED:
        break

console=event

window.close()

if(console=='Add'):
    addLayout = [[sg.Text("What is the name of this event?"), sg.InputText()],
            [sg.Text("When will this class be? ex. Mondays at 1:00 PM - 3:00 PM")], 
            [sg.Text("Or December 8th 2024 11:00 AM - 1:30 PM"),sg.InputText()],
            [sg.Text("What is the price of this event?  $"), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the window
    addWindow = sg.Window("Add a event", addLayout)

    # Create an event loop
    while True:
        event, values = addWindow.read()
        # End program if user closes window or
        # presses the Cancel button
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        
        if event=='Ok':
            toAddList=values
            addAclass(toAddList)
            break
    
    
    addWindow.close()

elif(console=='Remove'):
    removeLayout = [[sg.Text("What is the name of the event you wish to remove?"), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the window
    removeWindow = sg.Window("Remove an event", removeLayout)

    # Create an event loop
    while True:
        event, values = removeWindow.read()
        # End program if user closes window or
        # presses the Cancel button
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        
        if event=='Ok':
            toRemove='<tr id=\"'+values[0]+'\">'
            removeAclass(toRemove)
            break
    
    
    removeWindow.close()
    
