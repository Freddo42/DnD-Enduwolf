#!/usr/bin/python
import sys, socket, time

server = 'https://roll20.net/'
channel = '##Endu\'s game'
channel = '#DnD

def run():
        global server, channel
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((server, 6667))

        conn.sendall('USER Freddo * * Freddo\r\n')
        conn.sendall('PASS dndf0r3v3r\r\n')
        conn.sendall('NICK Morgran\r\n')
        conn.sendall('JOIN %s\r\n' % channel)
        conn.sendall('JOIN %s\r\n' % channel1)

        open_log()
