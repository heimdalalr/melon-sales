# SALESPERSON_INDEX = 0
# INTERNET_INDEX = 1
# DORKY_LINE_LENGTH = 80

def dorky_line(): # declares the function dorky line
    print("*" * 80) #prints a line of 80 asterisks

dorky_line()#calls the dorky_line function

def get_melon_count(filename): #declares the function to get the melon count
    """Tallies of melons by type"""

    with open(filename) as order_data: #opens the file as the variable order_data
        melon_counts ={ #sets the initial value of each type of melon as zero
            'musk': 0,
            'hybrid': 0,
            'watermelon': 0,
            'winter': 0
        }
        for line in order_data: #iterates through order data
            _, melon_type, melon_counts = line.rstrip().split('|') #splits the information between bars
            melon_counts[melon_type.lower()] += int(melon_counts) #taking the string of melon types into lowercase and adding the numbers of the types of melons

        return melon_counts

def get_revenue(counts):
    """Prints out the revenue for each melon type"""

    total_revenue = 0

    melon_prices = {
        'musk': 1.15,
        'hybrid': 1.30,
        'watermelon': 1.75,
        'winter': 4.00
    }

    for melon_type in counts:
        price = melon_prices[melon_type]
        revenue = counts[melon_type] * melon_prices[melon_type]
        total_revenue =+ revenue
        print(f"We sold {counts[melon_type]} {melon_type} melons at ${price:.2f} each for a total of ${revenue:.2f}")



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
