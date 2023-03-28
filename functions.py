FilePath = 'todos.txt'
def get_todos(filepath=FilePath):
    """ read text file and
    return to-do list items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FilePath):
    """write to text file and add to-do items"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)