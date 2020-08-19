# function return type is fuction 
def func(wrapper_func):
    def inner_fuction():
        print("this is inner method")   
        return wrapper_func()    
    return inner_fuction

@func  # this is similar to func(displaying) is called decorator
def displaying():
    print("disply function")

displaying()
#data = func(displaying)
#print(data)