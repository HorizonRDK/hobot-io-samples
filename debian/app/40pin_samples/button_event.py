#!/usr/bin/env python3

import Hobot.GPIO as GPIO
import time

# 定义使用的GPIO通道：
# 36号作为输出，可以点亮一个LED
# 38号作为输入，可以接一个按钮
led_pin = 36 # BOARD 编码 36
but_pin = 38 # BOARD 编码 38

# 禁用警告信息
GPIO.setwarnings(False)

def main():
    # 设置管脚编码模式为硬件编号 BOARD
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)  # LED pin set as output
    GPIO.setup(but_pin, GPIO.IN)  # button pin set as input

    # Initial state for LEDs:
    GPIO.output(led_pin, GPIO.LOW)

    print("Starting demo now! Press CTRL+C to exit")
    try:
        while True:
            print("Waiting for button event")
            GPIO.wait_for_edge(but_pin, GPIO.FALLING)

            # event received when button pressed
            print("Button Pressed!")
            GPIO.output(led_pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led_pin, GPIO.LOW)
    finally:
        GPIO.cleanup()  # cleanup all GPIOs

if __name__ == '__main__':
    main()
