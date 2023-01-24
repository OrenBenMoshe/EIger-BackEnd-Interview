# BackEnd interview Code Test
# First Question
def priceCheck(products: list[str], productPrices: list[float], productSold: list[str], soldPrice: list[float]):
    productsPricesDic = {}
    errorCounter = 0
    if len(productSold) != len(soldPrice):
        print("Something Went wrong the productSold list are not equal to soldPrice list")
        return
        # Should exit here but there is no such a request in the question
    if len(products) == len(productPrices):
        for x in range(len(products)):
            productsPricesDic[products[x]] = productPrices[x]
        for x in range(len(productSold)):
            if soldPrice[x] != productsPricesDic.get(productSold[x]):
                errorCounter += 1
    else:
        print("Something Went wrong the products list are not equal to productPrices list")
        return
        # Should exit here but there is no such a request in the question

    return errorCounter


# Second Question is written in SQL language
# Select the department name and count the employees in each department
# Use left join so all departments are listed even if there are no employees
# Group the results by department name
# Order the results by employee count in descending order, and by department name in ascending order
'''
SELECT Department.NAME as department_name, COUNT(Employee.ID) as employee_count
FROM Department
LEFT JOIN Employee ON Employee.DEPT_ID = Department.ID
GROUP BY Department.NAME
ORDER BY employee_count DESC, Department.NAME ASC;
'''

# Third Question


def sumOfDigits(num: int):
    if num == 0:
        return 0
    currentDigit = num % 10
    return currentDigit + sumOfDigits(num//10)

# Bonus Question


def RecursiveNumeric(num: int, maxValue: int, maxCounter: int):
    if num == 0:
        print(f"The max value is {maxValue} it appears {maxCounter} times")
    elif num == maxValue:
        maxCounter += 1
        RecursiveNumeric(
            int(input("Please enter a number enter 0 to Exit.\n")), maxValue, maxCounter)
    elif num > maxValue:
        maxValue = num
        maxCounter = 1
        RecursiveNumeric(
            int(input("Please enter a number enter 0 to Exit.\n")), maxValue, maxCounter)
    else:
        RecursiveNumeric(
            int(input("Please enter a number enter 0 to Exit.\n")), maxValue, maxCounter)
