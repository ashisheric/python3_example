import time

def outer_function(wrapper_func):
    def inner_function():
        start_time = time.time()
        rv = wrapper_func()
        end_time = time.time() - start_time  
        print('ran in {}'.format(end_time))      
        return rv

    return inner_function

@outer_function
def timer1():
    for _ in range(1000000):
        pass

@outer_function
def timer2():
    for _ in range(100000):
        pass

timer1()
timer2()