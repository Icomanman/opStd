import pywinauto
import win32com.client as STAAD


def apicall(call='start'):
    # instatiating COM Object (OpenSTAAD) unless specified as otherwise
    if call == 'start':
        app_api = STAAD.Dispatch("StaadPro.OpenSTAAD")
    else:
        # app_api = STAAD.Dispatch("C:\\SProV8i SS6\\STAAD\\Staadpro.exe")
        app_api = STAAD.Dispatch('StaadPro.Sprostaad')

    return app_api


def run(command):
    # function to return callable functions of (OpenSTAAD)
    if command:
        command()
        signal = 1
    else:
        signal = 0
    return signal


def unCall(func):
    # function to return UNcallable functions of (OpenSTAAD)
    if func:
        apicall().GetProcessId
        return
    else:
        pass
        return


def startSTAAD():
    _app = pywinauto.Application().start('C:\\SProV8i SS6\\STAAD\\Staadpro.exe')
    return _app


def startETABS():
    _app = pywinauto.Application().start(
        'C:\\Program Files (x86)\\Computers and Structures\\ETABS 9\\Etabs.exe')
    return _app
