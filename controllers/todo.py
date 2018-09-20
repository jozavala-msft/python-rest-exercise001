from apistar import Route, http

from models.todo import Todo
from repositories.todo import TodoRepository

todo_repository = TodoRepository()


#
#  Create a new resource
#
def create_todo(request: http.Request):
    json_body = request.body.decode('utf-8')
    todo = Todo.from_json(s=json_body, infer_missing=True)
    return todo_repository.create_todo(todo=todo).to_json()


#
#  Get a resource by its id
#
def get_todo(todo_id):
    return todo_repository.get_todo_by_id(todo_id=todo_id).to_json()


routes = [
    Route('/todos', method='POST', handler=create_todo),
    Route('/todos/{todo_id}', method='GET', handler=get_todo)
]
