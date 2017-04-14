'''
Python change the states of all variables (which are assigned at one line) at once.
"State should be updated for all at once    "

Preequisties:
first thing to notice that
python assigns all RHS values to LHS values simultenously ..
a,b=0,1
so a=0 and b=1 will be assign at the same time.

a=1
b=2
a,b=b+1,a+1
a
=>3
b
==>2

this means, a=b+1 and b=a+1 is assign at the same time...

#example of fibonacci:

'''
#normal way
def fib(n):
    x=0
    y=1
    for i in range(n):
        print(x)
        t=y
        y=x+y
        x=t
fib(10)

#Pythonic way
def fib_new(n):
    x,y=0,1
    for _ in range(n):
        print(x)
        x,y=y,x+y

fib_new(10)