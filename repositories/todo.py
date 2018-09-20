import uuid

from models.todo import Todo


class TodoRepository(object):

    todos_db = dict()


    #
    #  Create a new resource
    #
    def create_todo(self, todo: Todo):
        todo_id = str(uuid.uuid4())
        self.todos_db[todo_id] = todo
        todo.id = todo_id
        return todo

    #
    #  Get a resource by its id
    #
    def get_todo_by_id(self, todo_id):
        return self.todos_db[todo_id]
