# MongoGetterSetter Documentation

`MongoGetterSetter` is a metaclass that provides a convenient getter and setter API for instances of the classes that use it, allowing natural operations in Python objects to easily reflect in MongoDB documents.

Usage:
```
from mongogettersetter import MongoGetterSetter
```

### Methods

- `__getattr__(self, key)`: Returns a `MongoMatchWrapper` instance for the given `key`. See below for the capabalities of `MongoMatchWrapper`

    Example:

    Here, we initialize MyClass with `collection` and `filter_query` as mandatory attributes for MongoGetterSetter to function properly.

    ```
    class MyClass(metaclass=MongoGetterSetter):
        def init(self, _id):
        self._id = _id # this ID is used to query
        self.filter_query = {"id": _id} # or the ObjectID, at your convinence
        self.collection = collection # Should be a pymongo.MongoClient[database].collection


    obj = MyClass(_id)
    result = obj.some_key
    ```


- `__setattr__(self, key, value)`: Sets the value of the specified `key` in the MongoDB document.

    Example:

    ```
    obj.some_key = "new_value"
    ```

- `__contains__(self, key)`: Checks if the MongoDB document contains the specified `key`.

    Example:

    ```
    if "some_key" in obj:
        print("Key exists")
    ```

- `__str__(self)`: Returns a string representation of the MongoDB document.

    Example:

    ```
    print(obj)
    ```


## MongoMatchWrapper

`MongoMatchWrapper` is a class that wraps a MongoDB datatypes and provides a simple, straightforward API to perform various operations on the collection.

### Methods

- `__init__(self, _id, key, collection)`: Initialize the instance with the given `_id`, `key`, and `collection`.

- `get(self)`: Returns the value of the key in the MongoDB document.

- `inArray(self, value)`: Checks if the given `value` is present in the array of the document's key.

- `push(self, *values, maximum=-1)`: Pushes one or more `values` into the array of the document's key. If `maximum` is specified, it will limit the array size to the `maximum` value.

- `addToSet(self, value)`: Adds a `value` to the array of the document's key only if it doesn't exist in the array.

- `pop(self, direction=1)`: Removes the first (`direction=-1`) or the last (`direction=1`) element from the array of the document's key.

- `pull(self, value)`: Removes the specified `value` from the array of the document's key.

- `pullAll(self, *values)`: Removes all occurrences of the specified `values` from the array of the document's key.

- `size(self, value)`: Checks if the size of the array of the document's key is equal to the given `value`.

- `elemMatch(self, **kvalues)`: Checks if the array of the document's key contains at least one element that matches the specified key-value pairs in `kvalues`.

- `all(self, *values)`: Checks if the array of the document's key contains all the specified `values`.

- `update(self, field, match, **kvalues)`: Updates the nested field `field` of the document's key where the `field` value matches `match`, with the key-value pairs provided in `kvalues`.

- `__len__(self)`: Returns the length of the array of the document's key.

- `__str__(self)`: Returns a string representation of the value of the document's key.

- `__repr__(self)`: Returns a string representation of the value of the document's key.

## Examples

To provide a more detailed example, let's assume you have a MongoDB collection named people with the following documents:

```
[
    {
        "_id": 1,
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "Django", "JavaScript"],
        "contact": {
            "email": "alice@example.com",
            "phone": "555-1234"
        },
        "projects": [
            {
                "title": "Project A",
                "status": "completed"
            },
            {
                "title": "Project B",
                "status": "in progress"
            }
        ]
    },
    {
        "_id": 2,
        "name": "Bob",
        "age": 25,
        "skills": ["Java", "Spring", "JavaScript"],
        "contact": {
            "email": "bob@example.com",
            "phone": "555-5678"
        },
        "projects": [
            {
                "title": "Project X",
                "status": "completed"
            },
            {
                "title": "Project Y",
                "status": "in progress"
            }
        ]
    }
]
```

Now, let's create a class called `People` with `MongoGetterSetter` as its metaclass.

