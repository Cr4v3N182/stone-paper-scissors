import PySimpleGUI as sg


import functions

sg.theme("DarkAmber")

score = []

label = sg.Text("Choose stone, paper or scissors, and try to gues what's in a box")
stone_button = sg.Button("Stone", key="stone")
paper_button = sg.Button("Paper", key="paper")
scissors_button = sg.Button("Scissors", key="scissors")
show_score_button = sg.Button("Show score", key="score")
exit_button = sg.Button("Exit", key="exit")
result = sg.Text("", key="output")
check_win_lose = sg.Text("", key="check")

layout = [[label], [[stone_button, paper_button, scissors_button]],
          [show_score_button, result], [exit_button]]

window = sg.Window("Stone-Paper-Scissor-APP", layout=layout, size= (400, 200), element_justification='c')
while True:
    event, value = window.read()
    match event:
        case "stone":
            if "stone" == functions.draw_function():
                score.append(value)
                sg.popup("You Win")
            else:
                sg.popup("You lose")
        case "paper":
            if "paper" == functions.draw_function():
                score.append(value)
                sg.popup("You Win")
            else:
                sg.popup("You lose")
        case "scissors":
            if "scissors" == functions.draw_function():
                score.append(value)
                sg.popup("You Win")
            else:
                sg.popup("You lose")
        case "score":
            window["output"].update(value=f'Your score: {len(score)}')
        case "exit":
            break
        case sg.WIN_CLOSED:
            break



window.close()
