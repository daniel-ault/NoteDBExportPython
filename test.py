import sqlite3

from note import *
from folder import *

conn = sqlite3.connect("notes.db")
c = conn.cursor()

# c.execute("SELECT folder FROM Notes WHERE is_folder=1")
# print c.fetchone();

c.execute("SELECT folder FROM Notes WHERE is_folder=1");

folders = c.fetchall()

for i in range(0, len(folders)):
    print folders[i][0]
    

title = "TITLE whoo"
message = "this is an AWESOME message"

note = Note(title, message)

note.printNote()

folders = Folder("root")

folders.addFolder("folder1")
folders.addFolder("folder2")
folders.addFolder("folder3")

folders.printFolders()

print "teeeest " + title

#for row in c.execute("SELECT folder FROM Notes WHERE is_folder=1"):
#    print row