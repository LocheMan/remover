from pystyle import *
import time

LocheMan_WaterMark = ['\n  ╔╗           ╔╗      ╔═╗╔═╗         ', '  ║║           ║║      ║║╚╝║║         ', '  ║║   ╔══╗╔══╗║╚═╗╔══╗║╔╗╔╗║╔══╗ ╔═╗ '\
                      , '  ║║ ╔╗║╔╗║║╔═╝║╔╗║║╔╗║║║║║║║╚ ╗║ ║╔╗╗', '  ║╚═╝║║╚╝║║╚═╗║║║║║║═╣║║║║║║║╚╝╚╗║║║║', '  ╚═══╝╚══╝╚══╝╚╝╚╝╚══╝╚╝╚╝╚╝╚═══╝╚╝╚╝']

for part in LocheMan_WaterMark:
    print(Colorate.Horizontal(Colors.blue_to_red, part, 1))
    time.sleep(0.05)
