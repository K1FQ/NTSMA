#!/usr/bin/env python
"""
NTS_MA.PY (National Traffic System Message Assistant)
By: Kevin Shissler/K1FQ (k1fq@arrl.net)
This is Version 1.0
Created/last modified on: August 20, 2013 at 15:35 EDST / April 5, 2015 at 1725 EDST
Additional features (more than 25 word texts allowed, automated ARL texts, etc. will be
added in the next version.
This is my first ever Python & Tkinter application, and I'm not a programmer by trade --
feel free to email constructive feedback. Bug fixes, upgrades, will be forthcoming as needed.
"""
from Tkinter import *
import string
import re

check = 0

def clear_e1_window():
    """Clears the message input window."""
    e1.delete(0,END)

def word_count(check):
    """Checks to make sure there are 25 or fewer words in the message"""
    if check > 25:
        print "Your message exceeds 25 words. Please shorten it to 25 or fewer words."

def cap_msg():
    """Gets the input message text and calls the proof_text function"""
    msgtxt = e1.get()
    proof_text(msgtxt)
    print msgtxt # temp output to screen -- line will go away when finalizing the code

def is_punct(char):
    """Checks the message text for punctuation -- slash bar / virgule is ok; other is not allowed."""
    string.punctuation = re.sub('/', '', string.punctuation)
    return char in string.punctuation

# Main function        
def proof_text(msgtxt):
    """Runs various 'checks' on the message text -- no punctuation, removes extra spaces, counts words,
    changes case to UPPER, and verifies the word count (check) is not greater than 25"""
    # check length of msgtxt
    if len(msgtxt) > 0:
        print len(msgtxt) # temp output to screen -- line will go away when finalizing the code
        
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
        word_count(check)

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
l1 = Label(text='Enter the message text', bg="forest green", fg="yellow").grid(row=0, column=0)
e1 = Entry(root, width=150, relief="sunken")
e1.grid(row=1)
e1.focus_set()
b1 = Button(root, text='Check Message', command=cap_msg).grid(row=2, column=0, sticky=W)
b2 = Button(root, text='Clear Message', command=clear_e1_window).grid(row=2, column=0, sticky=E)
root.mainloop()
