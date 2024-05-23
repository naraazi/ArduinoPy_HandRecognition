import pyfirmata

comport = 'COM7'  # --  modify the serial port here
board = pyfirmata.Arduino(comport)

led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
led_4 = board.get_pin('d:11:o')
led_5 = board.get_pin('d:12:o')


def led(finger_up):
    if finger_up == [0, 0, 0, 0, 0]:  # -- no finger up
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif finger_up == [0, 1, 0, 0, 0]:  # -- index finger up
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif finger_up == [0, 1, 1, 0, 0]:  # -- middle finger up
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif finger_up == [0, 1, 1, 1, 0]:  # -- ring finger up
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif finger_up == [0, 1, 1, 1, 1]:  # -- little finger up
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif finger_up == [1, 1, 1, 1, 1]:  # -- thumb up
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
