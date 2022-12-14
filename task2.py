#Дан список, вывести отдельно буквы и цифры, пользуясь filter.
#[12,'sadf',5643] ---> ['sadf'] ,[12,5643]

sequence = '12 sadf 5643'
sequence = sequence.split()

letters = list(filter(lambda x: len(x) > 1 and x.isalpha(), sequence))
numbers = list(filter(lambda x: x.isnumeric(), sequence)) 

print(letters)
print(numbers)

