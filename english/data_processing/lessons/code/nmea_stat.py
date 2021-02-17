#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" NMEA statistics
"""

import sys
import re

def checksum(buf):
    """ check nmea checksum on line
        returns two digit hexa number
    """
    cs = ord(buf[1])
    for ch in buf[2:-3]:
        cs ^= ord(ch)
    ch = '0' + re.sub('^0x', '', hex(cs))
    return ch[-2:].upper()

def nmea2deg(nmea):
    """ convert nmea angle (dddmm.ss) to degree """
    w = nmea.rstrip('0').split('.')
    return int(w[0][:-2]) + int(w[0][-2:]) / 60.0 + int(w[1]) / 3600.0
    
if len(sys.argv) > 1:
    fin = sys.argv[1]   # get input file from command line
    fi = open(fin, 'r') # input file
else:
    fi = sys.stdin
token = {}
minlat = 90
minlon = 180
maxlat = -90
maxlon = -180
for line in fi:
    line = line.strip()
    if checksum(line) != line[-2:]:
        print("Chechsum error: " + line)
        continue
    nmea = line.split(',')
    if nmea[0] not in token:
        token[nmea[0]] = 0
    token[nmea[0]] += 1
    if re.match('\$..GGA', line):
        if nmea[6] == '1':  # use only fix
            lat = nmea2deg(nmea[2])
            if nmea[3].upper() == 'S':
                lat *= -1
            lon = nmea2deg(nmea[4])
            if nmea[5].upper() == 'W':
                lon = 360 - lon
            height = float(nmea[9])
            minlat = min(minlat, lat)
            minlon = min(minlon, lat)
            maxlat = max(maxlat, lat)
            maxlon = max(maxlon, lon)
fi.close()
print (minlat, minlon, maxlat, maxlon)
for t in token:
    print("{}: {}".format(t, token[t]))
