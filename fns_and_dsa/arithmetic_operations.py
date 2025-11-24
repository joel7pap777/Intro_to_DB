def perform_operation(num1,num2,operator):
    if(operator=='add'):
        return num1+num2
    elif(operator=='subtract'):
        return num1-num2
    elif(operator=='multiply'):
        return  num1*num2
    elif(operator=='divide'):
        if(num2==0):
            return'cannot divide by 0'
        else:
            return num1/num2

    