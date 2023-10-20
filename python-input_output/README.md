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
file = open("filename.txt", "w") # You can replace "filename.txt" with the desired file.

content = file.read() # Read full content of a file.

print(content) # Print conetnts of file.
```
In the example above, you can use *read()* function to read the full content of a file which is being stored inside a variable named *content*.
With the same variable, you can use it to print said contents.
