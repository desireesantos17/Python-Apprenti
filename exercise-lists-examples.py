#create an empty list

todo_list = []
print("your todo list:", todo_list)

#append item to the list

todo_list.append("buy groceries")
todo_list.append("go to Oasis")
todo_list.append("play with Pepper")

print("updated list:", todo_list)

# insert an item

todo_list.insert(1,"get paid")
print("after inserting an item:", todo_list)

# using indexes and slicing

print("first task:", todo_list[0])
print("first task:", todo_list[-2:])

#mark a task as done

done_task = todo_list.pop(2)
print("you completed:", done_task)
print("Todo list after removal:", todo_list)
      
#update a existing task

print(todo_list[1])
todo_list[1] = "Read a book"
print("updated todo list value:", todo_list)

#print a task list 

print("Here's what you still need to do:")
for task in todo_list:
    print("-", task)