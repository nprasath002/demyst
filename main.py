from src.todo_api_client import TodoApiClient

if __name__ == "__main__":
    api_client = TodoApiClient()
    params = {'id': [2 * i for i in range(1, 21)]}
    todos = api_client.get_todos(params)
    for todo in todos:
        print( 'title: ', todo['title'] , 'completed: ', todo['completed'] )
