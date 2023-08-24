import PySimpleGUI as sg

sg.theme("DarkAmber")

label = sg.Text("Choose stone, paper or scissors")
stone_button = sg.Button("Stone", key="stone", )
paper_button = sg.Button("Pape", key="paper")
scissors_button = sg.Button("Scissors", key="scissors")

layout = [[label], [[stone_button, paper_button, scissors_button]]]

window = sg.Window("Stone-Paper-Scissor-APP", layout=layout, size= (300, 200))

window.read()

window.close()
