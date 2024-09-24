# Sean A
# Multiplication Table
# Use list comprehension to create a multiplcation table


# ONE LINE - NO MORE, NO LESS
table = [i * num for i in range(1, 11) for num in range(1, 11)]

########### NO TOUCHY ###########
for i, num in enumerate(table):
    if i % 10 == 0:
        print()

    print(num, end="\t")
print()
#################################
