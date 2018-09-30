#!/usr/bin/python

import dbus
import os
import sys


def find_pause(tytul):
    i = 0;
    napis = ""
    for znak in tytul:
        print i
        if znak == "-":
            break;
        else:
            napis += znak
        i += 1
    return napis

try:
    bus = dbus.SessionBus()
    spotify = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
    
    

 #   if os.environ.get('BLOCK_BUTTON'):
 #       control_iface = dbus.Interface(spotify, 'org.mpris.MediaPlayer2.Player')
 #       if (os.environ['BLOCK_BUTTON'] == '1'):
 #           control_iface.Previous()
 #       elif (os.environ['BLOCK_BUTTON'] == '2'):
 #           control_iface.PlayPause()
 #       elif (os.environ['BLOCK_BUTTON'] == '3'):
 #           control_iface.Next()
    
    spotify_iface = dbus.Interface(spotify, 'org.freedesktop.DBus.Properties')
    props = spotify_iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

    if (sys.version_info > (3, 0)):
        #napis = (str(props['xesam:artist'][0]) + " - " + find_pause(str(props['xesam:title'])))   
        #napis = (str(props['xesam:artist'][0]) + " - " + find_pause(str(props['xesam:title'])))
        napis = (str(props['xesam:artist'][0]) + " - " + str(props['xesam:title'])) 
        print napis[:40]

    else:
        #napis = (str(props['xesam:artist'][0]) + " - " + str(props['xesam:title']))
        #napis = (props['xesam:artist'][0] + " - " + props['xesam:title']).encode('utf-8')
        napis = (props['xesam:artist'][0] + " - " + props['xesam:title']).encode('utf-8')
        print napis[:40]
        
    exit
except dbus.exceptions.DBusException:
    exit


#original 
#    if (sys.version_info > (3, 0)):
#        print(str(props['xesam:artist'][0]) + " - " + str(props['xesam:title']))
#    else:
#        print(props['xesam:artist'][0] + " - " + props['xesam:title']).encode#('utf-8')
#    exit
#except dbus.exceptions.DBusException:
 #   exit


#my v1 - static number of characters cut
#    spotify_iface = dbus.Interface(spotify, 'org.freedesktop.DBus.Properties')
#    props = spotify_iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
#
#    if (sys.version_info > (3, 0)):
#        napis = (str(props['xesam:artist'][0]) + " - " + str(props['xesam:title']))        
#        print napis[:40]
#    else:
#        napis = (props['xesam:artist'][0] + " - " + props['xesam:title']).encode#('utf-8')
#        print napis[:40]
#    exit
#except dbus.exceptions.DBusException:
#    exit


