"""BlueZone I/O functions for Python."""

import win32com.client


bz = win32com.client.Dispatch("BZWhll.WhllObj")



def Connect(screen_to_connect):
    """Connect to a BlueZone Screen."""
    bz.connect(screen_to_connect)
    # TODO: error if not connected?

def Focus():
    """Bring the BlueZone Display session window into the foreground."""
	bz.Focus


def GetCursor(RowVal, ColumnVal):
    """Retrieve the host screen cursor position."""
	bz.GetCursor(RowVal, ColumnVal)


def MsgBox(message_to_deliver):
    """Display a pop-up box from within the BlueZone window."""
    bz.MsgBox(message_to_deliver)


def ReadScreen(BufferStr, LengthVal, RowVal, ColumnVal):
    """Retrieve data from the host screen."""
	bz.ReadScreen(BufferStr, LengthVal, RowVal, ColumnVal)


def Search(SearchStr, RowVal, ColumnVal):
    """Searche the host screen for some specified text."""
	bz.Search(SearchStr, RowVal, ColumnVal)


def SendKey(KeyStr):
    """Send a sequence of keys to the display session."""
	bz.SendKey(KeyStr)


def SetCursor(RowVal, ColumnVal):
    """Set the host screen cursor position."""
	bz.SetCursor(RowVal, ColumnVal)


def WaitReady(TimeoutVal, ExtraWaitVal):
    """Suspend script execution until the host screen is ready for keyboard input."""
	bz.WaitReady(TimeoutVal, ExtraWaitVal)


def WriteScreen(WriteStr, RowVal, ColumnVal):
    """Paste the specified text into the host screen."""
	bz.WriteScreen(WriteStr, RowVal, ColumnVal)
