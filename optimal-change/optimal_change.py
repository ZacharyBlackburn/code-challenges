# create change variable rounded to cents
# must multpliy by 100 by to get rid of float, python cannot handle it
# return str if no change is given
# return str if item costs more than amount paid
# create lists of coins, values
# iterate through lists, adding from each to new array until change is at 0
# append to new list, create dictionary to get number of different coin types
# swap key, value pairs and add edge case 's', penny vs pennies, commas
# make list a str, add it to ouput str
# return output

import math

def optimal_change(item_cost, amount_paid):
    

    # # find change amount and round up to 2 decimals
    change = (amount_paid - item_cost) * 100
    change = round(change, 2)
    change = int(change)
    change = math.floor(change)
    
    # in case amount_paid doesn't exceed the item_cost, determine how much more is needed 
    more_money = round(item_cost - amount_paid)

    if change == 0:
        return f"There is no change for an item that costs ${round(item_cost, 2)} with an amount paid of ${round(amount_paid, 2)}."

    elif item_cost > amount_paid:
        return f"${round(amount_paid, 2)} is not enough to cover ${round(item_cost, 2)}, you need an extra ${round(more_money, 2)} to purchase this item."
    
    # create lists to iterate over of each value of coin type multiplied by 100 to account for floats
    else:
        coins = ['$100 bill', '$50 bill', '$20 bill', '$10 bill', '$5 bill', '$1 bill', 'quarter', 'dime', 'nickel', 'penny']
        values = [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1]
        
    
        amount_returned = []
    
    # iterate over values, pushing each coin type to new list until change is down to 0
        while change > 0:
            for i in range(len(values)):
                while values[i] <= change:
                    amount_returned.append(coins[i])
                    change = change - values[i]
                else:
                    i += 1
        
        # create dictionary to get key value pairs from coins and values
        duplicate_dict = {}
        for i in amount_returned:
            duplicate_dict[i] = amount_returned.count(i)

        # create a list with key value pairs swapped, account for different number of coins in given change statement, append 's' to plural values    
        new_list = []
        for keys, values in duplicate_dict.items():
            new_list.append(values)
            if values > 1 and keys == 'penny':
                new_list.append('penniess')
            elif values > 1:
                new_list.append(keys + 's,')
            else:
                new_list.append(keys + ',')
        
        # insert and at the 3rd to last element in list if there's more than one type of coin given back
        if len(new_list) > 2:
            new_list.insert(-2, 'and')
        
        
        # turn list into a string to add to final output
        output_coins = ' '.join(map(str,new_list))

    # Create final output str and add a period to the end of it while removing last comma
    output = f"The optimal change for an item that costs ${round(item_cost, 2)} with an amount paid of ${round(amount_paid, 2)} is {output_coins}"
    output = output[:-1] + '.'
        

    return output