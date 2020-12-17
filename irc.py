#!/usr/bin/env python3
#-*- coding: utf-8 -*-


"""

      1488
     irc.py
  Next Gen IRC Bot
    for #s2ch
   forked from
  Konsolka next
 HAPPY NEW YEAR!



"""

import socket
import sys
import ssl

class IRC:

    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        did = ("PRIVMSG " + chan + " " + msg + "n")
        self.irc.send(bytes(did.encode()))

    def connect(self, server, channel, botnick):
        self.irc.connect(server)

        url = ("USER " + botnick + " " + botnick +" " + botnick + " :This is a fun botty!n" )
        self.irc.send(bytes(url.encode()))

        url = ("NICK " + botnick + "n")
        self.irc.send(bytes(url.encode()))

        url = ("JOIN " + channel + "n")
        self.irc.send(bytes(url.encode()))

    def get_text(self):
        text = self.irc.recv(2048)
        print(text)
        return(text)

        if text.find('PING') != -1:
            dd = ('PONG ' + text. split() [1] + 'rn')
            self.irc.send(bytes(dd.encode()))

