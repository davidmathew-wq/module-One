def greet_customer():
    print("welome to the lemonade stand")
    print("fresh lemonade , made just for you.")
greet_customer()
price =(int(input(" price_per cup ")))
Cups =(int(input(" no.of cup sold ")))
def calculate_total(price,Cups):
    total = price*Cups
    return total
print("total price",calculate_total (price,Cups))
