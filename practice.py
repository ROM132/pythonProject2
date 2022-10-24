
# qus
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


ext = [2200, 2350, 2600, 2130, 2190]

print(f"You spent extra {ext[1] - ext[0]}")
print(f"You first three months are: {ext[1] + ext[0] + ext[2]}")

num = 2000
ext.append(1980)


print(f"==========> ext == {ext}")
if num in ext:
    print(num)
else:
    print("You dont have a month with 2000 dollar!")

print(f"You have now {ext[3] - 200}")
