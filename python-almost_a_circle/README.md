# Python - Almost A Circle Project!

## General Questions:

### What is Unit testing and how to implement it in a large project?

Unit testing is a software testing technique where individual units or components of a software system are tested in isolation to ensure that they
function correctly. It involves writing test cases for each unit to verify its functionality and behavior.

Divide your project into modules or packages, with each module containing related functionality. This modular structure will make it easier to write and
manage unit tests.


### How to serialize and deserialize a Class?

To serialize and deserialize a class, we can use the *pickle* module, which is part of the Python standard library. Pickle allos us to convert objects into a byte stream (serialization) and then deconstruct the objects from byte stream (deseerialization).

```ruby
import pickle

class MyClass:
    def __init__(self, name):
        self.name = name

# Serialize the object
my_object = MyClass("Example")
serialized_object = pickle.dumps(my_object)

# Save the serialized object to a file
with open("serialized_object.pickle", "wb") as file:
    file.write(serialized_object)

# Deserialize the object
with open("serialized_object.pickle", "rb") as file:
    deserialized_object = pickle.load(file)

# Access the deserialized object
print(deserialized_object.name)  # Output: Example
```
As we can see from the example abovee, *pickle* follows similar fundamentals as the *json* module, in terms of its convertion methods.

It is important to NOTE that  pickle  is not secure against malicious data, so it's recommended to only unpickle data from trusted sources.
Additionally,  pickle  is not compatible across different Python versions, so it's important to ensure compatibility when deserializing objects.


### What is *args and how to use it?

The  *args*  parameter collects any number of positional arguments into a tuple, which can then be accessed within the function.

```ruby
def my_function(*args):
    for arg in args:
        print(arg)

# Call the function with multiple arguments
my_function('Hello', 'World', 'Python')
```
In the above example, the  my_function  function has a parameter  *args . This means that the function can accept any number of arguments. When the
function is called with multiple arguments, they are collected into a tuple named  args . Inside the function, we can iterate over the  args  tuple and
print each argument.

The  *args  syntax is useful when you want to create a function that can handle a variable number of arguments without specifying them individually. It
allows for more flexibility and can simplify the function's implementation.


### What is **kwargs and how to use it?

The  **kwargs  parameter collects the keyword arguments into a dictionary, where the keys are the argument names and the values are the corresponding
values passed to the function.

```ruby
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

# Call the function with multiple keyword arguments
my_function(name='John', age=30, city='New York')
```
In the above example, the  my_function  function has a parameter  **kwargs . This means that the function can accept any number of keyword arguments
When the function is called with keyword argument, they are collected into a dictionary named  kwargs . Inside the function, we can iterate over the
kwargs  dictionary and print each key-value pair.

The  **kwargs  syntax is useful when you want to create a function that can handle a variable number of keyword arguments without specifying them
individually. It allows for more flexibility and can simplify the function's implementation.


### How to handle named arguments in a function?

We can handle *named arguments* by pairing the arguments with KeyWords, hence in similar fashion as **kwargs.

```ruby
def my_function(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

# calling the function with named arguments
my_function(name="John", age=30, city="New York")
```
From the example above, we can see that we called the function and gave each argument their respective value. Another thing to mention is that we are
defining the arguments in the function, we set a *default* value, as to sort expect certain mrequirements from the users. Also, we can be specific on the
arguments that we want to call, we don't have to use all of them if its not necessary.
