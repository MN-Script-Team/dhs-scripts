"""BlueZone I/O functions for Python."""

import win32com.client

bz = win32com.client.Dispatch("BZWhll.WhllObj")


def Connect(screen_to_connect):
    """Connect to a BlueZone Screen."""
    bz.connect(screen_to_connect)
    # TODO: error if not connected?


def Focus():
    """Bring the BlueZone Display session window into the foreground."""
    bz.Focus()


def CursorCol():
    """Return current cursor column of the connected BZ screen."""
    return bz.GetCursor(0, 0)[2]


def CursorRow():
    """Return current cursor row of the connected BZ screen."""
    return bz.GetCursor(0, 0)[1]


def MsgBox(message_to_deliver):
    """Display a simple pop-up box from within the BlueZone window."""
    bz.MsgBox(message_to_deliver)


def ReadScreen(LengthVal, RowVal, ColumnVal):
    """Retrieve data from the host screen."""
    ret_details = bz.ReadScreen("", LengthVal, RowVal, ColumnVal)
    # ret_details is a list with two items, 0 (any error code, 0 for success), and 1 (the text it read from BZ)
    if ret_details[0] != 0:
        raise ValueError("Either the row or column variable are too high.")
    return ret_details[1]


def Search(SearchStr):
    """Search the host screen for some specified text."""
    return bz.Search(SearchStr, 1, 1)


def SendKey(KeyStr):
    """Send a sequence of keys to the display session."""
    bz.SendKey(KeyStr)


def SetCursor(RowVal, ColumnVal):
    """Set the host screen cursor position."""
    bz.SetCursor(RowVal, ColumnVal)


def Transmit():
    """Send a transmit key and wait until the window refreshes."""
    SendKey("<enter>")
    WaitReady(0, 0)


def WaitReady(TimeoutVal, ExtraWaitVal):
    """Suspend script execution until the host screen is ready for keyboard input."""
    bz.WaitReady(TimeoutVal, ExtraWaitVal)


def WriteScreen(WriteStr, RowVal, ColumnVal):
    """Paste the specified text into the host screen."""
    bz.WriteScreen(WriteStr, RowVal, ColumnVal)
