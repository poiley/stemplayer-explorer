import os
import platform
import re
import subprocess

os_str = platform.system()

def get_devices():
    devices = []

    if os_str == 'Windows':
        print('OS Detected: Windows')
        import wmi
        devices = wmi.WMI().Win32_LogicalDisk(VolumeName="STEM PLAYER")
    elif os_str == 'Darwin':
        print('OS Detected: macOS')
    elif os_str == 'Linux':
        print('OS Detected: Linux')
        for scsi_device in os.popen("lsblk -S").read().split('\n'):
            if scsi_device and "Kano" in scsi_device:
                partition = '{}1'.format(scsi_device.split(' ')[0])
                mount_point = os.popen("mount | grep {}".format(partition)).read().split(' ')[2:4]
                devices.append(' '.join(mount_point))

    else:
        print('Unable to detect OS')
    return devices

def get_config(drive):
    if os_str == 'Windows':
        os.chdir(drive.name)
        return open(os.getcwd()+'\config.txt', 'r')
