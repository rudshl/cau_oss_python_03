def arithmetic_ops(op) :
    num1 = int(input("input 1st number : "))
    num2 = int(input("input 2nd number : "))
    return num1, num2, op(num1, num2)

# +, -는 함수로 정의
def add(x, y) : return x + y
def sub(x, y) : return x - y


while True :
    op = input("input operation : ")
    if  op == "end" :
        break # 반복을 종료
    elif op == "+" :
        num1, num2, ret = arithmetic_ops(add)
    elif op == "-" :
        num1, num2, ret = arithmetic_ops(sub)
    elif op == "*" :
        num1, num2, ret = arithmetic_ops(lambda x, y : x * y)
    elif op == "/" :
        num1, num2, ret = arithmetic_ops(lambda x, y : x / y)
    elif op == "%" :
        num1, num2, ret = arithmetic_ops(lambda x, y : x % y)
    else :
        print("Invalid operation")
        continue
    print(f"{num1} {op} {num2} = {ret}")

print("Exit program")