# Autograding Example: Python
This example project is written in Python, and tested with pytest.

### The assignment

Fix the failing tests in 

 - `test_exercise_01.py` and
 - `test_exercise_02.py`

The first tests are failing right now because the method isn't outputting the correct string. 

The second is failing because the code to pull the data hasn't been implemented yet.

Fixing these up will make the tests green. 


### Setup command
The following command is only used by the instructor:
`sudo -H pip3 install pytest`

Students can install pytest simply with the command: `pip install pytest`

### Run command
`pytest`

### Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be unaccessible.
