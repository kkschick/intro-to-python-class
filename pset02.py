"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance.
Finally, print out the total amount paid that year and the remaining balance at the end of the year.

The code you paste into the following box should not specify the values for the variables balance, annualInterestRate, or monthlyPaymentRate - our test code will define those values before testing your submission.
"""

month = 0
totalPay = 0
monthlyInterestRate = annualInterestRate / 12.0
while month <12:
    minPay = monthlyPaymentRate * balance
    unpayBal = balance - minPay
    totalPay += minPay
    balance = unpayBal + (monthlyInterestRate * unpayBal)
    month += 1
    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(minPay,2)))
    print('Remaining balance: ' + str(round(balance,2)))
print('Total paid: ' + str(round(totalPay,2)))
print(' Remaining balance: ' + str(round(balance,2)))


"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year.

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay.

The code you paste into the following box should not specify the values for the variables balance or annualInterestRate - our test code will define those values before testing your submission.
"""

initBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
month = 0
minPay = 10
def calculate(month, balance, minPay, monthlyInterestRate):
    while month <12:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance
while calculate(month, balance, minPay, monthlyInterestRate) > 0:
    balance = initBalance
    minPay +=10
    month = 0
    calculate(month, balance, minPay, monthlyInterestRate)
print('Lowest Payment: ' + str(minPay))


"""
Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.

The code you paste into the following box should not specify the values for the variables balance or annualInterestRate - our test code will define those values before testing your submission.
"""

initBalance = balance
monthlyInterestRate = annualInterestRate/12.0
low = balance/12.0
high = (balance * ((1.0 + monthlyInterestRate)**12))/12.0
epsilon = 0.01
minPay = (high + low)/2.0
month = 0
def calculate(month, balance, minPay, monthlyInterestRate):
    while month <12:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance   
while abs(balance) >= epsilon:
    balance = initBalance
    month = 0
    balance = calculate(month, balance, minPay, monthlyInterestRate)
    if balance > 0:
        low = minPay
    else:
        high = minPay
    minPay = (high + low)/2.0
minPay = round(minPay,2)
print('Lowest Payment: ' + str(minPay))