while True:
    x,y = map(int,input('what are ur 2 numbers: ').split())
    operation = input('what operation u want(in words) or write exit to stop it: ').lower()
    if operation=='multiplication':
        def multiply(number1,number2):
            return number1*number2
        print('ur result: '+str(multiply(x,y)))
    elif operation=='addition':
        def addition(number1,number2):
            result = number1+number2
            return result
        print('ur result: '+str(addition(x,y)))
    elif operation=='subtraction':
        def subtraction(number1,number2):
            result = number1-number2
            return result
        print('ur result: '+str(subtraction(x,y)))
    elif operation=='division':
        try:
            def division(number1,number2):
                result = number1/number2
                return result
            print('ur result: '+str(division(x,y)))
        except ZeroDivisionError as e:
            print(e)
            print('division by zero is not possible!')
    elif operation=='exit':
        print('ok, lets stop it for now')
        break
    else:
        print('dont waste my time')