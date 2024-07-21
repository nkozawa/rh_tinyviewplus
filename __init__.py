#my plugin

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
    ipAddress = "192.168.3.6"
    logger.info("TinyViewPlus IP Address: " + ipAddress)

def initialize(rhapi):
    rhapi.events.on(Evt.RACE_LAP_RECORDED, lapRecorded)
    rhapi.events.on(Evt.ACTIONS_INITIALIZE, loadIPaddress)

