#!/usr/bin/env python2.6
# -*- coding: latin-1 -*-

from listView import ListView

import gtk

nombres = [ "pedro", "juan", "pepe" ]


win = gtk.Window()

win.set_title("ListView")
win.set_default_size(50, 250)

win.add(ListView(nombres))


win.show_all()

win.connect("delete-event", gtk.main_quit)

gtk.main()