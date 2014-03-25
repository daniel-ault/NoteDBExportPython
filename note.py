
class Note:
    title = ""
    message = ""
    
    def __init__(self, title, message):
	self.title = title
	self.message = message
    
    
    def __str__(self):
	print "Note title: " + self.title
    
    def printNote(self):
	print self.title
	print self.message