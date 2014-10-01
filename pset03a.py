"""
In this problem, you are asked to find the amount of radiation a person is exposed to during some period of time.

To complete this function you'll need to know what the value of the radioactive decay curve is at various points. There is a function f that will be defined for you that you can call from within your function that describes the radioactive decay curve for the problem.
"""

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    n = 0
    count = 0
    if stop <= start:
        return count
    else:
        return (f(start) * step) + radiationExposure((start + (step * (n+1))), stop, step)
