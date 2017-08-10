payment = float(input("Please enter the monthly payment: "))
principal = float(input("Please enter the current principal: "))
interest_rate = float(input("Please enter the interest rate, in decimal form: "))
timeframe = 0
temp_sum = 0

while principal > 0:
    timeframe += 1
    temp_fee = ((principal * int_rate)/365.25)*30
    principal = (principal + temp_fee) - payment

return timeframe
