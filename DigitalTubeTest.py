import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

# a, 33  b, 31  c, 36  d, 38
# e, 40  f, 35  g, 27  ., 32

# 0 -> 31, 33, 35, 36, 38, 40
# 1 -> 31, 36
# 2 -> 31, 33, 37, 38, 40
# 3 -> 31, 33, 37, 36, 38
# 4 -> 31, 35, 37, 36
# 5 -> 33, 35, 37, 36, 38
# 6 -> 33, 35, 37, 36, 38, 40
# 7 -> 31, 33, 36
# 8 -> 31, 33, 35, 37, 36, 38, 40
# 9 -> 31, 33, 35, 37, 36, 38

nums = [{31, 33, 35, 36, 38, 40},
       {31, 36},
       {31, 33, 37, 38, 40},
       {31, 33, 37, 36, 38},
       {31, 35, 37, 36},
       {33, 35, 37, 36, 38},
       {33, 35, 37, 36, 38, 40},
       {31, 33, 36},
       {31, 33, 35, 37, 36, 38, 40},
       {31, 33, 35, 37, 36, 38}
       ]
def LED():
    while True:
        GPIO.output(11, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(11, GPIO.LOW)
        time.sleep(1)

def DigitalTube():
    while True:
        for num in nums:
            for on_lights in num:
                GPIO.output(on_lights, GPIO.HIGH)
            for off_lights in nums[8] - num:
                GPIO.output(off_lights, GPIO.LOW)
            time.sleep(2)



t1 = threading.Thread(target = LED)
t2 = threading.Thread(target = DigitalTube)
t1.start()
t2.start()
t1.join()
t2.join()




