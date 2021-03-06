#!/usr/bin/env python3
#*******************************************************
#       Filename: ps5.py
#       Author: Snowball Wang
#       Mail: wjq1996@mail.ustc.edu.cn
#       Description: Solution to problem set 5
#       Created on: 2018-11-14 17:09:58
#*******************************************************

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        found = False
        # Translate every letter in text to lowercase letter,
        # and replace punctuation with one blank space.
        text = text.lower()
        for char in text:
            if char in string.punctuation:
                #text.replace(char, ' ')
                # it is wrong, cause text.replace()
                # doesn't change the original text, it has to assign the
                # copy to the new string
                text = text.replace(char, ' ')

        # Turn text into a list containing all elements
        text = ' '.join(text.split())
        text_list = text.split()

        # Make a new list loc_list to record the location
        # of letter we find in text.
        loc_list = []
        for w in self.phrase.split():
            if w in text_list:
                loc_list.append(text_list.index(w))
            else:
                return False

        # Check out whether the location of letter we find
        # in text are next to each other in order.
        for i in range(1, len(loc_list)):
            if int(loc_list[i]) - int(loc_list[i-1]) == 1:
                found = True
            else:
                return False
        return found



# Problem 3
# TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        if self.is_phrase_in(story.get_title()):
            return True
        else:
            return False


# Problem 4
# DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        if self.is_phrase_in(story.get_description()):
            return True
        else:
            return False

# TIME TRIGGERS

# Problem 5
# TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, pubdate):
            pubdate = datetime.strptime(pubdate, "%d %b %Y %H:%M:%S")
            pubdate = pubdate.replace(tzinfo=pytz.timezone("EST"))
            self.pubdate = pubdate

# Problem 6
# BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, pubdate):
        TimeTrigger.__init__(self, pubdate)

    def evaluate(self, story):
        story_pubdate = story.get_pubdate()
        story_pubdate = story_pubdate.replace(tzinfo=pytz.timezone("EST"))
        if self.pubdate > story_pubdate:
            return True
        else:
            return False

class AfterTrigger(TimeTrigger):
    def __init__(self, pubdate):
        TimeTrigger.__init__(self, pubdate)

    def evaluate(self, story):
        story_pubdate = story.get_pubdate()
        story_pubdate = story_pubdate.replace(tzinfo=pytz.timezone("EST"))
        if self.pubdate < story_pubdate:
            return True
        else:
            return False


# COMPOSITE TRIGGERS

# Problem 7
# NotTrigger
class NotTrigger(Trigger):
    # T is a trigger of type trigger as a parameter passed in
    def __init__(self, T):
       self.T = T

    def evaluate(self, story):
        return not self.T.evaluate(story)


# Problem 8
# AndTrigger
class AndTrigger(Trigger):
    # T1 and T2 are triggers of type trigger as parameter passed in
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        return self.T1.evaluate(story) and self.T2.evaluate(story)

# Problem 9
# OrTrigger
class OrTrigger(Trigger):
    # T1 and T2 are triggers of type trigger as parameter passed in
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        return self.T1.evaluate(story) or self.T2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    stories_list = []
    # Loop the stories and put story that can be triggered into stories_list
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                # Story doesn't appear before
                if story not in stories_list:
                    stories_list.append(story)

    return stories_list



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    triggers_list = []
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    for elem in lines:
        # Separate each element in lines
        elem = elem.split(',')
        # If the first element is ADD, put the triggers
        # into the triggers_list
        if elem[0] == 'ADD':
            for trigger in elem[1:]:
                triggers_list.append(eval(trigger))
        else:
            # Match the second element in elem list
            # and instantialize the trigger
            if elem[1] == 'TITLE':
                exec("%s = TitleTrigger(elem[2])" %(elem[0]))
            elif elem[1] == 'DESCRIPTION':
                exec("%s = DescriptionTrigger(elem[2])" %(elem[0]))
            elif elem[1] == 'BEFORE':
                exec("%s = BeforeTrigger(elem[2])" %(elem[0]))
            elif elem[1] == 'AFTER':
                exec("%s = AfterTrigger(elem[2])" %(elem[0]))
            # eval() here is used to make sure elem[2] passed in as
            # trigger object, not str. Otherwise it will cause error
            # info like 'str object doesn't have the attribute evaluate'
            elif elem[1] == 'NOT':
                exec("%s = NotTrigger(eval(elem[2]))" %(elem[0]))
            elif elem[1] == 'AND':
                exec("%s = AndTrigger(eval(elem[2]), eval(elem[3]))" %(elem[0]))
            elif elem[1] == 'or':
                exec("%s = OrTrigger(eval(elem[2]), eval(elem[3]))" %(elem[0]))
            else:
                continue

    return triggers_list



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # After implementing read_trigger_config, uncomment this line
        #triggerlist = read_trigger_config('triggers.txt')
        triggerlist = read_trigger_config('my_own_triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            # Filter the stories according to the triggers defined by user
            stories = filter_stories(stories, triggerlist)


            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

