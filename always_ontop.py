import win32gui, win32con, keyboard

class Window():
    def __init__(self, window, active_code, inactive_code):
        self.window = window
        self.active_code = active_code
        self.inactive_code = inactive_code

    def get_window(self):
        return self.window
    
    def get_active_inactive_code(self):
        return [self.active_code, self.inactive_code]


added_windows = []

def setOnTop():
    global added_windows
    window = win32gui.GetForegroundWindow()
    found = False
    found_window = None
    for added_window in added_windows:
        if added_window.get_window() == window:
            found_window = added_window
            found = True


    size = win32gui.GetWindowRect(window)
    x = size[0]
    y = size[1]
    w = size[2] - x
    h = size[3] - y

    if found:
        window_code = win32gui.GetWindowLong(window, -20)
        active_inactive_code = found_window.get_active_inactive_code()
        if window_code == active_inactive_code[0]:
            inactive_code = win32gui.SetWindowPos(window, win32con.HWND_NOTOPMOST, x, y, w, h, 0)

        elif window_code == active_inactive_code[1]:
            active_code = win32gui.SetWindowPos(window, win32con.HWND_TOPMOST, x, y, w, h, 0)
    else:
        win32gui.SetWindowPos(window, win32con.HWND_TOPMOST, x, y, w, h, 0)
        active_code = win32gui.GetWindowLong(window, -20)
        win32gui.SetWindowPos(window, win32con.HWND_NOTOPMOST, x, y, w, h, 0)
        inactive_code = win32gui.GetWindowLong(window, -20)
        added_windows.append(Window(window, active_code, inactive_code))
        win32gui.SetWindowPos(window, win32con.HWND_TOPMOST, x, y, w, h, 0)



keyboard.add_hotkey('ctrl+space', setOnTop)
keyboard.wait()

