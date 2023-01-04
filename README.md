# MLMEF2022
MLMEF2022 project
## How to run the application
There’re two possibilities to run the model. Either locally from the ipynb file or from the Flask app.
1.	Run the model from the ipynb file.
    a.	Open the ipynb file and ensure that it is in an environment that supports the libraries, at minimum use python 3.10.6.
    b.	Activate the virtual environment with “conda activate [your environment here]”
    c.	Run all the code segments except the model-export.
    d.	Write values into the correct data fields.

2.	Run the model through the Flask application
    a.	To run the Flask application open commandprompt or powershell in administrator mode.
    b.	Move to the directory in which the “app.py” file is in.
    c.	Run the command “pip install -r requirements.txt”
    d.	Run the python file by using the “flask –app app.py run” command.
