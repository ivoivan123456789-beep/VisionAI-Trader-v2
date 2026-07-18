import win32gui


KEYWORDS = [
    "TRADINGVIEW",
    "MNQ",
    "NQ",
    "MES",
    "ES",
    "YM",
    "RTY",
    "BTC",
    "ETH",
    "NASDAQ",
]


def list_windows():
    windows = []

    def callback(hwnd, _):
        if not win32gui.IsWindowVisible(hwnd):
            return

        title = win32gui.GetWindowText(hwnd).strip()

        if title:
            windows.append((hwnd, title))

    win32gui.EnumWindows(callback, None)

    return windows


def find_tradingview_window():

    for hwnd, title in list_windows():

        upper = title.upper()

        if "VISIONAI" in upper:
            continue

        if "VISUAL STUDIO CODE" in upper:
            continue

        if any(word in upper for word in KEYWORDS):
            return hwnd, title

    return None, None