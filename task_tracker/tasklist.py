

from task_tracker.task import Task


class TaskList:
    def __init__(self) -> None:
        self.__task_list = []

    def add_task(self, task: Task):
        '''Add a task'''
        self.__task_list.append(task)

    def remove_task(self, index):
        '''Task remove'''
        for obj in self.__task_list:
            if index == obj.id:
                self.__task_list.remove(obj)

    def get_task_list_and_details(self):
        '''Outputs a list of tasks and details'''
        task_details = [str(i) for i in self.__task_list]
        print('\n\n'.join(task_details))
        print()
        print(input('Press Enter\n'))

    def update_task(self, index):
        '''Task update'''
        for obj in self.__task_list:
            if index == obj.id:
                while True:
                    try:
                        update = int(input(
                            '''What field update:\n1 - Task name\n2 - Task description\n3 - Task creation data\n4 - All fields\n> '''))
                    except ValueError:
                        print('Enter a value from 1 to 4\n')
                    else:
                        if update not in range(1, 4):
                            print('Enter a value from 1 to 4-!\n')
                        else:
                            if update == 1:
                                obj.task_name = input(
                                    'Enter the name of the task: ')
                            if update == 2:
                                obj.task_description = input(
                                    'Enter a description of the task: ')
                            if update == 3:
                                obj.task_creation_data = input(
                                    'Change the date the task was created: ')
                            if update == 4:
                                obj.task_name = input(
                                    'Enter the name of the task: ')
                                obj.task_description = input(
                                    'Enter a description of the task: ')
                                obj.task_creation_data = input(
                                    'Change the date the task was created: ')
                            break

    def update_status(self, index):
        '''Status update'''
        for obj in self.__task_list:
            if index == obj.id:
                while True:
                    update = input('Complete task?\n')
                    if update not in ('yes', 'no'):
                        print('Please enter yes or no')
                    elif update == 'yes':
                        obj.task_status = 'Complete'
                        break
                    elif update == 'no':
                        break

    def length(self):
        current_length = 0
        for _ in self.__task_list:
            current_length += 1
        return current_length

    def task_list_not_empty(self):
        if self.__task_list:
            return True
        print('Task list is empty')
