#!/usr/bin/env python

def consumer():
    r = 'first'
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] Consuming %s ...' % n )
        r = ' %d 200 OK' % n

def produce(c):
    c.send(None)
    n = 0
    while n < 12 :
        n += 1
        print('[procuder] Producing %s ...' % n)
        r = c.send(n)
        print('procuder Consumer return: %s ' % r)
    c.close()

c = consumer()
produce(c)
