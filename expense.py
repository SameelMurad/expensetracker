# @TODO: use this as is for a week and note improvements

try:
    with open("expenses.txt", "r") as f:
        expenses = f.read()
        print("Previous expenses:")
        print(expenses)
        total_expense = 0
        for i in expenses.split("\n"):
            if i != "":
                total_expense += int(i)
        print(f"Total expense: {total_expense}")
        
        
except FileNotFoundError:
    print("No previous expenses found")
    
# @TODO: add a note to track the type of purchase along with the amount
exp = input("Type your expense here: ")
print(exp) 

with open("expenses.txt", "a") as f:
    f.write(exp + "\n")