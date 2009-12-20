'''
Created on 16/08/2009

@author: pguridi
'''
import gtk
import gobject

class container(gtk.Bin):
    __gtype_name__ = 'container'
    def __init__(self):
        '''
        Constructor
        '''
        gtk.Bin.__init__(self)
        
        self.__title = gobject.new(gtk.Label("fdsss"), visible=True, xalign=0, yalign=0.5)
        #self.__title.set_parent(self)
        
        self.add(self.__title)