```
from pymongo import MongoClient
from mongogettersetter import MongoGetterSetter

# Connect to the MongoDB database and collection
client = MongoClient("mongodb://localhost:27017/")
db = client["example_db"]
people_collection = db["people"]

class People(metaclass=MongoGetterSetter):
    def __init__(self, _id, collection):
        self._id = _id  # this ID is used to query
        self.filter_query = {"id": _id}  # or the ObjectID, at your convenience
        self.collection = people_collection  # Should be a pymongo.MongoClient[database].collection



# Create a People object for Alice with _id = 1
alice = People(1)

# Access and modify Alice's name
print(alice.name.get())  # Output: 'Alice'
alice.name = "Alice Johnson"
print(alice.name.get())  # Output: 'Alice Johnson'

# Check if Alice's document has a 'contact' field
if 'contact' in alice:
    print("Contact field exists")

# Access and modify Alice's email
print(alice.contact.get())  # Output: {'email': 'alice@example.com', 'phone': '555-1234'}
alice.contact.email = "alice.johnson@example.com"
print(alice.contact.email.get())  # Output: 'alice.johnson@example.com'

# Access and modify Alice's skills
print(alice.skills.get())  # Output: ['Python', 'Django', 'JavaScript']
alice.skills.push("React", maximum=4)
print(alice.skills.get())  # Output: ['Python', 'Django', 'JavaScript', 'React']
alice.skills.pop(direction=-1)
print(alice.skills.get())  # Output: ['Python', 'Django', 'JavaScript']

# Access and modify Alice's projects
print(alice.projects.get())  # Output: [{'title': 'Project A', 'status': 'completed'}, {'title': 'Project B', 'status': 'in progress'}]
alice.projects.update("title", "Project A", status="archived")
print(alice.projects.get())  # Output: [{'title': 'Project A', 'status': 'archived'}, {'title': 'Project B', 'status': 'in progress'}]
```

## More MongoMatchWrapper examples

```
# Create a People object for Alice with _id = 1
alice = People(1)

# Create MongoMatchWrapper instances for Alice's skills and projects
alice_skills = alice.skills
alice_projects = alice.projects

# Examples for each method of the MongoMatchWrapper class

# 1. get()
print(alice_skills.get())  # Output: ['Python', 'Django', 'JavaScript']

# 2. inArray()
print(alice_skills.inArray("Python"))  # Output: True

# 3. push()
alice_skills.push("React", "Java", maximum=5)
print(alice_skills.get())  # Output: ['Python', 'Django', 'JavaScript', 'React', 'Java']

# 4. addToSet()
alice_skills.addToSet("C++")
print(alice_skills.get())  # Output: ['Python', 'Django', 'JavaScript', 'React', 'Java', 'C++']

# 5. pop()
alice_skills.pop(direction=-1)
print(alice_skills.get())  # Output: ['Python', 'Django', 'JavaScript', 'React', 'Java']

# 6. pull()
alice_skills.pull("Java")
print(alice_skills.get())  # Output: ['Python', 'Django', 'JavaScript', 'React']

# 7. pullAll()
alice_skills.pullAll("Python", "React")
print(alice_skills.get())  # Output: ['Django', 'JavaScript']

# 8. size()
print(alice_skills.size(2))  # Output: True

# 9. elemMatch()
print(alice_projects.elemMatch(title="Project A", status="completed"))  # Output: True

# 10. all()
print(alice_skills.all("Django", "JavaScript"))  # Output: True

# 11. update()
alice_projects.update("title", "Project A", status="archived")
print(alice_projects.get())  # Output: [{'title': 'Project A', 'status': 'archived'}, {'title': 'Project B', 'status': 'in progress'}]

# 12. __len__()
print(len(alice_skills))  # Output: 2

# 13. __str__() and __repr__()
print(alice_skills)  # Output: ['Django', 'JavaScript']
print(repr(alice_skills))  # Output: ['Django', 'JavaScript']
```


