from apistar import App

from controllers import todo

routes = [
    *todo.routes
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
