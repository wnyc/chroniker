# Chroniker

At WNYC we use the Chroniker module in places were we need a small
amount of performance profiling and the occasional warning that
something is taking longer than we'd like, but don't want the overhead
and complexity of a full fledged profiling tool.  

## Components

### Timer

Use a timer when you need to know if a section of code, or subsections
within it, take more than a certain amount of time.

There are two ways to use Timer.  The first, and recommended way, is to use a Timer object within a with statement as follows

````python
with chronkier.Timer(5, 'Message') as t:# 5 seconds
     do_something()
     t(1, 'msg describing do_something')
     do_something_else()
     t(0.5, 'msg describing do_something_else')
     do_nothing_special() 
````

Each call to Timer emits a log entry; in the above example three entries are logged, two for each of the calls to the timer object and one when the timer is cleaned up.  Timer logs to WARNING when late and DEBUG when online.

### Working example


Lets suppose you had code that looked like this
````python

def do_nothing():
    foobar()
    gronkulate()
````

Suppose you want to know if overall foobar and gronkulate take more
than 1 second, or if either foobar or gronkulate individually take
more than 3/4 of a second.

First, import chroniker.

````python
import chroniker
import logging

logging.basicConfig(level=logging.WARNING)

def do_nothing():
    foobar()
    gronkulate
```

Now instrument do_nothing as ...

````python
import chroniker


def do_nothing():
    with chroniker.Timer(1, 'We do nothing important here') as t:
        foobar()
	t(0.75, 'Foobar is late, we might have trouble gronkulating')
    	gronkulate
	t(0.75, 'Gronkulate was slow.  Oh no!')
```

Now lets provide some definitions for foobar and gronkulate to make this code work


````python
import chroniker
import time

def do_nothing():
    with chroniker.Timer(1, 'We do nothing important here') as t:
        foobar()
	t(0.75, 'Foobar is late, we might have trouble gronkulating')
    	gronkulate
	t(0.75, 'Gronkulate was slow.  Oh no!')

def foobar():
    time.sleep(1)

def gronkulate():
    time.sleep(0.1)

```

### Without with

For those allergic to the with statement there are two other ways of working with chroniker.Timer.

Timer can be closed explicitly
by invocation of Timer.done.   The initial example would be written as:

````python

t = chroniker.Timer(5, 'Message') # 5 seconds
do_something()
t(1, 'msg describing do_something')
do_something_else()
t(0.5, 'msg describing do_something_else')
do_nothing_special() 
d.done
````

You can also allow the Timer object to be garbage collected; hopefully this will happen sooner than later and not give you too many false positives:

````python
def do_nothing():
    t = chroniker.Timer(5, 'Message') # 5 seconds
    do_something()
    t(1, 'msg describing do_something')
    do_something_else()
    t(0.5, 'msg describing do_something_else')
    do_nothing_special() 
````