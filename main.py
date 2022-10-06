import sys
import serial.tools.list_ports
import time
import threading
import binascii

ser = serial.Serial()

arduino_port = None

var = ""


def main():
    setSerial('COM3', 9600, .1)
    startSerial()
    while True:
        if ser.is_open:
            packet = ser.readline()
            print(packet.decode("utf"))


def setSerial(port, boud, timeout):
    ser.boudrate = None
    ser.port = None
    ser.timeout = None

    if boud <= 0 or timeout < 0:
        raise ValueError

    ser.timeout = timeout

    ports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
    print(ports)
    print(len(ports))

    for gate in ports:
        if port in gate:
            ser.port = gate[0]

    if ser.port is None:
        raise AttributeError


def startSerial():
    if ser.is_open:
        ser.close()
        ser.open()
        print('already opened, reopening')
    else:
        ser.open()
        print('opening serial')


if __name__ == "__main__":
    main()
