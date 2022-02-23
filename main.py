import os
import platform

import re
import subprocess

os = platform.system()

def get_devices():
    device_re = re.compile(b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    devices = []

    if os == 'Windows':
        print('Windows')
        
    elif os == 'Darwin':
        print('macOS')
    elif os == 'Linux':
        df = subprocess.check_output("lsusb")
        for i in df.split(b'\n'):
            if i:
                info = device_re.match(i)
                if info:
                    dinfo = info.groupdict()
                    dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                    devices.append(dinfo)
        print('Linux')
        print(devices)
    else:
        print('Unable to detect OS')

if __name__ == '__main__':
    get_devices()