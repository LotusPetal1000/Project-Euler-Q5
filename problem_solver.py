#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Project Euler question no 5


def prime(num): # returns boolean
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)

    if factors == [1, num]:
        return True
    else:
        return False

def convert_to_prime(num): # returns list of prime factors
    prime_factors = []

    for i in range(1, num+1):
        while num % i == 0:
            if prime(i):
                prime_factors.append(i)
                num = num/i
            else:
                break
    if prime_factors:
        return prime_factors
    else:
        return None

def freq_counter(list): # returns a dictionary with each prime factor and its frequency

    freq_counter = {}
    
    for i in list:
        if i in freq_counter:
            freq_counter[i] += 1
        else:
            freq_counter[i] = 1
    
    return freq_counter

def lcm(factor_freq_dict : dict): # returns the lcm using the freq of each prime factor

    lcm = 1

    for key, value in factor_freq_dict.items():
        lcm *= key**value
    
    return lcm

spread = list(range(2, 21))
prime_spread = [convert_to_prime(i) for i in spread] # now we have the prime factors of the range
overall_freq_dict = {}

for prime_list in prime_spread:

    freq_dict = freq_counter(prime_list)

    for key, value in freq_dict.items():

        if not overall_freq_dict.get(key):
            overall_freq_dict.update({key:value})

        elif overall_freq_dict.get(key) < value:
            overall_freq_dict.update({key:value})
# dictionary with highest frequency of each prime factor ready

lcm = lcm(overall_freq_dict)

print(lcm)
