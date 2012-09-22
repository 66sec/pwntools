# top-level imports
import struct, pwn, sys, subprocess, re, time
from socket import htons, inet_aton, inet_ntoa, gethostbyname
from os import system
from time import sleep
import log

# conversion functions
def p8(x):
    return struct.pack('<B', x & 0xff)

def p8b(x):
    return struct.pack('>B', x & 0xff)

def p16(x):
    return struct.pack('<H', x & 0xffff)

def p16b(x):
    return struct.pack('>H', x & 0xffff)

def p32(x):
    return struct.pack('<I', x & 0xffffffff)

def p32b(x):
    return struct.pack('>I', x & 0xffffffff)

def p64(x):
    return struct.pack('<Q', x & 0xffffffffffffffff)

def p64b(x):
    return struct.pack('>Q', x & 0xffffffffffffffff)

def u8(x):
    return struct.unpack('<B', x)[0]

def u8b(x):
    return struct.unpack('>B', x)[0]

def u16(x):
    return struct.unpack('<H', x)[0]

def u16b(x):
    return struct.unpack('>H', x)[0]

def u32(x):
    return struct.unpack('<I', x)[0]

def u32b(x):
    return struct.unpack('>I', x)[0]

def u64(x):
    return struct.unpack('<Q', x)[0]

def u64b(x):
    return struct.unpack('>Q', x)[0]

def dehex(s):
    return s.decode('hex')

def enhex(s):
    return s.encode('hex')

# network utils
def ip (host):
    return struct.unpack('I', inet_aton(gethostbyname(host)))[0]

def get_interfaces():
    d = subprocess.check_output('ip -4 -o addr', shell=True)
    ifs = re.findall(r'^\S+:\s+(\S+)\s+inet\s+([^\s/]+)', d, re.MULTILINE)
    return [i for i in ifs if i[0] != 'lo']

# Stuff
def pause(n = None):
    try:
        if n is None:
            log.info('Paused (press enter to continue)')
            raw_input('')
        else:
            log.info('Continueing in ')
            for i in range(n, 0, -1):
                log.trace('%d... ' % i)
                time.sleep(1)
            log.trace('\n')
    except KeyboardInterrupt:
        log.trace('\n')
        log.warning('Interrupted\n')
        exit(1)

def die(s = None, e = None, error_code = -1):
    if s:
        log.failure('FATAL: ' + s + '\n')
    if e:
        log.failure('The exception was:\n' + str(e) + '\n')
    exit(error_code)