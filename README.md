# AirBnB Clone - The Console
The console is the first part of the AirBnB project. The goal is to eventually deploy our server a simple copy of the AirBnB Website(HBnB).
A command interpreter to manage all AirBnB objects.


## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Installation
* Clone this repository: `git clone "https://github.com/anaruzz/AirBnB_clone.git"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`


#### Functions:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object


# Execution
The shell should work like this in interactive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
but also in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## Example of use
first run the console program
```
AirBnB_clone$ ./console.py
(hbnb) create BaseModel
c93eetw6-bd9a-4a80-f22c-6c455e394a46
(hbnb) show BaseModel c93eetw6-bd9a-4a80-f22c-6c455e394a46
[BaseModel] (c93eetw6-bd9a-4a80-f22c-6c455e394a46) {'id': 'c93eetw6-bd9a-4a80-f22c-6c455e394a46', 'created_at': datetime.datetime(2018, 2, 15, 1, 0, 42, 625486), 'updated_at': datetime.datetime(2018, 2, 15, 1, 0, 42, 625516)}
(hbnb) create
** class name missing **
(hbnb) show BaseModel
** instance id missing **
```
## AUTHORS
Abidi Ghofrane - [Github](https://github.com/anaruzz) / [Twitter](https://twitter.com/AbidiGhofrane1)  
Khammassi Khouloud - [Github](https://github.com/ggirlk) / [Twitter](https://twitter.com/ggirlk2)
