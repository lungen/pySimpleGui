import PySimpleGUI as sg

frame1 = [[sg.Radio(', (Comma)',1, key='-R1-COMMA-', default=True)],
          [sg.Radio('| (Pipe)', 1, key='-R1-PIPE-')],
          [sg.Radio('; (Semi-Colon)', 1, key='-R1-SEMI-', )],
          [sg.Radio('  (Tab)', 1, key='-R1-TAB-')]]

col1 = [[sg.Button('Process Files')],
        [sg.Button('Exit')]]


layout = [  [sg.Input(key='-IN-',size=(20,1)), sg.Text('Uploader', size=(40,1)), sg.Button('Select All'), sg.Button('Refresh List'), sg.Checkbox('Debug', key='-DEBUG-')],
            [sg.Output(size=(100,10), key='-MULTI-LINE-')],
            [sg.Frame('Delimeter', frame1), sg.Column(col1)]  ]

window = sg.Window('Sandbox CSV Uploader', layout)

while True:             # Event Loop
    event, values = window.read()
    # print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Select All':
        print('Select All chosen')
    elif event == 'Refresh List':
        print('Refesh List chosen')
    elif event == 'Process Files':
        print('Process Files chosen')
        print('values = ', values)
window.close()
