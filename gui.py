import PySimpleGUI as sg

dictionary_of_items = {1 : "stone", 2 : "paper", 3 : "scissors"}

sg.theme("DarkAmber")

label = sg.Text("Choose stone, paper or scissors")
stone_button = sg.Button("Stone", key="stone")
paper_button = sg.Button("Paper", key="paper")
scissors_button = sg.Button("Scissors", key="scissors")

layout = [[label], [[stone_button, paper_button, scissors_button]]]

window = sg.Window("Stone-Paper-Scissor-APP", layout=layout, size= (400, 200), element_justification='c')
while True:
    window.read()

window.close()
