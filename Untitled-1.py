
def calculate_categories(salary, saving_percentage, rent_percentage, electricity_percentage):
    saving = salary * saving_percentage
    rent = salary * rent_percentage
    electricity = salary * electricity_percentage
    total = saving + rent + electricity
    remainder = salary - total
    yearly_rent = rent * 12
    yearly_electricity = electricity * 12
    total_salary = salary ** 2
    return saving, rent, electricity, total, remainder, yearly_rent, yearly_electricity, total_salary

def calculate_savings(saving, additional_saving):
    total_saving = saving / additional_saving
    return total_saving

def main():
    
    monthlydata = []

    while True:

       salary = float(input("Enter your salary for the month: "))
       month = input("Enter the name of the month: ")
       saving_percentage = float(input("Enter the percentage of your salary you want to save: "))
       rent_percentage = float(input("Enter the percentage of your salary you want to spend on rent: "))
       electricity_percentage = float(input("Enter the percentage of your salary you want to spend on electricity: "))
       additional_saving = 50
       saving, rent, electricity, total, remainder, yearly_rent, yearly_electricity, total_salary = calculate_categories(salary, saving_percentage, rent_percentage, electricity_percentage)
       total_saving = calculate_savings(saving, additional_saving)

       monthdata = {
            "Month": month,
            "Salary": salary,
            "Saving": saving,
            "Rent": rent,
            "Electricity": electricity,
            "Total": total,
            "Remainder": remainder,
            "Yearly Rent": yearly_rent,
            "Yearly Electricity": yearly_electricity,
            "Total Salary": total_salary,
            "Additional Savings Amount": additional_saving,
            "Additional Savings Remainder": total_saving
        }

       monthlydata.append(monthdata)
       month2 = input("Do you want to enter another month? (yes/no): ")
       if month2 == "no": 
           break
       
    for monthdata in monthlydata:
       
        print(f"\nIn {monthdata['Month']}, you have allocated the following amounts:")
        print(f"Savings: ${monthdata['Saving']}")
        print(f"Rent: ${monthdata['Rent']}")
        print(f"Electricity: ${monthdata['Electricity']}")
        print(f"\nThe total amount you spend on savings, rent, and electricity combined is: ${monthdata['Total']}")
        print(f"\nAfter these expenses, Nabiha has ${monthdata['Remainder']} left.")
        print(f"\nNabiha's yearly rent would be ${monthdata['Yearly Rent']} and yearly electricity cost would be ${monthdata['Yearly Electricity']}.")
        print(f"\nNabiha's total salary for the month raised to the power of 2 is: ${monthdata['Total Salary']}")
        print(f"\nIf Nabiha saves an additional ${monthdata['Additional Savings Amount']} each month, she would have ${monthdata['Additional Savings Remainder']} saved.")

main()