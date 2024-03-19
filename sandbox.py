from querymaker import make_query

def my_func(a, b):
    if a > b:
        return a

my_query = make_query(my_func)

print(my_query)

def my_func(a, b, table_name):
    with table_name:
        if a > b:
            del table_name

def my_func(table_name):
    return table_name.all()