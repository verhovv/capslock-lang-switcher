import keyboard
import win32api
import win32con
import win32gui

caps_lock_lock = False


def toggle_caps_lock(reverse: bool = False) -> None:
    if reverse:
        win32api.keybd_event(win32con.VK_CAPITAL, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(win32con.VK_CAPITAL, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    else:
        win32api.keybd_event(win32con.VK_CAPITAL, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        win32api.keybd_event(win32con.VK_CAPITAL, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)


def switch_language() -> None:
    hwnd = win32gui.GetForegroundWindow()
    win32api.SendMessage(hwnd, win32con.WM_INPUTLANGCHANGEREQUEST, 0, 0)


def on_caps_lock_down(event: keyboard.KeyboardEvent) -> None:
    global caps_lock_lock

    if not caps_lock_lock:
        if not keyboard.is_pressed('alt'):
            switch_language()
            toggle_caps_lock(reverse=True)
        else:
            toggle_caps_lock()

        caps_lock_lock = True


def on_caps_lock_up(event: keyboard.KeyboardEvent) -> None:
    global caps_lock_lock

    caps_lock_lock = False


keyboard.on_release_key(key='capslock', callback=on_caps_lock_up)
keyboard.on_press_key(key='capslock', callback=on_caps_lock_down)

keyboard.wait()
