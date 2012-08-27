'''
Created on 15/08/2009

@author: pguridi
'''
import gtk
import gobject
import re

COMMON_REGEX = { "ipv4" :  "\\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b",
                 "email"  : "^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$"}

class RegexEntry(gtk.Entry):

    def __init__(self, regex):
        gtk.Entry.__init__(self)

        if regex:
            if regex in COMMON_REGEX.keys():
                self._regex = re.compile(COMMON_REGEX[regex])
            else:
                self._regex = re.compile(regex)
        
        self.show()
        
        self.connect("changed", self.onTextBoxChanged)
    
    def onTextBoxChanged(self, widget):
        if not self.isValid():
            self.set_icon_from_stock(gtk.ENTRY_ICON_PRIMARY, gtk.STOCK_DIALOG_ERROR)
            self.set_icon_tooltip_text(gtk.ENTRY_ICON_PRIMARY, "Invalid format.")
        else:
            self.set_icon_from_stock(gtk.ENTRY_ICON_PRIMARY, None)
        
    def isValid(self):
        try:
            return self._regex.match(self.get_text())
        except:
            return False
        
