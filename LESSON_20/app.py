## Working with Files and Directories
from pathlib import Path # Importing Path class from pathlib module

# Absolute path
# In windows: c:\Program Files\Microsoft
# In Mac: /usr/local/bin

# Relative path: Starting from the current dirctory
# In this tutorial we are working with Releative path

path = Path("ecommerce")
print(path.exists()) ## Getting back True or False

## We can use the path method to create a director in the current directory
path = Path("emails")
print(path.mkdir())

## We can delete a dirctory using Path
print(path.rmdir())

## Finding all files and dirctories in a given path
## We can use glob method from Path class to search for all files and directories in a given path
path = Path()

for file in path.glob("*.py"):
    print(file)