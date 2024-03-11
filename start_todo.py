from app import Todolist
from app.models import Task


def run_todo():
    print('')
    print('Todo List 1.0')
    print('=============')
    todo = Todolist()

    task1 = Task('Window display maintenance', 'Check external signage and lighting', False)
    task2 = Task('Inspect department', 'Check aisle for clutter and re-order low-stock product', False)
    todo.tasks.append(task1)
    todo.tasks.append(task2)

    while True:
            print("\n1. Create A Task\n2. View All Tasks\n3. View Single Task\n4. Edit A Task\n5. Delete A Task\n6. Quit\n")
            to_do = input('Type a number and hit Enter: ')
            while to_do not in {'1', '2', '3', '4', '5', '6'}:
                to_do = input('Invalid option. Enter 1, 2, 3, 4, 5 or 6: ')
            if to_do == '1':
                todo.create_new_task()
            elif to_do == '2':
                todo.view_tasks()
            elif to_do == '3':
                todo.view_task()
            elif to_do == '4':
                todo.edit_task()
            elif to_do == '5':
                todo.delete_task()
            elif to_do == '6':
                break
            else:
                print(f"{to_do} is not a valid option")

    print('')
    print('=============================')
    print("Thank you for using Todo List")


run_todo()