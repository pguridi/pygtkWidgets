from container import container
import gtk

cont = container()

win = gtk.Window()

win.add(cont)

win.show_all()
win.connect("delete-event", gtk.main_quit)


gtk.main()