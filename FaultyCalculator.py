# We have to fault these three calculations but other calculation will not be affected 
# 45 * 3 = 44 , 56 + 9 = 45, 56/6 = 100

n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
opt = input("Enter your operator {+ , - , * , / }: ")

if opt == "+":
    if n1 == 56 and n2 == 9:
        print("Your answer is 45.")
    else:    
        print("Your answer is ", n1 + n2)
elif opt == "-":
    print("Your answer is ", n1 - n2) 
elif opt == "*":
    if n1 == 45 and n2 == 3:
        print("Your answer is 44.")
    else:    
        print("Your answer is ", n1 * n2)
elif opt == "/":
    if n1 == 56 and n2 == 6:
        print("Your answer is 100")
    else:
        print("Your answer is ", n1 / n2)                       
