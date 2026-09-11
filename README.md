# AirBnB Clone - The Console

## Description
This project is the first step towards building a full-stack AirBnB clone web application. It implements a command-line interface (console) that allows managing application data objects. The console supports CRUD operations for various models, with persistence provided via JSON file storage.

## Command Interpreter Features
- Create new data objects (BaseModel, User, State, City, Amenity, Place, Review).
- Retrieve existing objects from storage.
- Perform operations on objects (counting, updating attributes).
- Delete objects.
- Store and reload objects using JSON serialization.

## How to Start the Console
To start the console in interactive mode, execute console.py:
./console.py

To run in non-interactive mode, pipe commands into console.py:
echo "help" | ./console.py

## How to Use the Console
Once started, the prompt (hbnb) will appear. Type help to list available commands or help <command> for detailed command information.

## Authors
- Ganza Henry Kevin (ghkfuture@users.noreply.github.com)
