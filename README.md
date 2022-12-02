# Programming for Data Analytics Project
---
## Description
 I will investigate a real-world phenomenon, gather data points over different variables and investigate their various relationships and their predictive ability. For this project I am investigating the predictive factors which are indicators of the presence or absence of cardiovascular disease. I will take data from this dataset: https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset  The variables are of three types: Objective: containing factual information; Examination: results of medical examination; Subjective: information given by the patient. There are 12 input variables and 1 output variable "cardio" (has or hasn't cardiovascular disease). The 12 input variables are id, age, height, weight, gender, systolic blood pressure, diastolic blood pressure, cholesterol, glucose, smoking, alcohol intake, physical activity. Age, height, weight and gender are the objective variables. Systolic and diastolic blood pressure, cholestrol, glucose are the examination features. Smoking, alcohol intake and physical activity are the subjective variables. It must be noted that subjective variables are subject to a degree of unreliability due to the dependence on trust of the answers given by the patients. 

## Repository Contents
- Jupyter notebooks
- README.dm
- .gitignore 

## How to Run Jupyter
Jupyter Notebook is an interactive environment for writing and running code. The Notebook in my repository is linked with the iPython kernel and therefore runs Python code. Code cells allow users to run code by clicking 'shift-enter'or by clicking the ▶ button in the toolbar. 'ctrl-enter' runs a selected cell and enters command mode. The Kernel is used to manage running of the code, it can be restarted to nullify all cell outputs or interrupted.

Installation documentation for Jupyter can be found, on [ReadTheDocs](https://docs.jupyter.org/en/latest/install.html). More advanced usage of Jupyter notebook can be found [here](https://jupyter-notebook.readthedocs.io/en/latest/).

For a local installation, it can be installed via pip by running:
``` python
pip install notebook
```
Jupyter is launched with in a local installation:
``` python
jupyter notebook
```
Or for running a Jupyter notebook remotely you need some configuration. See [Running a notebook server](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html).