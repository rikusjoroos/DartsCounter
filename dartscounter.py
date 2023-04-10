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

menu_def = [['File',['New Game']]]

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
        [sg.InputText(size=(15,1), key = '-POINTS-', font = playerFont),sg.Button('Subtract', visible= True, bind_return_key=True), sg.Button("Remains", visible = True)],
        [sg.Button('Back', visible = True)]
        ]

layout = [[sg.Menu(menu_def, tearoff=False,key='-MENU BAR-')],
          [sg.Column(col1,justification="c", pad=(100,50)), sg.Column(col2, justification = "c", pad= (100,50))],
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

        if points < 0 or points > 180:
            continue
        if player1Turn:
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
                    player1Points.append(points)
                    player1MatchPoints.append(points)
                    legAvgP1 = (sum(player1Points))/(len(player1Points)*3) * 3
                    window['-P1AVG-'].update(str(legAvgP1))
                    matchAvgP1 = (sum(player1MatchPoints))/(len(player1MatchPoints)*3) * 3
                    window['-P1MATCHAVG-'].update(str(matchAvgP1))
                    player1Points = []
                    player2Points = []
                    if round % 2 != 0:
                        HighLightPlayer1()
                        continue
                    else:
                        HighLightPlayer2()
                        continue
                else:
                    window['-POINTS-'].update("")
                    player1Points.append(0)
                    player1MatchPoints.append(0)
                    legAvgP1 = (sum(player1Points))/(len(player1Points)*3) * 3
                    window['-P1AVG-'].update(str(legAvgP1))
                    matchAvgP1 = (sum(player1MatchPoints))/(len(player1MatchPoints)*3) * 3
                    window['-P1MATCHAVG-'].update(str(matchAvgP1))
                    HighLightPlayer2()
                    continue
            player1Points.append(points)
            player1MatchPoints.append(points)
            window['-POINTSLEFT1-'].update(str(updatedPoints))
            window['-POINTS-'].update("")
            legAvgP1 = (sum(player1Points))/(len(player1Points)*3) * 3
            window['-P1AVG-'].update(str(legAvgP1))
            matchAvgP1 = (sum(player1MatchPoints))/(len(player1MatchPoints)*3) * 3
            window['-P1MATCHAVG-'].update(str(matchAvgP1))
            HighLightPlayer2()
        else:
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
                    player2Points.append(points)
                    player2MatchPoints.append(points)
                    legAvgP2 = (sum(player2Points))/(len(player2Points)*3) * 3
                    window['-P2AVG-'].update(str(legAvgP2))
                    matchAvgP2 = (sum(player2MatchPoints))/(len(player2MatchPoints)*3) * 3
                    window['-P2MATCHAVG-'].update(str(matchAvgP2))
                    player1Points = []
                    player2Points = []
                    if round % 2 != 0:
                        HighLightPlayer1()
                        continue
                    else:
                        HighLightPlayer2()
                        continue
                else:
                    player2Points.append(0)
                    player2MatchPoints.append(0)
                    window['-POINTS-'].update("")
                    legAvgP2 = (sum(player2Points))/(len(player2Points)*3) * 3
                    window['-P2AVG-'].update(str(legAvgP2))
                    matchAvgP2 = (sum(player2MatchPoints))/(len(player2MatchPoints)*3) * 3
                    window['-P2MATCHAVG-'].update(str(matchAvgP2))
                    HighLightPlayer1()
                    continue
            player2Points.append(points)
            player2MatchPoints.append(points)
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
            player2MatchPoints.pop()
            backUpPoints = int(window['-POINTSLEFT2-'].get()) + lastPoint
            window['-POINTSLEFT2-'].update(str(backUpPoints))
            window['-POINTS-'].update(str(lastPoint))
        else:
            if len(player1Points) == 0:
                continue
            HighLightPlayer1()
            lastPoint = player1Points[-1]
            player1Points.pop()
            player1MatchPoints.pop()
            backUpPoints = int(window['-POINTSLEFT1-'].get()) + lastPoint
            window['-POINTSLEFT1-'].update(str(backUpPoints))
            window['-POINTS-'].update(str(lastPoint))

    if event == "Remains":
        try:
            remainingpoints = int(window['-POINTS-'].get())
        except ValueError:
            continue
        if remainingpoints < 0:
            continue
        if player1Turn == True:
            if remainingpoints == 0:
                playerName = window['-PLAYER1NAME-'].get()
                answer = sg.popup_yes_no(playerName + " won?", title = "Winner?")
                p1CurrentPoints = int(window['-POINTSLEFT1-'].get())
                scoredPoints = p1CurrentPoints - remainingpoints
                if answer == "Yes":
                    round = round + 1
                    p1legwins = int(window['-PLAYER1LEGWIN-'].get())
                    window['-PLAYER1LEGWIN-'].update(str(p1legwins + 1))
                    window['-POINTSLEFT1-'].update("501")
                    window['-POINTSLEFT2-'].update("501")
                    window['-POINTS-'].update("")
                    player1Points.append(scoredPoints)
                    player1MatchPoints.append(scoredPoints)
                    legAvgP1 = (sum(player1Points))/(len(player1Points)*3) * 3
                    window['-P1AVG-'].update(str(legAvgP1))
                    matchAvgP2 = (sum(player1MatchPoints))/(len(player1MatchPoints)*3) * 3
                    window['-P1MATCHAVG-'].update(str(matchAvgP1))
                    player1Points = []
                    player2Points = []
                    if round % 2 != 0:
                        HighLightPlayer1()
                        continue
                    else:
                        HighLightPlayer2()
                        continue
                else:
                    HighLightPlayer2()
                    window['-POINTS-'].update("")
                    player1MatchPoints.append(0)
                    player1Points.append(0)
                    legAvgP1 = (sum(player1Points))/(len(player1Points)*3) * 3
                    window['-P1AVG-'].update(str(legAvgP1))
                    matchAvgP2 = (sum(player1MatchPoints))/(len(player1MatchPoints)*3) * 3
                    window['-P1MATCHAVG-'].update(str(matchAvgP1))
                    continue
            player1Points.append(scoredPoints)
            player1MatchPoints.append(scoredPoints)
            window['-POINTSLEFT1-'].update(str(remainingpoints))
            legAvgP1 = (sum(player1Points))/(len(player1Points)*3) * 3
            window['-P1AVG-'].update(str(legAvgP1))
            matchAvgP1 = (sum(player1MatchPoints))/(len(player1MatchPoints)*3) * 3
            window['-P1MATCHAVG-'].update(str(matchAvgP1))
            window['-POINTS-'].update("")
            HighLightPlayer2()
        else:
            if remainingpoints == 0:
                playerName = window['-PLAYER2NAME-'].get()
                answer = sg.popup_yes_no(playerName + " won?", title = "Winner?")
                p2CurrentPoints = int(window['-POINTSLEFT2-'].get())
                scoredPoints = p2CurrentPoints - remainingpoints
                if answer == "Yes":
                    round = round + 1
                    p2legwins = int(window['-PLAYER2LEGWIN-'].get())
                    window['-PLAYER2LEGWIN-'].update(str(p2legwins + 1))
                    window['-POINTSLEFT1-'].update("501")
                    window['-POINTSLEFT2-'].update("501")
                    window['-POINTS-'].update("")
                    player2Points.append(scoredPoints)
                    player2MatchPoints.append(scoredPoints)
                    legAvgP2 = (sum(player2Points))/(len(player2Points)*3) * 3
                    window['-P2AVG-'].update(str(legAvgP2))
                    matchAvgP2 = (sum(player2MatchPoints))/(len(player2MatchPoints)*3) * 3
                    window['-P2MATCHAVG-'].update(str(matchAvgP2))
                    player1Points = []
                    player2Points = []
                    if round % 2 != 0:
                        HighLightPlayer1()
                        continue
                    else:
                        HighLightPlayer2()
                        continue
                else:
                    window['-POINTS-'].update("")
                    HighLightPlayer1()
                    player2Points.append(0)
                    player2MatchPoints.append(0)
                    legAvgP2 = (sum(player2Points))/(len(player2Points)*3) * 3
                    window['-P2AVG-'].update(str(legAvgP2))
                    matchAvgP2 = (sum(player2MatchPoints))/(len(player2MatchPoints)*3) * 3
                    window['-P2MATCHAVG-'].update(str(matchAvgP2))
                    continue

            player2Points.append(scoredPoints)
            player2MatchPoints.append(scoredPoints)
            window['-POINTSLEFT2-'].update(str(remainingpoints))
            legAvgP2 = (sum(player2Points))/(len(player2Points)*3) * 3
            window['-P2AVG-'].update(str(legAvgP2))
            matchAvgP2 = (sum(player2MatchPoints))/(len(player2MatchPoints)*3) * 3
            window['-P2MATCHAVG-'].update(str(matchAvgP2))
            window['-POINTS-'].update("")
            HighLightPlayer1()

    if event == "New Game":
        player1Points = []
        player2Points = []
        player1MatchPoints = []
        player2MatchPoints = []
        round = 1
        player1Turn = True
        window['-PLAYER2LEGWIN-'].update("0")
        window['-PLAYER1LEGWIN-'].update("0")
        window['-POINTSLEFT1-'].update("501")
        window['-POINTSLEFT2-'].update("501")
        window['-POINTS-'].update("")
        window['-P1AVG-'].update("0")
        window['-P1MATCHAVG-'].update("0")
        window['-P2AVG-'].update("0")
        window['-P2MATCHAVG-'].update("0")
        HighLightPlayer1()
            





            
            
        
