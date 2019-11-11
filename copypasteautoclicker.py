import win32api, win32con
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

print("Clicking in 3 seconds")
time.sleep(3)
print("Clicking")

for i in range(1000):
    click(960,540)
    time.sleep(0.003)
