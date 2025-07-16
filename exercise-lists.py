# create a list

todo_list = []
print("your todo list:", todo_list)

#append item to the list

todo_list.append("Make dinner")
todo_list.append("Go to Oasis")
todo_list.append("Walk Pepper")

print("updated list:", todo_list)

#mark done
done_task = todo_list.pop(0)
print("Completed", done_task)
print("Todo list after removing a task:", todo_list)

# use a for loop to iterate through the list

print("Here's what you still need to do:")
for task in todo_list:
    print("-", task)
