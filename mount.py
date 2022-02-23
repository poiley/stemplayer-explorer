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
        return wmi.WMI().Win32_LogicalDisk(VolumeName="STEM PLAYER")
    elif os_str == 'Darwin':
        print('OS Detected: macOS')
    elif os_str == 'Linux':
        print('OS Detected: Linux')
        df = subprocess.check_output("lsusb")
        for i in df.split(b'\n'):
            if i:
                info = device_re.match(i)
                if info:
                    dinfo = info.groupdict()
                    dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                    devices.append(dinfo)
        print(devices)
    else:
        print('Unable to detect OS')

def get_config(drive):
    if os_str == 'Windows':
        os.chdir(drive.name)
        return open(os.getcwd()+'\config.txt', 'r')
