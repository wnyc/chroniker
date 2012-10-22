from timer import Timer
import time
import logging

logging.basicConfig(level=logging.DEBUG)

def demo_a():
    with Timer(3, 'We do something important') as t:
        time.sleep(2)
        t(1, 'Step #1')
        time.sleep(2)
        t(3, 'Step #2')

def demo_b():
    t = Timer(3, 'foobar')
    time.sleep(2)
    t(1, 'Step #1')
    time.sleep(2)
    t(3, 'Step #2')

def demo_c():
    t = Timer(3, 'foobar')
    time.sleep(2)
    t(1, 'Step #1')
    time.sleep(2)
    t(3, 'Step #2')
    t.done()
    t(1, 'Step #3')

demo_a()
demo_b()
demo_c()
