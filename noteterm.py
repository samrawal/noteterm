#!/usr/bin/env python

import sys
import time
from os import listdir, path, makedirs
import os

notesdir = os.path.realpath(__file__)[:-7]

def print_file(filepath):
   filecontent = ""
   with open(filepath, "r") as file:
      filecontent = file.read()
   print filecontent

def minimize_string(content, cutoff):
   if len(content) > cutoff:
       return content[:cutoff] + "..."
   else:
       return content
   
def search_for_note(searchtitle):
    matchingnotes = []
    for note in listdir(notesdir + "/notes"):
        data = note.split("__")
        notetime = data[0]
        notetitle = data[1][:-4]
        if searchtitle == notetitle:
            with open(notesdir + "/notes/"+note, 'r') as file:
                notecontent = file.read()
                matchingnotes.append((notetime, notecontent))
    return matchingnotes
def print_search_results(searchtitle, matchingnotes):
    if len(matchingnotes) == 0:
        print "No note found. Run \'note -view\' to view all notes."

    elif len(matchingnotes) == 1:
        print matchingnotes[0][1]

    elif len(matchingnotes) > 1:
        print "Multiple results for \'" + searchtitle + "\' found:"
        print "---------------------------------"

        for note in matchingnotes:
            print note[0]
            print note[1]

def add_note(notetitle):
    notetime = time.strftime("%Y-%m-%d::%H:%M")
    if notetitle != '':    #there is a title
        notetitle = notetime + "__" + notetitle 
    else:
        notetitle = notetime

    notecontent = ""
    print "Enter note (press RETURN twice when finished):\n"

    line = raw_input()

    while len(line) != 0:
        notecontent = notecontent + line + "\n"
        line = raw_input()

    with open(notesdir+"/notes/"+notetitle+".txt", "w") as note:
        note.write(notecontent)
        
def view_note():
    notetitle = ""
    notecontent = ""
    notetime = ""

    def view_all_notes():
       template = "{0:18}{1:20}{2:36}"
       print template.format("note (.txt)", "date", "content")
       print "--------------------------------------------------------"
       for note in listdir(notesdir+"/notes"):
           data = note.split("__")
           notetime = data[0]
           notetitle = minimize_string(data[1][:-4], 15)

           with open(notesdir+"/notes/"+note, 'r') as file:
               notecontent = file.read().replace("\n", "")
           notecontent = minimize_string(notecontent, 33) 
            
           print template.format(notetitle, notetime, notecontent)



    if len(sys.argv) == 2:    #view all note summary
        if (sys.argv[1] == "-view" or sys.argv[1] == "-v"):
            view_all_notes();

    elif len(sys.argv) == 3:
       searchtitle = sys.argv[2]
       matchingnotes = search_for_note(searchtitle)
       print_search_results(searchtitle, matchingnotes)
      
    
if not os.path.exists(notesdir+"/notes"):
   os.makedirs(notesdir+"/notes")
   
if len(sys.argv) == 1:
   print_file(notesdir+"/docs/usage.txt")
      
elif sys.argv[1] == "-add" or sys.argv[1] == "-a":
   notetitle = ""
   if len(sys.argv) == 3:
      notetitle = sys.argv[2]
      
   add_note(notetitle)

elif sys.argv[1] == "-view" or sys.argv[1] == "-v":
    view_note()

elif sys.argv[1] == "-help" or sys.argv[1] == "-h":
   print_file(notesdir+"/docs/help.txt")

elif sys.argv[1] == "-dir":
   print "Notes are stored in: {0}/notes/".format(notesdir)
   
else:
    notesearch = search_for_note(sys.argv[1])
    if len(notesearch) == 0:
        print "New note: ", sys.argv[1]
        add_note(sys.argv[1])
    else:
        print_search_results(sys.argv[1], notesearch)
