import os
import platform
import re
import subprocess
import wmi

os_str = platform.system()

def get_devices():
    device_re = re.compile(b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    devices = []

    if os_str == 'Windows':
        print('OS Detected: Windows')
        devices = wmi.WMI().Win32_LogicalDisk(VolumeName="STEM PLAYER")
    elif os_str == 'Darwin':
        print('OS Detected: macOS')
    elif os_str == 'Linux':
        print('OS Detected: Linux')
        for usb_device in subprocess.check_output("lsusb").split(b'\n'):
            if usb_device:
                info = device_re.match(usb_device)
                if info:
                    dinfo = info.groupdict()
                    dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                    if dinfo['id'] == '1209:572a':
                        devices.append(dinfo)
    else:
        print('Unable to detect OS')
    return devices

def get_config(drive):
    if os_str == 'Windows':
        os.chdir(drive.name)
        return open(os.getcwd()+'\config.txt', 'r')
