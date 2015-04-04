#!/usr/bin/env python
"""
NTS_MA.PY (National Traffic System Message Assistant)
By: Kevin Shissler/K1FQ (k1fq@arrl.net)
This is Version 1.0
Created/modified on: August 20, 2013 at 15:35 EDST
Additional features (more than 25 word texts allowed, automated ARL texts, etc. will be
added in the next version.
This is my first ever Python & Tkinter application, and I'm not a programmer by trade --
feel free to email constructive feedback. Bug fixes, upgrades, will be forthcoming as needed.
"""
from Tkinter import *
import string
import re

check = 0

def cap_msg():
    msgtxt = e1.get()
    prooftext(msgtxt)
    print msgtxt

# Function checks the message text for punctuation -- slash bar / virgule is ok.
def is_punct(char):
    string.punctuation = re.sub('/', '', string.punctuation)
    return char in string.punctuation

# Main function        
def prooftext(msgtxt):
    # check length of msgtxt
    if len(msgtxt) > 0:
        print len(msgtxt)
        
        # Check for punctuation
        for char in msgtxt:
            if is_punct(char):
                print "Punctuaton has been detected in your message text. Please remove punctuation and check again."
        
        # Replace tabs, newlines, & other whitespace characters with a singe space;
        # .strip() removes same at front/end of string
        
        re.sub('\s+', ' ', msgtxt).strip()
        print msgtxt, '\n', len(msgtxt)
        
        # 'Count' the number of words; place in variable for Message Preamble
        check = msgtxt.count(' ') + 1 # spaces + 1 should = words
        
        # And, because the 'standard' ARRL Radiogram has 25 words or less, this version is
        # going to enforce the 25 word limit -- this is a good place to check for that.
        if check > 25:
            print "shit"
        # Convert the text into UPPERCASE
        msgtxt = msgtxt.upper()
        
        # Split the message text into words, placing words in a list
        msgtxt_list = msgtxt.split()

        
        print msgtxt_list[0:5]
        print msgtxt_list[5:10]
        print msgtxt_list[10:15]
        print msgtxt_list[15:20]
        print msgtxt_list[20:25]
        print msgtxt
        print check

        
    # otherwise the length is zero -- pop-up a warning "Please enter some text"
    else:
        print "You must input some text."
    return msgtxt


root = Tk()
root.configure(bg="forest green")
l1 = Label(text='Enter the message text', bg="forest green", fg="yellow").pack(side=TOP)
e1 = Entry(root, width=150, relief="sunken")
e1.pack()
e1.focus_set()
b1 = Button(root, text='Check Message', command=cap_msg)
b1.pack()

root.mainloop()
