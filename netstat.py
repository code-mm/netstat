#!/usr/bin/env python
import time
from decimal import *

interface = 'wlp2s0'

last_rx = 0
last_tx = 0

while(True):
    # open file handlers
    f_rx = open('/sys/class/net/' + interface + '/statistics/rx_bytes', 'r')
    f_tx = open('/sys/class/net/' + interface + '/statistics/tx_bytes', 'r')

    # read from file and remove newline
    rx = int(f_rx.read().replace('\n', ''))
    tx = int(f_tx.read().replace('\n', ''))

    # compare with values from last run and return the difference
    current_rx = rx - last_rx
    current_tx = tx - last_tx

    # rx output
    if current_rx <= 1024: # bytes
        print('rx' + str(round(current_rx/(1024), 2)) + 'B/s')
    elif current_rx <= 1024*1024: # kilo
        print('rx' + str(round(current_rx/(1024*1024), 2)) + 'KB/s')
    elif current_rx > 1024*1024: # mega
        print('rx' + str(round(current_rx/(1024*1024*1024), 2)) + 'MB/s')

    # tx output
    if current_tx <= 1024: # bytes
        print('tx' + str(round(current_tx/(1024), 2)) + 'B/s')
    elif current_tx <= 1024*1024: # kilo
        print('tx' + str(round(current_tx/(1024*1024), 2)) + 'KB/s')
    elif current_tx > 1024*1024: # mega
        print('tx' + str(round(current_tx/(1024*1024*1024), 2)) + 'MB/s')

    # make current to last for next cycle
    last_rx = rx
    last_tx = tx

    # sleep for a second
    time.sleep(1)

