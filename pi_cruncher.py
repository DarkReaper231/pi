import math
import re
from gmpy2 import mpz, isqrt

DIGITS = 1000000
FILE_NAME = "pi_digits.txt"

def pi_cruncher_bs(n):
    C = 640320  # magic number
    C3_OVER_24 = C**3 // 24
    step = 0
        
    def print_progress():
        nonlocal step
        step += 1
        bar_width = 50
        progress =  step / n * 710  # magic number
        bar_length = progress * bar_width
        blocks = int(progress / 2)
        spaces = 50 - blocks
        bar = '#' * blocks + ' ' * spaces
        if progress > 100:
            print(f"Squaring the result! This may take a while so go get yourself some coffee and be patient...", end='\r', flush=True)
        else:
            print(f"\rDon't interupt! Computing Pi: [{bar}] {progress:.2f}%", end='\r', flush=True)

    def bs(a, b):
        if b - a == 1:
            # direct computation of P(a,a+1), Q(a,a+1) and T(a,a+1)
            if a == 0:
                Pab = Qab = mpz(1)
            else:
                Pab = mpz((6*a-5)*(2*a-1)*(6*a-1))
                Qab = mpz(a*a*a*C3_OVER_24)
            Tab = Pab * (13591409 + 545140134*a)
            if a & 1:
                Tab = -Tab      
        else:
            # recursive computation P(a,b), Q(a,b) and T(a,b)
            m = (a + b) // 2
            Pam, Qam, Tam = bs(a, m)
            Pmb, Qmb, Tmb = bs(m, b)
            Pab = Pam * Pmb  # combine everything
            Qab = Qam * Qmb
            Tab = Qmb * Tam + Pam * Tmb
        print_progress()
        return Pab, Qab, Tab
    
    # how many terms to compute
    digits = math.log10(C3_OVER_24/6/2/6)
    N = int(n/digits + 1)
    P, Q, T = bs(0, N)  # computation of P(0,N) and Q(0,N)
    one_squared = mpz(10)**(2*n)
    sqrtC = isqrt(10005*one_squared)
    pi = str((Q*426880*sqrtC) // T)[1:]  # hack
    
    print("\nComputation finished! Writing to a file...")
    
    result = ""
    for i in range(0, len(pi), 50):
        # can we have faster regexes
        if i + 50 <= len(pi):
            result += re.sub(r'(.{10})', r'\1 ', pi[i:i+50]).strip() + f' : {i + 50}\n'
        else:
            result += re.sub(r'(.{10})', r'\1 ', pi[i:]).strip() + f' : {len(pi)}'
    return '3.\n' + result  # hack

with open(FILE_NAME, mode='w') as file:
    file.write(pi_cruncher_bs(DIGITS))
    print("All done!")
