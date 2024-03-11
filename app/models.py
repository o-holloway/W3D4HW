class Task:
    id_counter = 1

    def __init__(self, description, body, status):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.description = description
        self.body = body
        self.status = status

    def __str__(self):
        return f"""
        {self.id} - {self.description}
        Complete: {self.status}
        {self.body}
        """
    
    def __repr__(self):
        return f"<Task {self.id}|{self.description}>"