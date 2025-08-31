# Defines the set_max_ticks function and its arguments.
def set_max_ticks(tickets, maximum=4):
    """Takes in the number of tickets and a default maximum number of 
    tickets as arguments and returns the appropriate maximum number of 
    tickets the next customer may buy. 

    args:
    tickets = An integer representing the number of tickets remaining.
    maximum = An integer representing the maximum number of tickets a 
        customer may purchase. Defaults to 4.
    """
    # Initializes the max_tickets variable and sets its value to 4.
    max_tickets = maximum
    # Evaluates the number of remaining tickets and sets max_tickets to 
    # the remaining value if it is lower than 4.
    if tickets < maximum:
        max_tickets = tickets

    # Returns max_tickets as an integer.
    return max_tickets

# Defines the set_message function and its arguments.
def set_message(tickets, max_ticks):
    """Takes in the number of tickets and the max number of tickets as 
    arguments and returns the appropriate message for the next customer. 

    args:
    tickets = An integer representing the number of tickets remaining.
    max_ticks = An integer representing the maximum number of tickets a 
        customer may purchase.
    """
    # Initializes the message variable with an empty string.
    message = ''
    # Evaluates the number of tickets remaining. If 4 or more remain, 
    # The first message is used, otherwise the second is used.
    if tickets >= max_ticks:
        message = f'How many tickets do you need? You may purchase up to {max_ticks}. '
    else:
        message = f'How many tickets do you need? You may purchase up to {tickets}. '

    # Returns the designated message as a string.
    return message

# Defines the buy_ticks function and its arguments.
def buy_ticks(tickets):
    """Takes in the number of tickets as an argument and returns the 
    number of tickets purchased by the customer.

    args:
    tickets = An integer representing the number of tickets remaining.
    """
    # Calls the set_max_ticks function to set an appropriate value for 
    # the maximum number of tickets each customer may purchase.
    max_ticks = set_max_ticks(tickets)

    # Calls the set_message function to set an appropriate message for 
    # the next customer.
    message = set_message(tickets, max_ticks)
    
    # Starts an input validation loop.
    while True:
        # Takes initial input from the customer.
        order = input(message)
        # Attempts to convert the customer's input to an integer. If 
        # there is an error, prints a message and restarts the loop.
        try:
            order = int(order)
        except:
            print('Please enter a number')
            continue

        # Evaluates the customer input to see if it's within the 
        # allowable range. If not prints a message and restarts the 
        # loop. Otherwise returns the value of order.
        if order > max_ticks or order < 1:
            print(f'Please enter a number between 1 and {max_ticks}.')
            continue
        else:
            return order
        
# Defines the main function.
def main():
    """The main function where initial variable values are established 
    and helper functions are called.
    """
    # Initializes the tickets variable with a value of 20.
    tickets = 10
    # Initializes the customers variable with a value of 0.
    buyers = 0

    # Starts a loop that runs until there are no more tickets.
    while tickets > 0:
        # On each loop, subtracts the number of tickets bought from 
        # the total.
        tickets -= buy_ticks(tickets)
        # On each loop, adds 1 to the number of customers.
        buyers += 1
    
    # Displays the total number of customers.
    print(f'Total number of customers: {buyers}')
        
if __name__ == '__main__':
    main()
