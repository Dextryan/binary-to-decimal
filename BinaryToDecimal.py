import PySimpleGUI as sg
import string

def is_binary(input):
    for i in input:
        if i in string.printable[2::]:
            return False
    return True
def translate_bin(bin):
    translated_bin = 0
    len_bin = len(bin)
    for i in bin:
        translated_bin += int(i)*(2**(len_bin-1)) 
        len_bin -= 1
    return translated_bin
def make_window():
    layout = [ [sg.Text("Insira número binário a ser convertido:",justification="center")],
                [sg.T("Binário:"), sg.In(justification="center", k="--IN--", p=((8,0),(0)), size=24)],
                [sg.T("Decimal:"), sg.In(justification="center", readonly=True, k="--OUT--", size=24)],
                [sg.B("Converter", bind_return_key=True), sg.B("Cancelar")] ]
    return sg.Window("Configurações", layout, finalize=True, element_justification="c") 
def make_popup():
    layout = [  [sg.Text("O valor inserido não é binário")],
                [sg.Ok()]]
    return sg.Window("Erro", layout, element_justification="c", keep_on_top=True, modal=True)
def Main():
    sg.set_options(font=("Verdana", 12))
    sg.theme("light grey 1")
    win = make_window()
    while(True):
        event, values = win.read()
        if event == sg.WIN_CLOSED or event == "Cancelar":
            win.close()
            break
        elif event == "Converter":
            if is_binary(values["--IN--"]):
                    win["--OUT--"].update(translate_bin(values["--IN--"]))
            else:
                popup = make_popup().read(close=True)
                win["--IN--"].update("")
Main()