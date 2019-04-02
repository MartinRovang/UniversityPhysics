""""

▓█████▄  ██▓ ▄▄▄        ▄████  ███▄    █  ▒█████    ██████ ▄▄▄█████▓ ██▓ ▄████▄    ██████ 
▒██▀ ██▌▓██▒▒████▄     ██▒ ▀█▒ ██ ▀█   █ ▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒▓██▒▒██▀ ▀█  ▒██    ▒ 
░██   █▌▒██▒▒██  ▀█▄  ▒██░▄▄▄░▓██  ▀█ ██▒▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██▒▒▓█    ▄ ░ ▓██▄   
░▓█▄   ▌░██░░██▄▄▄▄██ ░▓█  ██▓▓██▒  ▐▌██▒▒██   ██░  ▒   ██▒░ ▓██▓ ░ ░██░▒▓▓▄ ▄██▒  ▒   ██▒
░▒████▓ ░██░ ▓█   ▓██▒░▒▓███▀▒▒██░   ▓██░░ ████▓▒░▒██████▒▒  ▒██▒ ░ ░██░▒ ▓███▀ ░▒██████▒▒
 ▒▒▓  ▒ ░▓   ▒▒   ▓▒█░ ░▒   ▒ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░▓  ░ ░▒ ▒  ░▒ ▒▓▒ ▒ ░
 ░ ▒  ▒  ▒ ░  ▒   ▒▒ ░  ░   ░ ░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░     ▒ ░  ░  ▒   ░ ░▒  ░ ░
 ░ ░  ░  ▒ ░  ░   ▒   ░ ░   ░    ░   ░ ░ ░ ░ ░ ▒  ░  ░  ░    ░       ▒ ░░        ░  ░  ░  
   ░     ░        ░  ░      ░          ░     ░ ░        ░            ░  ░ ░            ░  
 ░                                                                      ░                 

Diagnostic file with decorator pattern for timing functions.

"""



import time



class Profiler:
    """
    Profiler used for diagnostics, finds the cumulative time and calls for a decorated function
    @timer
    def somefunction():
        ....

    Profiler.showprofile() will output the information.
    """
    functions = {}
    @classmethod
    def add(cls, funcname, time):
        """Finds cumulative time and calls for decorated @timer functions."""
        if funcname in cls.functions:
            cls.functions[funcname][0] += time
            cls.functions[funcname][1] += 1
        else:
            cls.functions[funcname] = [time]
            cls.functions[funcname].append(1)
    
    @classmethod
    def showprofile(cls):
        """Show cumsum and calls of decorated @timer functions."""
        if len(cls.functions) > 0:
            print(f'Cumsum/Calls: {cls.functions}')


def timer(func):
    """Wrapper for timing functions. *args, **kwargs -> take any arguments/ arg1,arg2 and arg3 = value1. arg4 = value2"""
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        total = (end-start)
        Profiler.add(func.__name__, total)
    return wrapper
