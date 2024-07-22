### rh_tinyviewplus ###
# This plugin adds TinyViewPlus LAP from RotorHazard 
# when Tinyviewplus fails to read AR markers!
# Author: KozakFPV, Version: 1.0

import os
import re
import logging
logger = logging.getLogger(__name__)

from eventmanager import Evt
from pythonosc.udp_client import SimpleUDPClient

ipAddress = "127.0.0.1"

def sendLap(camera):
    client = SimpleUDPClient(ipAddress, 4000)
    client.send_message("/v1/camera/"+str(camera)+"/lap", "add")

def lapRecorded(args):
    node = args['node_index']
    camera = node + 1
    logger.info("Adding LAP to TinyViewPlus("+ipAddress+") Camera"+str(camera)+")")
    sendLap(camera)

def loadIPaddress(args):
    global ipAddress
    ipfile = "tvpIPAddress.ini"         # this file should be placed at user home
    home = os.path.expanduser("~")      # probably /home/pi
    ipfilepath = os.path.join(home, ipfile)
    if (os.path.isfile(ipfilepath)):
        logger.info("Reading "+ipfilepath)
        f = open(ipfilepath, 'r')
        d = f.read()
        f.close()
        pat = r'[0-9]+(?:\.[0-9]+){3}'  # mostly matches with IP address
        ip = re.findall(pat,d)
        if (0 < len(ip)):
            ipAddress = ip[0]    
    logger.info("TinyViewPlus IP Address: " + ipAddress)

def initialize(rhapi):
    rhapi.events.on(Evt.RACE_LAP_RECORDED, lapRecorded)
    rhapi.events.on(Evt.ACTIONS_INITIALIZE, loadIPaddress)
