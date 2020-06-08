import PySimpleGUI as sg
import Calculator as calc

bw = {'size':(5,1), 'font': ('Franklin Gothic Book', 24), 'button_color':('black',"#F8F8F8") }
bt = {'size':(5,1), 'font': ('Franklin Gothic Book', 24), 'button_color':('black',"#F1EABC") }
bo = {'size':(10,1), 'font':('Franklin Gothic Book', 24), 'button_color':('black',"#ECA527"), 'focus':True }
#can ={'size':(3,1), 'font': ('Franklin Gothic Book', 24), 'button_color':('black',"#F1EABC") }

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('RT_100_X1', justification='left', size=(50,1), background_color="#272533", text_color='white' )],
            [ sg.Text('0.000', size=(18,1), justification='right', font=('digital-7 (mono).ttf',8), text_color='red', relief='sunken', key="DISPLAY")],
            [ sg.Button("C", **bt),sg.Button("CE",**bt), sg.Button('%',**bt), sg.Button("/",**bt) ,sg.Button("PMT",**bt) ],
            [ sg.Button("7", **bw), sg.Button("8", **bw),  sg.Button("9", **bw), sg.Button("*",**bt), sg.Button("FV",**bt) ],
            [ sg.Button("4", **bw), sg.Button("5", **bw),  sg.Button("6", **bw), sg.Button("-",**bt), sg.Button("PV",**bt)  ],
            [ sg.Button("1", **bw), sg.Button("2", **bw),  sg.Button("3", **bw), sg.Button("+",**bt), sg.Button("I",**bt)  ],
            [ sg.Button('0', **bw), sg.Button('.', **bw), sg.Button('=',**bo),sg.Button("N",**bt) ,sg.Cancel(size=(3,1), font=("Franklin Gothic Book",10) )]
        ]

# Create the Window
window = sg.Window('Hp-TI180-II', layout=layout, background_color="#272533", size=(550, 600), return_keyboard_events=True)
# Event Loop to process "events" and get the "values" of the inputs

def format_number() -> float:
    return float(''.join(var['front']) + '.' + ''.join(var['back'] ))

def update_display(display_value: str):
    try:
        window['DISPLAY'].update(value='{:,.4f}'.format(display_value))
    except:
        window['DISPLAY'].update(value = display_value)


def click_number(event:str):
    """Number button button click event"""
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

    if event in ['0','1','2','3','4','5','6','7','8','9']:
        click_number(event)


window.close()