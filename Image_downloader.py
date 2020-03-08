from subprocess import run
from os import mkdir, path
from pathlib import Path

try:
    import PySimpleGUI as sg
except ModuleNotFoundError:
    run(['pip', 'install', 'PySimpleGUI'])
    import PySimpleGUI as sg

this_file = path.abspath(path.dirname(__file__))
source = this_file / Path(r'bing')
parent_dir = this_file / Path(r'Completed Queries')
try:
    mkdir(parent_dir)
except FileExistsError:
    pass

layout = [
    [sg.Text('Bulk Bing Image Downloader', font=('Tebuchet', 14, 'bold'))],
    [sg.Text('Query:\t\t', font=('Trebuchet', 12, 'bold')), sg.Input('', key='_query_')],
    [sg.Text('# of Images:\t', font=('Trebuchet', 12, 'bold')), sg.Input('', key='_quantity_')],
    [sg.Button('GO', font=(16)), sg.Button('HELP', font=(16))]
]

window = sg.Window('Bing Image Downloader', layout)


def search_and_dump(query, quantity):
    new_search_folder = parent_dir / Path('{}'.format(query))
    try:
        mkdir(new_search_folder)
    except FileExistsError:
        pass
    run(['python', r'C:\Users\kirby\Desktop\BirdUp\EtcFiles\BBID.py', '-s',
         '\"{}\"'.format(query), '-o', '{}'.format(new_search_folder), '--limit', '{}'.format(quantity)])

def help():
    sg.Popup('Welcome to an Image Downloader using Bing and BBID\n\nThis program is meant to be super lightweight and super stupid easy', title='HELP', font=('Trebuchet', 12))
    sg.Popup('Simply put in the query you want a picture of, \n\nand the qunatity of images you want of.', title='HELP', font=('Trebuchet', 12))
    sg.Popup('Your query will be placed in the \"Completed Queries\" folder \n\nin the folder with the same name as the query you made', title='HELP', font=('Trebuchet', 12))
    sg.Popup('Also thanks to ostrolucky on Github for the \n\nBBID code, and for his help', title='HELP', font=('Trebuchet', 12))
    sg.Popup('This is really just a front end to more easily use HIS code\n\nI don\'t claim the core of this project as my own', title='HELP', font=('Trebuchet', 12))

while True:
    event, values = window.Read(timeout=0)
    window.Refresh()
    if event in (None, ""):
        break
    elif event == 'GO':
        search_and_dump(values['_query_'], values['_quantity_'])  

    elif event == 'HELP':
        help()
