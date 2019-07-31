import json
import time
import openstd
from pywinauto import Application
import pywinauto as pw
mouse = pw.mouse


def pause(sec=3):
    time.sleep(sec)
    return


def pas():
    # for almost imperceivable pauses like the average human interaction with the machine
    time.sleep(1)
    return


def prompt():
    print('No instance of STAAD.Pro is found.')
    usrInput = raw_input('Would you like to open a new one? y/n\n')
    return usrInput


try:
    # try to instatiate OpenSTAAD to check whether the app is already opened
    OSt = openstd.apicall()
    PID = OSt.GetProcessId
    print 'OpenSTAAD was successfully instantiated; PID =', PID

    # if successful, connect to the app via pywinauto using PID
    std = Application().connect(process=PID)

    # pause to ensure connection: Giving the machine the benefit of the doubt
    pas()
    print 'pywinauto successfully connected to the main app using PID'

except:
    usrInput = prompt()
    while usrInput != 'n'or usrInput != 'y':
        if usrInput == 'y':
            OSt = openstd.apicall('start')
            OSt.ShowApplication
            if OSt == None:
                print 'ERROR'
                exit()
            # app = OSt.start('staad')
            break
        elif usrInput != 'n' and usrInput != 'y':
            usrInput = prompt()
        else:
            exit()

# # specifying window handles
# # control_id's can be taken from window.get_properties()
# stdHandle = OSt.GetMainWindowHandle
# mainWindow = std.window(handle=stdHandle)
# # popUpWindow = std.window(best_match='STAAD.Pro V8i (SELECTseries 6)')
# # popHandle = pw.findwindows.find_windows(process=PID)[0]
# # print popHandle
# # popUpWindow = std.window(handle=popHandle)
# popUpWindow = std.window(control_id=0, active_only=True)

# # part of the analysis app
# outputWindow = std.window(best_match='STAAD Output Viewer')
# modelWindow = mainWindow.child_window(control_id=65280)
# # sample control_id taken from te command below:
# # print mainWindow.child_window(best_match=' - Whole Structure').get_properties()


# def analApp():
#     # link to Staad analysis app
#     runnr = Application().connect(title_re="STAAD Analysis and Design")
#     if runnr:

#         # runnr.wait_cpu_usage_lower(threshold=0.1, timeout=2, usage_interval=1)
#         # # BUGGY, killing process prematurely at certain times
#         print 'Analysis successfully connected; will close when cpu usage falls below 0.1%'
#         cycles = 1

#         while runnr.cpu_usage() > 0.1:
#             print 'running analysis... ', cycles
#             cycles += 1
#         else:
#             runnr.kill()
#             print 'Analysis Completed'
#         return runnr.is_process_running()
#     else:
#         print 'Failed to connect'
#         return True


# def run():
#     # run analysis
#     mainWindow.type_keys('^{F5}')
#     # pas()
#     # skipping any pop dialogs, if applicable
#     try:
#         while popUpWindow:
#             popUpWindow.type_keys('{ENTER}')
#     except:
#         exit

#     viewMode = analApp()
#     # viewing results via OSt
#     if viewMode == False:
#         # OSt.View.SetModeSectionPage(1, 6, 19)
#         mouse.click(coords=(1000, 740))
#         viewDiag()
#         modelWindow.maximize()
#         return
#     else:
#         print 'An error occured with STAAD run.'
#         exit
#         return

#     analApp()
#     return


# def viewDiag():

#     OSt.View.ShowIsometric()
#     OSt.View.SetModeSectionPage(0, 1, 0)

#     modelWindow.maximize()
#     OSt.View.ZoomExtentsMainView()

#     mouse.right_click(coords=(330, 930))
#     mouse.click(coords=(370, 790))
#     mouse.click(coords=(1160, 215))
#     mouse.click(coords=(685, 323))
#     mouse.click(coords=(880, 895))
#     return


# def showFail():

#     OSt.View.ShowIsometric()
#     OSt.View.SetModeSectionPage(0, 3, 6)
#     OSt.View.ZoomExtentsMainView()

#     mouse.right_click(coords=(330, 930))
#     mouse.click(coords=(370, 790))
#     mouse.click(coords=(1160, 215))
#     mouse.click(coords=(685, 323))
#     mouse.click(coords=(880, 895))
#     return


# def getSectionView(plane='xy', coord=0):
#     v = OSt.View
#     if plane == 'xy':
#         planeInt = 0
#         v.ShowFront()
#     elif plane == 'yz':
#         planeInt = 1
#         v.ShowLeft()
#     elif plane == 'xz':
#         planeInt = 2
#         v.ShowPlan()
#     else:
#         print 'not a valid plane (xy, yz or xz).'
#         planeInt = 0

#     modelWindow.maximize()

#     # switch off member tags
#     # v.SetLabel(1, False)
#     # switch on member section
#     # v.SetLabel(7, True)
#     # take a section within a plane
#     v.SetSectionView(planeInt, coord - 0.1, coord + 0.1)
#     v.ZoomExtentsMainView()

#     # capture elevation here...

#     return


# def takePicture(name):
#     std.top_window().menu_select("Edit -> Take Picture")
#     std.top_window().type_keys(name)
#     std.top_window().child_window(title="OK").type_keys('{ENTER}')
#     return


# def saveSectionView(plane, coordList=[]):

#     for x in range(len(coordList)):
#         OSt.View.ShowAllMembers()
#         print 'Section at ', coordList[x]
#         title = 'Elev ' + str(x+1)
#         getSectionView(plane, coord=coordList[x])
#         pause(2)
#         takePicture(title)

#     return


# # std.top_window().print_control_identifiers()
# # print std['Dialog'].Texts()
# # print std['Dialog'].window_text()
# # std.window(title='Report Setup').print_control_identifiers()

# # std['Dialog'].print_control_identifiers()
# # std['Dialog'].No.click()
# # 32871

# # run()

# # coordList = [0, 6.5, 13, 26, 39, 52, 59.9, 71.3]
# coordList = [15, 30, 39, 60]
# saveSectionView('yz', coordList)

# # viewDiag()
# # showFail()


# # terminate OpenSTAAD Instance by the end of each run to avoid unexpected behaviour
# OSt = openstd.apicall('end')
# std = None
# runnr = None

# print '*** script finished ***'
