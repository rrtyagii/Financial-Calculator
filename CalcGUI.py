import PySimpleGUI as sg
import Calculator as calc

bw = {'size':(5,1), 'font': ('Franklin Gothic Book', 24), 'button_color':('black',"#F8F8F8") }
bt = {'size':(5,1), 'font': ('Franklin Gothic Book', 24), 'button_color':('black',"#F1EABC") }
bo = {'size':(10,1), 'font':('Franklin Gothic Book', 24), 'button_color':('black',"#ECA527"), 'focus':True }
#can ={'size':(3,1), 'font': ('Franklin Gothic Book', 24), 'button_color':('black',"#F1EABC") }

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('RT_100_X1', justification='right', size=(50,1), background_color="#272533", text_color='white' )],
            [ sg.Text('0.000', size=(100,3), justification='right', font=('digital-7 (mono).ttf',8), text_color='red', relief='sunken', key="DISPLAY")],
            [ sg.Button("C", **bt),sg.Button("CE",**bt), sg.Button('%',**bt), sg.Button("/",**bt) ,sg.Button("PMT",**bt) ],
            [ sg.Button("7", **bw), sg.Button("8", **bw),  sg.Button("9", **bw), sg.Button("*",**bt), sg.Button("FV",**bt) ],
            [ sg.Button("4", **bw), sg.Button("5", **bw),  sg.Button("6", **bw), sg.Button("-",**bt), sg.Button("PV",**bt)  ],
            [ sg.Button("1", **bw), sg.Button("2", **bw),  sg.Button("3", **bw), sg.Button("+",**bt), sg.Button("I",**bt)  ],
            [ sg.Button('0', **bw), sg.Button('.', **bw), sg.Button('=',**bo),sg.Button("N",**bt) ,sg.Cancel(size=(3,1), font=("Franklin Gothic Book",10) )]
        ]

# Create the Window
window = sg.Window('Hp-TI180-II', layout=layout, background_color="#272533", size=(550, 415), return_keyboard_events=True)
# Event Loop to process "events" and get the "values" of the inputs


var: dict = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}


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


def clear_click():
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False


def operator_click(event:str):
    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']
    clear_click()


def calculate_click():
    global var
    var['y_val'] = format_number()
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']) )
        update_display(var['result'])
        clear_click()
    except:
        update_display('ERROR! DIV/0')
        clear_click()



while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED or event == 'Cancel' or event is None:
        break
#    print('You entered ', values[0])
    if event in ['0','1','2','3','4','5','6','7','8','9'] :
        click_number(event)
    if event in ['Escape:27','C','CE']: # 'Escape:27 for keyboard control
        clear_click()
        update_display(0.0)
        var['result'] = 0.0
    if event in ['+','-','*','/']:
        operator_click(event)
    if event == '=': #or event is sg.:
        calculate_click()
    if event == '.':
        var['decimal'] = True
    if event == '%':
        update_display(var['result'] / 100.0)


window.close()