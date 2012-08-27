'''
Created on 15/08/2009

@author: pguridi
'''
import gtk
import gobject
import re

class HRegExEntry(gtk.Entry):

    def __init__(self):
        gtk.Entry.__init__(self)
        self.IP_ADDRESS = "\\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b"
        self.EMAIL = "^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$"

        self.__regularExpression = self.IP_ADDRESS
        #self.__regularExpression = ""
        self.__errorMessage = "Error!"
        self.__okMessage = "Ok!"
        
        if gtk.__dict__.has_key ('ENTRY_ICON_PRIMARY'): 
            self.set_icon_from_stock (gtk.ENTRY_ICON_PRIMARY,gtk.STOCK_FIND)
        
        self.show()
        
        self.connect("changed", self.onTextBoxChanged)
    
    def onTextBoxChanged(self, widget):
        if self.isValid():
            print self.__okMessage
        else:
            print self.__errorMessage
        
    def isValid(self):
        try:
            reg = re.compile(self.__regularExpression)
            return reg.match(self.get_text())
        except:
            return False
        