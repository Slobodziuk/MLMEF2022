# MLMEF2022
MLMEF2022 project
## How to run the application
There’re two possibilities to run the model. Either locally from the ipynb file or from the Flask app.
1.	Run the model from the ipynb file.
    1.1.	Open the ipynb file and ensure that it is in an environment that supports the libraries, at minimum use python 3.10.6.
    1.2.	Activate the virtual environment with “conda activate [your environment here]”
    1.3.	Run all the code segments except the model-export.
    1.4.	Write values into the correct data fields.

2.	Run the model through the Flask application
    2.1.	To run the Flask application open commandprompt or powershell in administrator mode.
    2.2.	Move to the directory in which the “app.py” file is in.
    2.3.	Run the command “pip install -r requirements.txt”
    2.4.	Run the python file by using the “flask –app app.py run” command.
