import PySimpleGUI as sg

WIDTH = 400
LOC1 = (50, 0)
LOC2 = (LOC1[0] + WIDTH, LOC1[1])
LOC3 = (LOC2[0] + WIDTH, LOC1[1])

layout1 = [
    [sg.Text("My Window")],
    [sg.Input(k="-IN-"), sg.Text(size=(12, 1), k="-OUT-")],
    [
        sg.CB("Check 1", k="-CB1-", enable_events=True),
        sg.CB("Check 2", k="-CB2-", enable_events=True),
        sg.CB("Mirror on Window 2", enable_events=True, k="-CB3-"),
    ],
    [sg.Button("Go"), sg.B("Dummy"), sg.Button("Exit")],
]

window1 = sg.Window("Window 1 Title", layout1, finalize=True, location=LOC1)

layout2 = [
    [sg.Text("My Window")],
    [sg.Input(k="-IN-"), sg.Text(size=(12, 1), k="-OUT-")],
    [sg.CB("Check 1", k="-CB1-"), sg.CB("Check 2", k="-CB2-")],
    [sg.Button("Go"), sg.B("Popup"), sg.Button("Exit")],
]

window2 = sg.Window("Window 2 Title", layout2, finalize=True, location=LOC2)

while True:  # Event Loop
    window, event, values = sg.read_all_windows()
    if window is None and event != sg.TIMEOUT_EVENT:
        print("exiting because no windows are left")
        break
    print(window.Title, event, values) if window is not None else None
    if event == sg.WIN_CLOSED or event == "Exit":
        window.close()
    if event == "Go":
        window["-OUT-"].update(values["-IN-"])
        try:  # try to update the other window
            if window == window1:
                window2["-OUT-"].update("The other window")
            else:
                window1["-OUT-"].update("The other window")
        except:
            pass
    if event == "Dummy":
        sg.popup_non_blocking("Non-blocking popup")
    if event == "Popup":
        sg.popup("plain popup")

    try:
        if window == window1 and values["-CB3-"]:
            window2["-CB1-"].update(values["-CB1-"])
            window2["-CB2-"].update(values["-CB2-"])
    except:
        pass
