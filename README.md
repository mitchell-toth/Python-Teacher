# Python-Teacher
An interactive teaching tool made to introduce beginners to Python. 

Complete with warmup exercises, challenges, hints, and a solution reference.

Initially made for my brother.

# Introduction
The "Introduction" directory provides a set of very simple exercises.

These are intended to teach the student basic Python data types and key words.

These also represent my first attempt at an interactive Python teaching tool that evaluates student code against expected output criteria.

To run a set of introductory exercises, select one of the Python files and run it.

# Interactive-Tester
The "Interactive-Tester" directory represents a more refined attempt at making an interactive teaching tool for Python.

There are 3 important directories to note:
 - Problems		--> 	contains Python problems that students complete
 - Solutions 	--> 	a reference containing all problem solutions. Also used by the tester to evaluate correctness of student code.
 - Data			--> 	contains all input/output for use by the solutions file in testing student code.
 
The final file in the "Interactive-Tester" directory is the main testing service: "tester.py".
 
# Format
Every test is confined to a function the student must implement. 

Student output is evaluated against a set of inputs specially designed for each problem. 
If every output matches the expected output, then the student passed the problem.

# Run
Simply run "tester.py" and follow the instructions.

For students working on the problems, it is best for them to have an editor open while the tester is running.
Preferably, the student's editor would auto-save so that the newest changes are picked up by the tester automatically.
If not, the user must manually save before each problem test (so that the changes are visible, of course). 

# Extending the problem set
Feel free to extend the problems that this interactive teacher has to offer.

When adding problems, keep in mind that you must add problems to the Problems directory,  
corresponding solutions to the Solutions directory, 
and corresponding input/output data to the Data directory.

Finally, you must update "tester.py" to display the option for the new problem set.