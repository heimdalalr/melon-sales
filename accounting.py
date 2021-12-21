# SALESPERSON_INDEX = 0
# INTERNET_INDEX = 1
# DORKY_LINE_LENGTH = 80

def dorky_line(): # declares the fuctions
    print("*" * 80) #prints a line of 80 asterisks

dorky_line()#calls the dorky_line function

orders = open("orders-by-type.txt") #opens the file specified
melon_tally = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0} #creates a dictionary of melon keys with initial values set to 0

for line in orders: #iterates through each line in an open file
    data = line.split("|")
    melon_type = data[1]
    melon_count = int(data[2])
    melon_tally[melon_type] += melon_count

f.close()
melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
total_revenue = 0
for melon_type in melon_tally:
    price = melon_prices[melon_type]
    revenue = price * melon_tally[melon_type]
    total_revenue += revenue
    # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))
    print(f"We sold {melon_tally[melon_type]} {melon_type} melons at {price:.2f} each for a total of {revenue:.2f}")
print("******************************************")
f = open("orders-with-sales.txt")
sales = [0, 0]
for line in f:
    d = line.split("|")
    if d[1] == "0":
        sales[0] += float(d[3])
    else:
        sales[1] += float(d[3])
print(f"Salespeople generated ${sales[1]:.2f} in revenue.")
print(f"Internet sales generated ${sales[0]:.2f} in revenue.")
if sales[1] > sales[0]:
    print("Guess there's some value to those salespeople after all.")
else:
    print("Time to fire the sales team! Online sales rule all!")
print("******************************************")
