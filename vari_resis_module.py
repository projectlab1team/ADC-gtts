import sys
#import time
from time import time, strftime, localtime, sleep
from pymata4 import pymata4
#import thingspeak

#gtts
#from gtts import gTTS
#from playsound import playsound

"""
This file demonstrates analog input using both callbacks and
polling. Time stamps are provided in both "cooked" and raw form
"""
#channel_id = 1933072 # put here the ID of the channel you created before
#write_key = 'CRA2BUB6VVIZTS75' # update the "WRITE KEY"

# Setup a pin for analog input and monitor its changes
ANALOG_PIN = 2  # arduino pin number
POLL_TIME = 2  # number of seconds between polls

# Callback data indices
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3

#tts_vari_ris_module = gTTS(text="adc값이 thingspeak cloud에 upload 되었습니다.", lang='ko')
#tts_vari_ris_module.save("tts_vari_ris_module.mp3")
#

def the_callback(data):
    """
    A callback function to report data changes.

    :param data: [pin_mode, pin, current_reported_value,  timestamp]
    """
    #print(data)
#     formatted_time = strftime('%Y-%m-%d %H:%M:%S', localtime(data[CB_TIME]))
#     print(f'Analog Call Input Callback: pin={data[CB_PIN]}, '
#           f'Value={data[CB_VALUE]} Time={formatted_time} '
#           f'(Raw Time={data[CB_TIME]})')


def analog_in(my_board, pin):
    my_board.set_pin_mode_analog_input(pin_number = pin, callback=the_callback, differential=0)
    #channel = thingspeak.Channel(id=channel_id, write_key=write_key)
    #changed = False
    # run forever waiting for input changes
    try:
        while True:
            sleep(0.1) #sleep(POLL_TIME)
            # retrieve both the value and time stamp with each poll
            value, _ = my_board.analog_read(pin = pin) #value, time_stamp = my_board.analog_read(pin = pin)
            # format the time stamp
            #formatted_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time_stamp))
            print(
               # f'Reading latest analog input data for pin {pin} = {value} change received on {formatted_time} '
                f'Reading current analog value = {value} ')#change received on {formatted_time} '
                #f'(raw_time: {time_stamp})')
            #response = channel.update({'field1': value})
            #playsound("tts_vari_ris_module.mp3")
    except KeyboardInterrupt:
        my_board.shutdown()
        sys.exit(0)


# instantiate pymata4
board = pymata4.Pymata4()

analog_in(my_board = board, pin = ANALOG_PIN)