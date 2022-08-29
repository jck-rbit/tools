import pickle

with open('birthday list.txt', 'rb') as og_list:
    birthday_list = pickle.load(og_list)

# taking input

task = input("Would you like to: [add], [remove], [find] a birthday, check for birthdays [today], [check] if someone is in the list or [view] the list? ").lower()

if task == 'view':
    print(birthday_list)

elif task == 'today':
    current_date = input("Today's date? ").lower()
    for name, date in birthday_list.items():
        if current_date == date:
            print( "It is" , name +"'s birthday today.")

elif task == 'check':
    name = input("Name? ").lower()
    if name in birthday_list:
        print(name +"'s birthday is in the list.")
    else:
        print(name+"'s birthday is not in the list.")

elif task == 'add':
    name = input("Name? ").lower()
    date = input("Date? ").lower()
    birthday_list[name] = date
    print(name +"'s birthday, the" , date , "has been added.")

elif task == 'remove':
    remove = input("Name of person? ").lower()
    del birthday_list[remove]
    print(remove +"'s birthday has been removed.")

elif task == 'find':
    find = input("Name? ").lower()
    print( find +"'s birthday is the" , birthday_list[find]+".")

og_list.close()

# birthday list has been updated, time to write it to the birthday list file

with open('birthday list.txt', 'wb') as new_list:
    pickle.dump(birthday_list, new_list)

new_list.close()
