# =================================================================================
# VERSION: 2.1
# =================================================================================
import time
# =================================================================================
import pyautogui                        # pip install pyautogui
import win32api, win32con               # pip install pypiwin32
# =================================================================================
import keyboard                         # pip install keyboard
# =================================================================================
class PianoTiles():
    SITE = "https://www.gamesgames.com/game/magic-piano-tiles"
    QUIT_KEY  = "esc"
    START_KEY = "`"     # TILDA
    def __init__(self, minX=0, minY=0, maxX=0, maxY=0, columns=[0,0,0,0], row=0) -> None:
        print(self.SITE)
        self.MIN_X = minX
        self.MIN_Y = minY
        self.MAX_X = maxX
        self.MAX_Y = maxY
        self.columns    = columns
        self.row        = row
        self.startEventOnPress()
        self.run()
    def run(self):
        current_x_col = -1
        running_x_col = -1
        # self.moveClick(950, 550)      # X & Y cordinates of start button
        while True:
            running_x_col = self.getKeyColumn()
            self.forceQuitOnPress()
            if running_x_col != current_x_col and running_x_col != -1:
                current_x_col = running_x_col
                self.moveClick(self.columns[current_x_col], self.row + 50)
    def forceQuitOnPress(self):
        if keyboard.is_pressed(self.QUIT_KEY): 
            print("'{}' Pressed. TERMINATOR TERMINATED!".format(self.QUIT_KEY))
            exit()
    def startEventOnPress(self):
        print("Press '{}' to TERMINATE".format(self.QUIT_KEY))
        print("Press '{}' to START SEQUENCE".format(self.START_KEY))
        while True:
            self.forceQuitOnPress()
            pressed = keyboard.read_key()
            if pressed == self.START_KEY:
                print("STARTED SEQUENCE")
                break
    def moveClick(self, x=0, y=0):
        if not (self.MIN_X <= x and x <= self.MAX_X):     return None
        if not (self.MIN_Y <= y and y <= self.MAX_Y):     return None
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        time.sleep(.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    def getKeyColumn(self):
        c0 = pyautogui.pixel(self.columns[0], self.row)[0]
        if 0 == c0:     return 0
        c1 = pyautogui.pixel(self.columns[1], self.row)[0]
        if 0 == c1:     return 1
        c2 = pyautogui.pixel(self.columns[2], self.row)[0]
        if 0 == c2:     return 2
        c3 = pyautogui.pixel(self.columns[3], self.row)[0]
        if 0 == c3:     return 3
        return -1

minX=0          # Keep as 0
minY=0          # Keep as 0
maxX=1920       # Your Monitor Pixel Width
maxY=1080       # Your Monitor Pixel Height
row = 500       # Y axis - read black keys
columns=[
    750,        # Column 1's aprox pixel on the X axis
    900,        # Column 2's aprox pixel on the X axis
    1050,       # Column 3's aprox pixel on the X axis
    1200,       # Column 4's aprox pixel on the X axis
]
piano = PianoTiles(minX, minY, maxX, maxY, columns, row)
