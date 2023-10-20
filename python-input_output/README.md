# Python - Input/Output Project!

## General Questions:

### Why Python programming is awesome?

Python programming is awesome due to its clean and readable syntax, making it easy to understand and maintain. Its simplicity and versatility make it accessible to
beginners and applicable to a wide range of applications. Python benefits from a large and active community that provides support and contributes to its continual
growth. It offers portability across different platforms and seamless integration with other languages. Additionally, Python provides an extensive collection of
libraries and frameworks that simplify complex tasks and accelerate development. Overall, Python's combination of readability, simplicity, versatility, community
support, portability, integration capabilities, and rich libraries make it an exceptional programming language.

### How to open a file?

To open a file, you can use the built-in *open()* function:
```ruby
file = open("filename.txt", "r") # You can replace "filename.txt" with the desired file.
```
In the *open()* function, the first argument is the name of the file to open and the second argument is the way(mode) that you want to open the
file, in this case, we're opening it on **READ** mode using *"r"*.

### How to write text in a file?

To write text in a file, you can open the file in **WRITE** mode using *"w"* then utilizing the *write()* function:
```ruby
file = open("filename.txt", "w") # You can replace "filename.txt" with the desired file.

file.write("Hello, World!") # Writing text to file.
file.write("Why is that a thing?\n") #Finishing text with new line.
```
As you see, you can call this method multiple times to write different lines of text as you can also finish the text with *\n*.

### How to read the full content of a file?

To read the full content of a file, you can use the **read()** function:
```ruby
file = open("filename.txt", "r") # You can replace "filename.txt" with the desired file.

content = file.read() # Read full content of a file.

print(content) # Print contents of file.
```
In the example above, you can use *read()* function to read the full content of a file which is being stored inside a variable named *content*.
With the same variable, you can also use it to print said contents.

### How to read a file line by line?

To read a file line by line, you can use **readline()** function along with a *loop*:
```ruby
file = open("filename.txt", "r") # You can replace "filename.txt" with the desired file.

line = file.readline() # Read line by line.
while line: # Loop through file to print each line.
    print(line)
    line = file.readfile()
```
In the example above, we made a variable name *line* that reads each line of the the file using a loop. The loop will continue until there no
more lines to print. A worthy mention is that inside the loop can implement different operations that suit your needs...!

### How to move the cursor in a file?

To move cursor in a inside a file, you can use the **seek()** function which determines where the next read or write operation will be:
```ruby
file = open("filename.txt", "r") # You can replace "filename.txt" with the desired file.

file.seek(10) # Moves the cursor 10th byte position in the file.
```
As we can see, you can specify different positions like byte offsets or use other parameters to move the cursor to a specific line or character
position.

### How to make sure a file is closed after using it?

To close a file after using it, you can use the **close()** function:
```ruby
file = open("filename.txt", "r") # You can replace "filename.txt" with the desired file.

file.close() # Closes file.
```
Is important to mention to be careful when using this function since it can be prone to errors. For example, if we set an exception that takes
place before the *close()* statement, it can be troublesome.

To avoid such scenarios, we can use the **with** statement since it can take care of the closing of a file automatically, even if an exception
were to happen:
```ruby
with open("filename.txt", "r") as file:
    # Perform desired tasks.
# File is automatically closed outside the 'with' block.
```

### What is JSON?

**JSON** (JavaScript Object Notation) is a lightweight data interchange format that is widely used for data storage and communication between systems.
JSON is supported in Python through the built-inn module called *json*.

### What is Serialization?

**Serialization** refers to the process of converting a Python object into a format that can be stored or transferred, such as a byte stream or
string. This allows the object to be reconstructed for later use, either within the same application or in a different enviroment.

### What is Deserialization?

**Deserialization** refers to the process of converting a *serialized* object, such as a JSON string or a byte stream, back into a Python object.
In essence, it allows us to use said object were it originally came from.

### How to convert a Python data structure to a JSON string?

To convert a Python data structure to a JSON string, we can use **json.dumps()** function that's provided by the JSON module:
```ruby
import json

# Python data structure (dictionary).
data = {"name": "Christian", "age": 23, "city": "Cayey"}

# Convert Python data structure to JSON string
json_string = json.dumps(data)
```
In the example above, we used the *json.dumps()* function for the convertion into a JSON string. The resulting JSON string can be stored in a file,
sent over a network or used in any other way that requires a JSON representation of the data structure.

### How to convert a JSON string to a Python data structure?

To convet a JSON string to a Python data structure, we can use the **json.loads()**:
```ruby
import json

# JSON string.
json_string = {"name": "Christian", "age": 23, "city": "Cayey"}

# Convert JSON string to Python data structure
data = json.loads(json_string)
```
In the example above, we used the **json.loads()** function to convert variable *json_string* into a Python data structure. The resulting *data*
variable will contain the dictionary that we originally created in Python.

### How to access command line parameters in a Python script?

To access command-line parameters, we can use the the built-in function **sys.arv** in the *sys* module:
```ruby
import sys

# Access command-line parameters
arguments = sys.argv

# The first argument (index 0) is the script name itself
funny_names = arguments[0]

# Subsequently, you can store arguments into variables with indexing.
name1 = arguments[1]
name2 = arguments[2]
```
As we can see, *sys.argv* is a list that contains the command-line arguments passed to the script.
