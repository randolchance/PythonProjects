# PROJECT EULER PROBLEM 25 - 1000-digit Fibonacci Number



from memoise import Memoise

@Memoise
def fib(n):
    if n == 1 or n == 2:
        return(1)
    return(fib(n-2)+fib(n-1))



for i in range(1,10000):
    len_fib = len(str(fib(i)))
    if len_fib == 1000:
        print(i,len_fib)
        break
    
