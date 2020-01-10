# Add your code here.
def total_length(list_string):
    total_sum   =   0
    for item in list_string:
        total_sum   +=  len(item)

    return total_sum

# Should return 6:
print(total_length(['foo', 'bar']))

# Should return 0 (it's an empty list):
print(total_length([]))

# Should return 8:
total_length(['balloons'])

# Should return 0 (it has four empty strings):
total_length(["", '', "", ''])
