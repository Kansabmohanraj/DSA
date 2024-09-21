def sum_of_digits(num):
    result = 0
    while num > 0:
        result += num % 10  
        num //= 10   
    if(result==6):
        return "yes"
    return "no"       
    return result

print(sum_of_digits(123)) 

def calculate_total_salary(base_salary, leave_deduction, extra_work_bonus):
    total_salary = base_salary
    
    total_salary -= leave_deduction
    
    total_salary += extra_work_bonus
    
    return total_salary

print(calculate_total_salary(12000,1000,700))

while True:
    user_input = input("Type 'exit' to stop the loop: ")
    if user_input == 'exit':
        print("Loop has been terminated.")
        break
    print("You typed:", user_input)
