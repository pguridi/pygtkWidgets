#!/usr/bin/env python2.6
# -*- coding: latin-1 -*-
'''
Created on 16/08/2009

@author: Pedro Guridi
'''
import gtk
import gobject
import re

class ListView(gtk.VBox):

    def __init__(self, items=[]):
        gtk.VBox.__init__(self)
        
        self.noDuplicates = True
        self.validate = True
        self.regEx = "^"
                
        self.__treeView = gtk.TreeView()
        self.__treeView.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        self.__treeView.set_headers_visible(False)
        
        self.__addStringColumn("Data", self.__treeView)
        
        self.__model = gtk.ListStore(gobject.TYPE_STRING)
        self.__treeView.set_model(self.__model)
        
        self.__scrolledWin = gtk.ScrolledWindow()
        self.__scrolledWin.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        self.__scrolledWin.add(self.__treeView)
        
        self.__hbox = gtk.HBox()
        self.__entry = gtk.Entry()
        self.__addButton = gtk.Button()
        self.__delButton = gtk.Button()
        
        self.__entry.connect("key-press-event", self.__onAddItem)
        self.__entry.set_width_chars(10)
        self.__addButton.connect("clicked", self.__onAddItem)
        self.__delButton.connect("clicked", self.__onDelItem)
        
        image = gtk.Image()
        image.set_from_stock("gtk-add", gtk.ICON_SIZE_SMALL_TOOLBAR)
        image2 = gtk.Image()
        image2.set_from_stock("gtk-remove", gtk.ICON_SIZE_SMALL_TOOLBAR)
        
        self.__addButton.set_image(image)
        self.__delButton.set_image(image2)
        
        self.__hbox.pack_start(self.__entry, True, True, 0)
        self.__hbox.pack_start(self.__addButton, False, False, 0)
        self.__hbox.pack_start(self.__delButton, False, False, 0)
        
        self.pack_start(self.__hbox, False, False, 0)
        self.pack_start(self.__scrolledWin, True, True, 0)
        
        self.setItems(items)
        
    
    def __addStringColumn(self, name, treeview):
        cell = gtk.CellRendererText()
        column = gtk.TreeViewColumn(name, cell, text=0)
        column.set_resizable(True)
        treeview.append_column(column)
        
    def __onAddItem(self, widget, event=None):
        if event:
            if (event.keyval != gtk.keysyms.Return or event.keyval == gtk.keysyms.KP_Enter):
                return
        text = self._getText()
        if not text:
            return
        if self.noDuplicates and self.findItem(text):
            return
        if self.validate and not self.__isValidText():
            return
        
        self._appendItem(text)
        self.__entry.set_text("")
    
    def _getCurrentSelectedItem(self):
        '''
        This method returns the current selected item.
        @return: item, or None.
        '''
        try:
            (model, iter) = self.__treeView.get_selection().get_selected()
            return self.__model.get_value(iter, 0)
        except:
            return None
    
    def __onDelItem(self, widget):
        selection = self.__treeView.get_selection()
        model, selected = selection.get_selected_rows()
        iters = [model.get_iter(path) for path in selected]
        for iter in iters:
             model.remove(iter)

    def _getText(self):
        text = self.__entry.get_text()
        if not text.isspace():
            return text
        else:
            self.__entry.set_text("")
            return None
    
    def _appendItem(self, item):
        self.__model.append([item])
    
    def findItem(self, item):
        for i in self.__model:
            if item == i[0]:
                return True
        return False
    
    def __isValidText(self):
        try:
            reg = re.compile(self.regEx)
            return reg.match(self._getText())
        except:
            return False
        
    def getItems(self):
        items = []
        for i in self.__model:
            items.append(i[0])
        return items
    
    def setItems(self, items=[]):
        self.__model.clear()
        for item in items:
            self._appendItem(item)
        