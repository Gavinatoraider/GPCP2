# Gavin Pierce, Debugging notes

import trace
import sys
tracer = trace.Trace(count=False, trace=True)

def trace_calls(frame ,event ,arg):

    if event == 'call': #when the function is called
        print(f'calling function: {frame.f_code.co_name}')
    elif event == 'line': #when a new line of code happens
        print(f'Exicuting line {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return':
        print(f'{frame.f_code.co_name} returned {arg}')    
    elif event == 'exeptions': #triggered when there is an exeption
        print(f'exception in {frame.f_code.co_name}: {arg}')

        return trace_calls

sys.settrace(trace_calls)

#what is tracing?

def sub(numone, numtwo):
    return numone - numtwo

def add(numone, numtwo):
    print(sub(numone,numtwo))
    return numone + numtwo

print(add(5,2))

#tracer.run('add(8,9)')

#basic tracing command
#python -m trace --trace debuging_notes\main.py

"""
    --trace (displays lines as excuted)
    --count (displays the number if times executed)
    --listfuncs (displaus functions used in the program)
    --trackcalls (displays relationships betwwen functions)
"""

#what are some ways we can debug by tracing?
    #find where the errors are so that you dont have to change the code.


#How do you acess the debuger in python
    #Click the debugger one the left
    #F5 key
    #drop down next to run button.

#what is testing?
    #running your code to make sure it works as required

#what are boundry cinsitions?
    #Checks the entries most llkely to be wrong

#how do you handle when users give strange inputs
    #conditionals and loops