# Housing Value Prediction
Simple machine learning code in python for house price prediction using linear regression model.
also flask and unitest are done.
# Steps Performed
1. **Folder Structure**: Maintain a folder structure with files organized in their respective folders.

2. **Conda Environment**: Create a new Conda environment for your project.

3. **Libraries**: Install all the required libraries from the `requirements.txt` file.

4. **Package Setup**: Create a Python package structure by adding an `__init__.py` file inside a folder (e.g., `housing_price`) within the `src` directory.

5. **Setup.py**: Create a `setup.py` file for your package and install it using the appropriate command.

6. **Flask API**: Create an `app.py` file for your Flask API application.

7. **HTML Interface**: Create an `index.html` file and place it inside the `templates` folder for your web interface.

**Note for GitHub Actions:**

GitHub Actions is designed for automated tasks, not GUI applications. Running a Python app with a graphical interface in GitHub Actions is challenging as it typically runs in a headless environment.

Consider adapting your app for headless execution or explore alternative CI/CD platforms for GUI apps.

## Command to create the environment
$ conda create --name H_p_predict
## Command to activate the environment
$ conda activate H_p_predict
## Command to install the required libraries from the requirements.txt
$ pip install -r requirements.txt
## command to install setup.py
$ python setup.py install
## command to run the unitest
$ python -m unittest tests/test_model.py
## Command to start the flask application
$ python app.py
