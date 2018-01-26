"""Test."""

# Imports the bzio module.
import bzio

# Connects to BlueZone.
bzio.Connect("")

# Focuses the BlueZone window.
bzio.Focus()

# Reads a few characters into a variable, read_var.
read_var = bzio.ReadScreen(4, 3, 25)
print(read_var)

# Now it writes those characters into a BlueZone screen.
bzio.WriteScreen(read_var, 12, 61)

# Now it prints the current CursorRow and CursorCol.
print(bzio.CursorRow())
print(bzio.CursorCol())

# Lastly, we'll make a MsgBox!
bzio.MsgBox("Thanks for running me in Python!")
