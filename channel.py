import serial
import time
seri = serial.Serial('/dev/ttyUSB0', 9600)
if (seri.isOpen() == False):
    seri.open()
k = 0
try:
    f_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    tab = '   '
    name = input("please put your name:")
    jg = open(r'/home/pi/date.log', 'a')
    jg.write(f_time + tab + name + '\n')
    jg.close
    while True:
        seri.write('\xFE\x18\x03\x03\x04\x00\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x01\x02\x03\x04\x01\x00')
        time.sleep(0.3)
        count = seri.inWaiting()
        print ("------------")
        k = k+1
        print(k)
        print (count)
        if count > 0:
            data = seri.read(count)
            if count == 36:
                print ('true')
                alist = list(data)
                result = str('%x'%ord(alist[29]))
                str1 = str('%x'%ord(alist[30]))
                str2 = str('%x'%ord(alist[31]))
                str3 = str('%x'%ord(alist[32]))
                str4 = str('%x'%ord(alist[33]))
                print 'chan1:', str1
                print 'chan2:', str2
                print 'chan3:', str3
                print 'chan4:', str4
                print 'result:', result
                jg = open(r'/home/pi/date.log', 'a')
                count = str(count)
                jg.write(count)
                jg.write(tab)
                jg.write(str1 + tab)
                jg.write(str2 + tab)
                jg.write(str3 + tab)
                jg.write(str4 + tab)
                jg.write(result + '\n')
                jg.close
            else:
                jg = open(r'/home/pi/date.log', 'a')
                count = str(count)
                jg.write(count)
                jg.write(tab)
                jg.write('false'+ '\n')
                jg.close
                print ('false')
        print ("------------")
        time.sleep(1)
except KeyboardInterrupt:
    seri.close()
