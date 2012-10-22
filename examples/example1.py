import chroniker
import time
import logging

logging.basicConfig(level=logging.WARNING)

def demo_a():
    with chroniker.Timer(3, 'We do something important') as t:
        time.sleep(2)
        t(1, 'Step #1')
        time.sleep(2)
        t(3, 'Step #2')

def demo_b():
    t = chroniker.Timer(3, 'foobar')
    time.sleep(2)
    t(1, 'Step #1')
    time.sleep(2)
    t(3, 'Step #2')
    t.done()

def demo_c():
    t = chroniker.Timer(3, 'foobar')
    time.sleep(2)
    t(1, 'Step #1')
    time.sleep(2)
    t(3, 'Step #2')
    t.done()
    try:
        t(1, 'Step #3') 
    except chroniker.TimerFinishedError:
        print "Failed as expected"
    
demo_a()
print
print
demo_b()
print
print

demo_c()
