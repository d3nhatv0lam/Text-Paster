import tkinter as tk
from tkinter import filedialog
import keyboard
import pyautogui
import unidecode
import sys , time


root = tk.Tk()
root.withdraw()

Line = []


# Load Text
def LoadData():
    print("Load data: ")
    global file_path
    file_path = filedialog.askopenfilename()

    try:
        with open(file_path,'r',encoding='utf-8') as f:
            data = f.read()
            data = unidecode.unidecode(data)
            print(data)
    except:
        print("Pls Choose Code File or Txt File")
        sys.exit(0)

    return data.split("\n")


def isStop():
    if keyboard.is_pressed('Esc'):
        sys.exit(0)

def clean(char):
    match char:
        case '{' | '[' | '<' | '(' | '"' | '"':
            pyautogui.press('delete')
        case _:
            pass


def Default_Paste():

    for line in Line:
        for char in line:
            isStop()
            pyautogui.press(char)
        pyautogui.press('Enter')

def Python_Paste():
    # tính toán số lần tab hoặc alt tab
    CurLspace = len(Line[0]) - len(Line[0].lstrip())
    defaultspace = 4

    for line in Line:
        backspaceCnt = len(line) - len(line.lstrip())

        line = line.lstrip()

        if (line != ''):
            isSpace = CurLspace - backspaceCnt
            if (isSpace > 0):
                for i in range(0,isSpace//defaultspace):
                    pyautogui.keyDown('shift')
                    pyautogui.press('tab')
                    time.sleep(0.1)
                    pyautogui.keyUp('shift')
            CurLspace = backspaceCnt
            line += ' '

        for char in line:
            isStop()
            pyautogui.press(char)
            clean(char)

        pyautogui.press("Enter")



def C_Cpp_Paste():

    for line in Line:
        line = line.lstrip()
        if line != '':
            line += ' '
        for char in line:
            isStop()
            pyautogui.press(char)
            clean(char)
        pyautogui.press('Enter')



def Paste(extension):
    keyboard.wait("F2")

    match extension:
        case "py":
            Python_Paste()
        case "c":
            C_Cpp_Paste()
        case "cpp":
            C_Cpp_Paste()
        case _:
            Default_Paste()


def Introduce():
    print("---------------")
    print("Tool was created by D3n")
    print("hope u feel good with my tool <3")
    print("#Note: U shoud keep the scene when tool is running")
    print("#Note: Press Esc when tool is running to Stop Copy")
    print("---------------")


if __name__ == "__main__":
    Introduce()
    pyautogui.PAUSE = 0.012
    Line = LoadData()
    print("Press F2 to Copy this!") 
    Paste(file_path.split(".")[-1])