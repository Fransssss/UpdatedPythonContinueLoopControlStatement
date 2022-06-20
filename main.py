# Continue loop control - skip to the next itetation in loop

print("\n== Continue Loop Control Statement ==")
phone = input("Input phone number in these format: 'xxx-xxx-xxxx' : ")
lenPhone = int(12)
print('\n')
if len(phone) == lenPhone:
    for i in phone:
        if i == "-":
            continue             # skip dash '-'
        print(i,end="")          # end="" make the statement output horizontally
else:
    print("\n[Invalid phone format]")

print('\n')
