import PySimpleGUI as sg

sg.theme('Black')
player1Points = []
player2Points = []
player1MatchPoints = []
player2MatchPoints = []
round = 1
player1Turn = True
pointFont = ("Arial", 60)
playerFont = ("Arial", 30)

def HighLightPlayer1():
    global player1Turn
    player1Turn = True
    window['-TURN-'].update("Player 1 points")
    window['-POINTSLEFT1-'].update(background_color = 'white', text_color = 'black')
    window['-POINTSLEFT2-'].update(background_color = sg.theme_background_color(), text_color = sg.theme_text_color())

def HighLightPlayer2():
    global player1Turn
    player1Turn = False
    window['-TURN-'].update("Player 2 points")
    window['-POINTSLEFT2-'].update(background_color = 'white', text_color = 'black')
    window['-POINTSLEFT1-'].update(background_color = sg.theme_background_color(), text_color = sg.theme_text_color())

col1 = [[sg.Text("Player 1")],
        [sg.InputText(size=(10,1), font=playerFont, key = '-PLAYER1NAME-'), sg.Text("0", font=playerFont, key = '-PLAYER1LEGWIN-')],
        [sg.Text("501", key = '-POINTSLEFT1-', font = pointFont, enable_events=True, background_color="white", text_color="black")],
        [sg.Text("AVG:"),sg.Text("0", key = '-P1AVG-')],
        [sg.Text("Match AVG:"), sg.Text("0", key = '-P1MATCHAVG-')]
        ]

col2 = [[sg.Text("Player 2")],
        [ sg.InputText(size=(10,1), font = playerFont, key = '-PLAYER2NAME-'), sg.Text("0", font=playerFont, key = '-PLAYER2LEGWIN-') ],
        [sg.Text("501",key = '-POINTSLEFT2-', font = pointFont, enable_events= True)],
        [sg.Text("AVG:"), sg.Text("0", key = '-P2AVG-')],
        [sg.Text("Match AVG:"), sg.Text("0", key = '-P2MATCHAVG-')]
        ]

col3 = [[sg.Text("Player 1 points", key = '-TURN-')],
        [sg.InputText(size=(15,1), key = '-POINTS-', font = playerFont),sg.Button('Subtract', visible= True, bind_return_key=True)],
        [sg.Button('Back', visible = True)]
        ]

layout = [[sg.Column(col1,justification="c", pad=(100,50)), sg.Column(col2, justification = "c", pad= (100,50))],
          [sg.Column(col3, justification="c")]]

window = sg.Window("Darts Counter", layout, resizable=True)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Subtract':
        try:
            points = int(window['-POINTS-'].get())
        except ValueError:
            continue
        if player1Turn:
            player1Points.append(points)
            player1MatchPoints.append(points)
            updatedPoints = int(window['-POINTSLEFT1-'].get()) - points
            if updatedPoints == 0:
                playerName = window['-PLAYER1NAME-'].get()
                answer = sg.popup_yes_no(playerName + " won?", title = "Winner?")
                print(answer)
                if answer == "Yes":
                    round = round + 1
                    p1legwins = int(window['-PLAYER1LEGWIN-'].get())
                    window['-PLAYER1LEGWIN-'].update(str(p1legwins + 1))
                    window['-POINTSLEFT1-'].update("501")
                    window['-POINTSLEFT2-'].update("501")
                    window['-POINTS-'].update("")
                    player1Points = []
                    player2Points = []
                    if round % 2 != 0:
                        HighLightPlayer1()
                        continue
                    else:
                        HighLightPlayer2()
                        continue
                    
            window['-POINTSLEFT1-'].update(str(updatedPoints))
            window['-POINTS-'].update("")
            legAvgP1 = (sum(player1Points))/(len(player1Points)*3) * 3
            window['-P1AVG-'].update(str(legAvgP1))
            matchAvgP2 = (sum(player2MatchPoints))/(len(player2MatchPoints)*3) * 3
            window['-P2MATCHAVG-'].update(str(matchAvgP2))
            HighLightPlayer2()
        else:
            player2Points.append(points)
            player2MatchPoints.append(points)
            updatedPoints = int(window['-POINTSLEFT2-'].get()) - points
            if updatedPoints == 0:
                playerName = window['-PLAYER2NAME-'].get()
                answer = sg.popup_yes_no(playerName + " won?", title = "Winner?")
                print(answer)
                if answer == "Yes":
                    round = round + 1
                    p2legwins = int(window['-PLAYER2LEGWIN-'].get())
                    window['-PLAYER2LEGWIN-'].update(str(p2legwins + 1))
                    window['-POINTSLEFT1-'].update("501")
                    window['-POINTSLEFT2-'].update("501")
                    window['-POINTS-'].update("")
                    player1Points = []
                    player2Points = []
                    if round % 2 != 0:
                        HighLightPlayer1()
                        continue
                    else:
                        HighLightPlayer2()
                        continue
                else:
                    HighLightPlayer1()
                    continue
            window['-POINTSLEFT2-'].update(str(updatedPoints))
            window['-POINTS-'].update("")
            legAvgP2 = (sum(player2Points))/(len(player2Points)*3) * 3
            window['-P2AVG-'].update(str(legAvgP2))
            matchAvgP2 = (sum(player2MatchPoints))/(len(player2MatchPoints)*3) * 3
            window['-P2MATCHAVG-'].update(str(matchAvgP2))
            HighLightPlayer1()
    
    if event == 'Back':
        if player1Turn == True:
            if len(player2Points) == 0:
                continue
            HighLightPlayer2()
            lastPoint = player2Points[-1]
            player2Points.pop()
            backUpPoints = int(window['-POINTSLEFT2-'].get()) + lastPoint
            window['-POINTSLEFT2-'].update(str(backUpPoints))
            window['-POINTS-'].update(str(lastPoint))
        else:
            if len(player1Points) == 0:
                continue
            HighLightPlayer1()
            lastPoint = player1Points[-1]
            player1Points.pop()
            backUpPoints = int(window['-POINTSLEFT1-'].get()) + lastPoint
            window['-POINTSLEFT1-'].update(str(backUpPoints))
            window['-POINTS-'].update(str(lastPoint))

            
            
        
