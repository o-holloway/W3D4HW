from .models import Task

class Todolist:
    def __init__(self):
        self.tasks = []

    def __get_task_from_id(self):
        task_id = input('Task ID Number? ')
        while not task_id.isdigit():
            task_id = input('Task ID must be an integer.\nEnter ID again: ')
        for task in self.tasks:
            if task.id == int(task_id):
                return task
        print(f"Task ID {task_id} does not exist")

    def create_new_task(self):
        description = input('Enter new task description: ')
        body = input('Enter new task body: ')
        status = False
        new_task = Task(description, body, status)
        self.tasks.append(new_task)
        print(f"New task created: '{new_task.description}'")

    def view_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(task)
        else:
            print('No tasks')

    def view_task(self):
        task = self.__get_task_from_id()
        if task:
            print(task)

    def edit_task(self):
        task = self.__get_task_from_id()
        if task:
            print(task)

            new_description = input("Type new description or press Enter to skip: ")
            if new_description.lower() != '':
                task.description = new_description

            new_body = input("Type new body or press Enter to skip: ")
            if new_body.lower() != '':
                task.body = new_body
            
            new_status = input("Toggle the completion status by pressing Enter or type 'X' to skip: ")
            if new_status.lower() != 'x':
                if task.status:
                    task.status = False
                else: 
                    task.status = True

            print(f"'{task.description}' has been updated!")

    def delete_task(self):
        task = self.__get_task_from_id()
        if task:
                print(task)
                confirm = input("Type 'yes' to delete this task: ").lower()
                if confirm == 'yes':
                    self.tasks.remove(task)
                    print(f"'{task.description}' was deleted")
                else:
                    print(f"'{task.description}' was NOT deleted")
