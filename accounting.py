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

def get_sales_by_type(filename):
    """compares the sales revenue of online orders and orders from salespeople"""

    with open(filename, 'r') as sales_data:
        online_revenue = 0
        salesperson_revenue = 0

        for line in sales_data:
            _, sales_type, _, amt = line.rstrip().split('|')

            if sales_type == "0":
                online_revenue += float(amt)
            else:
                salesperson_revenue += float(amt)
            print(f"Salespeople generated ${salesperson_revenue:.2f} in revenue.")
            print(f"Internet sales generated ${online_revenue:.2f} in revenue.")

            if sales[1] > sales[0]:
                print("Guess there's some value to those salespeople after all.")
            else:
                print("Time to fire the sales team! Online sales rule all!")


def main():
    """run the melon count, gets the total revenue and shows revenue by type of sale"""

    #gets the order counts
    counts = get_melon_count('orders-by-type.txt')

    #gets total revenue
    dorky_line()
    get_revenue(counts)

    #gets the revenue by sales type
    dorky_line()
    get_sales_by_type('orders-with-sales.txt')

#call main function
main()




