from note import *

class Folder:
    name = ""
    folder_list = []
    note_list = []
    
    def __init__(self, name):
	self.name = name
	
    def __str__(self):
	return name
    
    def addFolder(self, folderName):
	self.folder_list.append(Folder(folderName))
	
    def addNote(self, title, body):
	self.note_list.append(Note(title, body))
	
    def printFolders(self):
	for folder in self.folder_list:
	    print folder.name
	    
    def printNoteTitles(self):
	for note in self.note_list:
	    print note.title
