

class Task:
    id = 0

    def __init__(self,
                 task_name: str,
                 task_description: str,
                 task_creation_data: 'str',) -> None:
        self.task_name = task_name
        self.task_description = task_description
        self.task_creation_data = task_creation_data
        self.task_status = 'Incomplete'
        Task.id += 1
        self.id = Task.id

    def __str__(self):
        return (f'Task id: {self.id}\n'
                f'Task name: {self.task_name}\n'
                f'Task description: {self.task_description}\n'
                f'Task creation data: {self.task_creation_data}\n'
                f'Task status: {self.task_status}')
