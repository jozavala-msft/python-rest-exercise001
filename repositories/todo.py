import uuid


class TodoRepository(object):

    todos_db = dict()


    #
    #  Create a new resource
    #
    def create_todo(self, todo_payload):
        todo_id = str(uuid.uuid4())
        self.todos_db[todo_id] = todo_payload
        todo_payload['id'] = todo_id
        return todo_payload

    #
    #  Get a resource by its id
    #
    def get_todo_by_id(self, todo_id):
        return self.todos_db[todo_id]
