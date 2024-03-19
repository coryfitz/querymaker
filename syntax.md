## querymaker

Querymaker is a lightweight query builder for turning python functions into SQL queries.

It is not an ORM. It outputs strings which can be used as sql queries by other programs.

The primary design principle in querymaker syntax is to avoid creating specialized methods but rather to use the primitives inherent in python syntax to build sql queries.

<br>

### select star from

```sql
SELECT * FROM table_name;
```

option 1: all (built in)
good fit with English syntax - bad if you're thinking of the boolean meaning of all
```python
def my_func(table_name):
    return all(table_name)
```

option 2: all (not built in)
```python
def my_func(table_name, all):
    return table_name.all()
```

option 3: star
```python
def my_func(table_name, star):
    return star(table_name)
```
<br>

### select where

```sql
SELECT column_name FROM table_name WHERE condition;
```

option 1: with statement

```python
def my_func(condition, table_name):
    with table_name:
        if condition:
            return column_name
```

option 2: dot syntax

```python
def my_func(condition, table_name):
    if condition:
        return table_name.column_name
```
<br>

### delete from

```sql
DELETE FROM table_name WHERE condition;
```

Option: where

```python
def my_func(a, b, table_name):
    with table_name as table:
        if condition:
            del table_name
```       
<br>

### alter table + drop

```sql
ALTER TABLE customers DROP COLUMN contact_name;
```
should alter table be a function? automatically added?

```python

```