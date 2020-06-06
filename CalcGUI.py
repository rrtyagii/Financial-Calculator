import PySimpleGUI as sg

sg.theme("DarkAmber")

layout =[ [sg.Text("HPBT-II-0", size=(50,1), justification='right', background_color="#272533", text_color='white') ],
          [sg.Text('0.0000', size = (18,1), justification='right', background_color='black', text_color='red', font=('digital-7 (mono).ttf',8), relief='sunken', key ='_DISPLAY_')]
          [sg.Button("C"), sg.Button("CE")]
]

window: object = sg.Window('Hp-TI180-II', layout=layout, background_color="#272533", size=(580, 660), return_keyboard_events=True)

while True:
    event, values = window.read()
    print(event)
    if event is None:
        break
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        #number_click(event)
        pass
    if event in ['Escape:27','C','CE']:
        #clear_click()
        #update_display(0.0)
        pass