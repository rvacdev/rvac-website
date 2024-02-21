import PySimpleGUI as sg

layout = [[sg.Text('Would you like to add or remove a class')],
          [sg.Button('Add'), sg.Button('Remove')]]

# Create the Window
window = sg.Window('Add or Remove class', layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the Cancel button
    if event == "Add" or event == "Remove" or event == sg.WIN_CLOSED:
        break

console=event

window.close()

if(console=='add'):
    addLayout = [[sg.Text("What is the name of this class?"), sg.InputText()],
            [sg.Text("When will this class be? ex. Mondays at 1:00 PM - 3:00 PM")], 
            [sg.Text("Or December 8th 2024 11:00 AM - 1:30 PM"),sg.InputText()],
            [sg.Text("What is the price of this class?  $"), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the window
    addWindow = sg.Window("Add a class", addLayout)

    # Create an event loop
    while True:
        event, values = addWindow.read()
        # End program if user closes window or
        # presses the Cancel button
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        
        if event=='Ok':
            toAddList=values
            break

    addWindow.close()


elif(console=='remove'):
    removeLayout = [[sg.Text("What is the name of the class you wish to remove?"), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the window
    removeWindow = sg.Window("Remove a class", removeLayout)

    # Create an event loop
    while True:
        event, values = removeWindow.read()
        # End program if user closes window or
        # presses the Cancel button
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        
        if event=='Ok':
            toRemove=values[0]
            break
        
    removeWindow.close()
