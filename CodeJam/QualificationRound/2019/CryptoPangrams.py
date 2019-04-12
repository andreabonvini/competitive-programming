
import sys

def EuclideanAlgorithm(a, b):
    # Efficient way to find the GCD of two numbers a & b
    while b:
        a, b = b, a % b
    return a

T = int(sys.stdin.readline().strip())

for case in range(T):
    N,L = list(map(int,sys.stdin.readline().strip().split()))
    ct = list(map(int,sys.stdin.readline().strip().split()))  # ct : cipher text
    plain_text = [-1 for i in range(len(ct)+1)]
    
    # Here we find all the non-ambiguous values in our plain_text
    for i in range(len(ct)-1):
        if ct[i] == ct[i+1]: # Ambiguous --> pass
            pass
        else:
            plain_text[i+1] = EuclideanAlgorithm(ct[i],ct[i+1])
    
    
    # Check for ambiguities at the tail
    tmp = len(plain_text)-1
    flag = False
    if plain_text[tmp] == -1:
        flag = True
        while plain_text[tmp] == -1:
            tmp-=1
        fix_from_here = tmp
        
    # Fix ambiguities at the tail (if necessary)
    if flag:
        for i in range(fix_from_here,len(plain_text)-1):
            plain_text[i+1] = ct[i]//plain_text[i]
    
    # Fix last letter of the message
    if not flag:
        cmmn_prime = EuclideanAlgorithm(ct[-2],ct[-1])
        plain_text[-1] = ct[-1]//cmmn_prime
    
    # Back-Propagate to fix ambiguities (and the first letter of the message)
    while tmp > 0:
        if plain_text[tmp-1] == -1:
            plain_text[tmp-1] = ct[tmp-1] // plain_text[tmp]
        tmp-=1
    
   
    # Convert primes to letters
    alpha_set = list(set(plain_text))
    alpha_set.sort()
    alpha_dict = {}
    for i in range(26):
        alpha_dict[alpha_set[i]] = chr(ord('A')+i)
    plain_text = list(map(lambda x : alpha_dict[x],plain_text))
    plain_text = ''.join(plain_text)
    
    # Print plain_text
    print("Case #{}: {}".format(case+1,plain_text))