from apistar import Route

from repositories.todo import TodoRepository

todo_repository = TodoRepository()


#
#  Create a new resource
#
def create_todo(todo_payload):
    return todo_repository.create_todo(todo_payload=todo_payload)


routes = [
    Route('/todos', method='POST', handler=create_todo)
]
