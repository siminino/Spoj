
def life_main():
    life = [1,2,4,6,28,42,88]
    result = ''
    for n in life:
        result += '%d\n'%n
        if n == 42:
            return result
    
    
