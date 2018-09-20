from apistar import Route

from repositories.todo import TodoRepository

todo_repository = TodoRepository()


#
#  Create a new resource
#
def create_todo(todo_payload):
    return todo_repository.create_todo(todo_payload=todo_payload)


#
#  Get a resource by its id
#
def get_todo(todo_id):
    return todo_repository.get_todo_by_id(todo_id=todo_id)


routes = [
    Route('/todos', method='POST', handler=create_todo),
    Route('/todos/{todo_id}', method='GET', handler=get_todo)
]
