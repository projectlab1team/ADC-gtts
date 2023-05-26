import sys
import time
from pymata4 import pymata4
"""
This file demonstrates analog input using both callbacks and polling. Time stamps are provided in both "cooked" and raw form
"""

# Setup a pin for analog input and monitor its changes
ANALOG_PIN = 2  # arduino pin number
POLL_TIME = 0.5  # number of seconds between polls

# Callback data indices
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3

def the_callback(data):
    """
    A callback function to report data changes.
    :param data: [pin_mode, pin, current_reported_value,  timestamp]
    """
    #formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[CB_TIME]))
#     print(f'Analog Call Input Callback: pin={data[CB_PIN]}, '
#           f'Value={data[CB_VALUE]} ' )#Time={formatted_time} '
          #f'(Raw Time={data[CB_TIME]})')

def analog_in(my_board, pin, callback=None):
    """
    This function establishes the pin as an analog input. Any changes on this pin will
    be reported through the call back function.
    Every 5 seconds the last value and time stamp is polled and printed.
    Also, the differential parameter is being used. The callback will only be called when there is
    difference of 5 or more between the current and last value reported.
    :param my_board: a pymata4 instance
    :param pin: Arduino pin number
    """
    my_board.set_pin_mode_analog_input(pin, callback=callback, differential=0)
    # run forever waiting for input changes
    try:
        while True:
            time.sleep(POLL_TIME)
            # retrieve both the value and time stamp with each poll
            value, time_stamp = board.analog_read(pin)
            # format the time stamp
#             formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_stamp))
            print(f'Reading latest analog input data {value} change received on {time_stamp}')
                 #f'(raw_time: {time_stamp})')
    except KeyboardInterrupt:
        my_board.shutdown()
        sys.exit(0)

# instantiate pymata4
board = pymata4.Pymata4()
analog_in(board, ANALOG_PIN,the_callback)
