#-*-coding:utf-8-*-

# 필요한 라이브러리를 불러옵니다. 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#센서에 연결한 Trig와 Echo 핀의 핀 번호 설정 
TRIG = 15
ECHO = 14
RED = 17
YELLOW = 27
BLUE = 22
BUZZER = 18
print("Distance measurement in progress")

#Trig와 Echo 핀의 출력/입력 설정 
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.setup(BUZZER,GPIO.OUT)
GPIO.output(BUZZER,GPIO.HIGH)

#Trig핀의 신호를 0으로 출력 
GPIO.output(TRIG, False)
print("Waiting for sensor to settle")
time.sleep(2)

try:
    while True:                  
        GPIO.output(TRIG, True)   # Triger 핀에  펄스신호를 만들기 위해 1 출력
        time.sleep(0.00001)       # 10µs 딜레이 
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO)==0:
            start = time.time()  # Echo 핀 상승 시간 
        while GPIO.input(ECHO)==1:
            stop= time.time()  # Echo 핀 하강 시간 
            
        check_time = stop - start
        distance = check_time * 34300 / 2
        print("Distance : %.1f cm" % distance)
        if distance < 10:
            GPIO.output(RED, 1)
            GPIO.output(YELLOW, 0)
            GPIO.output(BLUE, 0)
            GPIO.output(BUZZER, 0)
        elif distance < 20:
            GPIO.output(RED, 0)
            GPIO.output(YELLOW, 1)
            GPIO.output(BLUE, 0)
            GPIO.output(BUZZER, 0)
            time.sleep(0.1)
            GPIO.output(BUZZER, 1)
        else :
            GPIO.output(RED, 0)
            GPIO.output(YELLOW, 0)
            GPIO.output(BLUE, 1)
            GPIO.output(BUZZER, 1)
        time.sleep(0.4) # 0.4초 간격으로 센서 측정 
        
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()

