#!/usr/bin/env python3
#-*- coding: utf-8 -*-


"""

      1488
     core.py
  Next Gen IRC Bot
    for #s2ch
   forked from
  Konsolka next
 HAPPY NEW YEAR!



"""

from irc import *
import os
import random
import time

channel = 'warbot'
server  = 'chat.freenode.net'
nick    = 'warbot_'
port    =  6667

irc = IRC()
irc.connect(server, channel, nick)

while 1:
    text = irc.get_text()
    url = (channel, 'Hello!')

    if 'PRIVMSG' in text and 'channel' in text and 'hell' in text :
        irc.send(bytes(url.encode()))


