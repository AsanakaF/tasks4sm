def cl():
    def inpx():
        try:
            x = float(input('Enter first number: '))
        except:
            print('its not a number!')
            return inpx()
        return x
    def inpa():
        try:
            a = float(input('Enter second number: '))
        except:
            print('its not a number')
            return inpa()
        return a

    def inpa2():
        try:
            a2 = float(input('Enter second number: '))
        except:
            print('its not a number')
            return inpa2()
        return a2
    x = inpx()
    op = input('enter operation: ')
    a = inpa()

    if op == '+':
        cum = x + a
        print('{} + {} = {} '.format(x, a, cum))
        op2 = input('enter operation: ')
        a2 = inpa2()
        if op2 == '+':
            cum2 = cum + a2
            print('{} + {} = {} '.format(cum, a2, cum2))
        elif op2 == '-':
            cum2 = cum - a2
            print('{} - {} ={} '.format(cum, a2, cum2))
        elif op2 == '*':
            cum2 = cum * a2
            print('{} * {} ={} '.format(cum, a2, cum2))
        elif op2 == '/':
            cum2 = cum / a2
            print('{} / {} ={} '.format(cum, a2, cum2))


    elif op == '-':
        cum = x - a
        print('{} - {} = {} '.format(x, a, cum))
        op2 = input('enter operation: ')
        a2 = inpa2()
        if op2 == '+':
            cum2 = cum + a2
            print('{} + {} = {} '.format(cum, a2, cum2))
        elif op2 == '-':
            cum2 = cum - a2
            print('{} - {} ={} '.format(cum, a2, cum2))
        elif op2 == '*':
            cum2 = cum * a2
            print('{} * {} ={} '.format(cum, a2, cum2))
        elif op2 == '/':
            cum2 = cum / a2
            print('{} / {} ={} '.format(cum, a2, cum2))

    elif op == '*':
        cum = x * a
        print('{} * {} = {} '.format(x, a, cum))
        op2 = input('enter operation: ')
        a2 = inpa2()
        if op2 == '+':
            cum2 = cum + a2
            print('{} + {} = {} '.format(cum, a2, cum2))
        elif op2 == '-':
            cum2 = cum - a2
            print('{} - {} ={} '.format(cum, a2, cum2))
        elif op2 == '*':
            cum2 = cum * a2
            print('{} * {} ={} '.format(cum, a2, cum2))
        elif op2 == '/':
            cum2 = cum / a2
            print('{} / {} ={} '.format(cum, a2, cum2))

    elif op == '/':
        cum = x / a
        print('{} / {} = {} '.format(x, a, cum))
        op2 = input('enter operation: ')
        a2 = inpa2()
        if op2 == '+':
            cum2 = cum + a2
            print('{} + {} = {} '.format(cum, a2, cum2))
        elif op2 == '-':
            cum2 = cum - a2
            print('{} - {} ={} '.format(cum, a2, cum2))
        elif op2 == '*':
            cum2 = cum * a2
            print('{} * {} ={} '.format(cum, a2, cum2))
        elif op2 == '/':
            cum2 = cum / a2
            print('{} / {} ={} '.format(cum, a2, cum2))

    else:
        print('Enter operation!')
        cl()
    ag()
def ag():
        cn=input('y or n: ')
        if cn == 'y':
            cl()
        elif cn == 'n':
            print('bb')
        else:
            ag()

cl()
