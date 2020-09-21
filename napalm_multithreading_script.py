from netmiko import ConnectHandler
from napalm import get_network_driver
from datetime import datetime
import getpass
import os
import sys
import time
import re
import telnetlib
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import json
from random import random
import threading
from io import StringIO
from time import gmtime, strftime
from pprint import pprint
from time import time


class NapalmMultithreadingTelnet:
    
    def read_devices(self, devices_filename):
        devices = {} # create our dictionary for storing devices and their info

        with open(devices_filename) as devices_file:
             for device_line in devices_file:

                 device_info = device_line.strip().split(',')  #extract device info from line

                 device = {'ipaddr': device_info[0],
                           'type':   device_info[1],
                           'name':   device_info[2],
                           'username':   device_info[3],
                           'password':   device_info[4],
                           'config_file':   device_info[5],
                           'port':   device_info[6]}  # create dictionary of device objects ...

                 devices[device['port']] = device  # store our device in the devices dictionary
                                                # note the key for devices dictionary entries is ipaddr

        print ('\n----- devices --------------------------')
        pprint(devices)

        return devices

#------------------------------------------------------------------------------
    def config_worker(self, a, b, c, d, e, f):

        #---- Connect to the device ----
        if b == 'cisco-ios-telnet': device_type = 'ios'
        else:                               device_type = 'ios'    # attempt Cisco IOS telnet as default



        if device_type == 'ios' and f == '7026':
           #---- Use CLI command to get configuration data from device
           print("Logging to Telnet device")
           starting_time = time()
           print('starting_time',starting_time)
           driver = get_network_driver(device_type)
           optional_args = {'port': f, 'transport': 'telnet'}
           device1 = driver(a, c, d, optional_args=optional_args)
           device1.open()
           print ('---- load file------------')
           config_data_ip1 = device1.device.send_config_from_file(config_file=e)
           print ('---- print file------------')
           print(config_data_ip1)
           device1.close()
           print ('\n---- End get config threading, elapsed time=', time() - starting_time)

        if device_type == 'ios' and f == '7025':
           #---- Use CLI command to get configuration data from device
           print("Logging to Telnet device")
           starting_time = time()
           print('starting_time',starting_time)
           driver = get_network_driver(device_type)
           optional_args = {'port': f, 'transport': 'telnet'}
           device2 = driver(a, c, d, optional_args=optional_args)
           device2.open()
           print ('---- load file------------')
           config_data_ip2 = device2.device.send_config_from_file(config_file=e)
           print ('---- print file------------')
           print(config_data_ip2)
           device2.close()
           print ('\n---- End get config threading, elapsed time=', time() - starting_time)
        if device_type == 'ios' and f == '7024':
           #---- Use CLI command to get configuration data from device
           print("Logging to Telnet device")
           starting_time = time()
           print('starting_time',starting_time)
           driver = get_network_driver(device_type)
           optional_args = {'port': f, 'transport': 'telnet'}
           device3 = driver(a, c, d, optional_args=optional_args)
           device3.open()
           print ('---- load file------------')
           config_data_ip3 = device3.device.send_config_from_file(config_file=e)
           print ('---- print file------------')
           print(config_data_ip3)
           device3.close()
           print ('\n---- End get config threading, elapsed time=', time() - starting_time)

        if device_type == 'ios' and f == '7023':
           #---- Use CLI command to get configuration data from device
           print("Logging to Telnet device")
           starting_time = time()
           print('starting_time',starting_time)
           driver = get_network_driver(device_type)
           optional_args = {'port': f, 'transport': 'telnet'}
           device4 = driver(a, c, d, optional_args=optional_args)
           device4.open()
           print ('---- load file------------')
           config_data_ip3 = device4.device.send_config_from_file(config_file=e)
           print ('---- print file------------')
           print(config_data_ip3)
           device4.close()
           print ('\n---- End get config threading, elapsed time=', time() - starting_time)

        #session.disconnect()

        return
        

BGP = NapalmMultithreadingTelnet()

def connect_to_device():

    devices = BGP.read_devices('/path/to/file/having/below/6_parameters.txt')
    starting_time = time()

    config_threads_list = []
    for port,device in devices.items():
        a, b, c, d, e, f = device['ipaddr'], device['type'], device['username'], device['password'], device['config_file'], device['port']
        print ('Creating thread for: ', device)
        config_threads_list.append(threading.Thread(target=BGP.config_worker, args=(a,b,c,d,e,f)))

    print ('\n---- Begin get config threading ----\n')
    for config_thread in config_threads_list:
        config_thread.start()

    for config_thread in config_threads_list:
        config_thread.join()

    print ('\n---- End get config threading, elapsed time=', time() - starting_time)

