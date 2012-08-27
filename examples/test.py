'''
Created on 15/08/2009

@author: pguridi
'''
import sys
import os

sys.path.append(os.path.join("..", "pygtk2widgets"))

import RegexEntry
import gtk


win = gtk.Window()

hreg = RegexEntry.RegexEntry("email")

win.add(hreg)

win.show_all()
win.connect("delete-event", gtk.main_quit)


gtk.main()

