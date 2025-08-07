# # #program to check whether the new provided through the link is true or false
# # import requests
# # def check_url(url):
# #     try:
# #         response = requests.get(url)
# #         if response.status_code == 200:
# #             return True
# #         else:
# #             return False
# #     except requests.exceptions.RequestException as e:
# #         print(f"An error occurred: {e}")
# #         return False    
    

#write a program to build a simple calculator that can perform addition, subtraction, multiplication, and division
def calculator():
    print("Welcome to the simple calculator")
    print("Select operation:")
    print("1.Addition")
    print("2.Substration")
    print("3.Multiplication")
    print("4.Division")

    choice=input("Enter choice(1/2/3/4):")
    if choice in ('1','2','3','4'):
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))

        if choice=='1':
            print(f"{num1}+{num2}={num1+num2}")
        elif choice=='2':
            print(f"{num1}-{num2}={num1-num2}")
        elif choice=='3':
            print(f"{num1}*{num2}={num1*num2}")
        elif choice=='4':
            if num2!=0:
                print(f"{num1}/{num2}={num1/num2}")
            else:
                print("Error! Division by zero")
        else:
            print("Enter a valid choice:")

n=calculator()
print(n)



