# Sample list of mobile numbers
mobile_numbers = [
    '01971196937',
    '01719067566',
    '01946770371',
    '01752867522',
    '01727653535',
    '01866557515',
    '01747503257',
    '01621938810',
    '01747503257',
    '01991416320',
    '01831276542',
    '01789051988',
    '01831276542',
    '01322390574',
    '01856865625',
    '01639605088',
    '01647705787',
    '01741015762',
    '01894099343'

]

# Create an empty set to store unique numbers
unique_numbers = set()

# Iterate through each mobile number in the list
for number in mobile_numbers:
    # Add the number to the set
    unique_numbers.add(number)

# Convert the set back to a list if needed
unique_numbers_list = list(unique_numbers)

# Print the unique mobile numbers
for number in unique_numbers_list:
    print(number)
