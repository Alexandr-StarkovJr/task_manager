

from task_tracker.task import Task
from task_tracker.tasklist import TaskList


def main():
    task_list = TaskList()
    options = '''
1 - Add task
2 - Delete task
3 - Update task
4 - View task list
5 - Update status
6 - Exit
'''
    task = None

    while True:
        print(options)
        try:
            user_input = int(input("Please choose an option: "))
        except ValueError:
            print('Enter a valid value from 1 to 6')
        else:
            if user_input not in range(1, 7):
                print('Enter a valid value from 1 to 6\n')
            else:
                if user_input == 1:
                    task = Task(input('Task name: '), input(
                        'Task description: '), input('Task creation data: '))
                    task_list.add_task(task)
                    print('Task added')
                if user_input == 2:
                    if task_list.task_list_not_empty():
                        index = int(
                            input(f'You have {task_list.length()} task(s)\nWhat task delete: '))
                        if index in range(task_list.length() + 1):
                            task_list.remove_task(index)
                        else:
                            print('There is no such task')
                if user_input == 3:
                    if task_list.task_list_not_empty():
                        index = int(
                            input(f'You have {task_list.length()} task(s)\nWhat task to update: '))
                        if index in range(task_list.length() + 1):
                            task_list.update_task(index)
                        else:
                            print('There is no such task')
                if user_input == 4:
                    if task_list.task_list_not_empty():
                        task_list.get_task_list_and_details()
                if user_input == 5:
                    if task_list.task_list_not_empty():
                        index = int(
                            input(f'You have {task_list.length()} task(s)\nWhat task status to update: '))
                        if index in range(task_list.length() + 1):
                            task_list.update_status(index)
                        else:
                            print('There is no such task')
                if user_input == 6:
                    break


if __name__ == '__main__':
    main()
