"""break continue pass"""  # docSting

# break
number = 0

for number in range(10):
    if number == 5:
        break    # дает возможность выйти из цикла

    print('Number is ' + str(number))

print('Out of loop \n')


# continue
number = 0

for number in range(10):
    if number == 5:
        continue    # дает возможность пропустить часть цикла

    print('Number is ' + str(number))

print('Out of loop \n')


# pass
number = 0

for number in range(10):
    if number == 5:
        pass    # позволяет обрабатывать условия без влияния на цикл

    print('Number is ' + str(number))

print('Out of loop')