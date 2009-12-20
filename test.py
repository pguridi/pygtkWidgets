'''
Created on 15/08/2009

@author: pguridi
'''
import HRegExEntry
import gtk


win = gtk.Window()

hreg = HRegExEntry.HRegExEntry()

win.add(hreg)

win.show_all()
win.connect("delete-event", gtk.main_quit)


gtk.main()

