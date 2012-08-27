#!/usr/bin/env python2.6
# -*- coding: latin-1 -*-

import sys
sys.path.append("..")

from pygtk2widgets import ListView
import gtk

items = [ "item1", "item2", "item3" ]

win = gtk.Window()
win.set_title("ListView")
win.set_default_size(50, 250)

# Now add a gtk.Treeview with the list
win.add(ListView(items))

win.show_all()

win.connect("delete-event", gtk.main_quit)

gtk.main()
