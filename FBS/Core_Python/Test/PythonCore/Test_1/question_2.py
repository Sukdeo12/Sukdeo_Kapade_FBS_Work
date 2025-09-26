#WAP to calculate simple interest based on priciple, rate and Time (SI = P*R*T/100)
priciple = float(input("Enter the principle amount : "))
rate = float(input("Enter the rate of interest amount : "))
Time = float(input("Enter the time amount : "))

SI = (priciple * rate * Time) / 100

print(f"principle amount is : {priciple}, rate is : {rate} and Time is {Time} then Simple interest is {SI}.")
