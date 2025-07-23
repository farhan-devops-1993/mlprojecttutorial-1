# Importing necessary modules
import os  # For interacting with the operating system: creating directories, checking file paths, etc.
from pathlib import Path  # For working with file and directory paths in an object-oriented way
import logging  # For displaying info/debug logs

# Configure the logging module to show messages of level INFO and above
logging.basicConfig(level=logging.INFO)  # This will print messages like "Creating directory..." etc.

# Define your project name as a variable
# This makes your structure flexible — you can rename the project by changing this one variable
project_name = "mlproject"

# List of all files (with paths) to be created for your project structure
# Using f-strings to make the structure dynamic based on the project name
list_of_files = [

    #".github/workflows/.gitkeep",  # Used to keep the empty workflows folder in GitHub Actions for CI/CD

    # Core package folder (src/mlproject/)
    f"src/{project_name}/__init__.py",  # Makes mlproject a Python package

    # Components folder - contains individual steps in ML pipeline
    f"src/{project_name}/components/__init__.py",  # Makes components a sub-package
    f"src/{project_name}/components/data_ingestion.py",  # Will contain logic to ingest data
    f"src/{project_name}/components/data_transformation.py",  # Logic to transform/clean/preprocess data
    f"src/{project_name}/components/model_trainer.py",  # Script to train the ML model
    f"src/{project_name}/components/model_monitering.py",  # Will contain code to monitor model performance

    # Pipelines folder - contains training and prediction pipelines
    f"src/{project_name}/pipelines/__init__.py",  # Makes pipelines a sub-package
    f"src/{project_name}/pipelines/training_pipeline.py",  # Code to run the full training pipeline
    f"src/{project_name}/pipelines/prediction_pipeline.py",  # Code to run inference/predictions

    # Utility and supporting files
    f"src/{project_name}/exception.py",  # Will contain custom exception classes
    f"src/{project_name}/logger.py",  # Logger configuration for the project
    f"src/{project_name}/utils.py",  # Common reusable utility functions

    # Project-level files
    "app.py",  # Entry point if running the project as an app (e.g., Streamlit, FastAPI, etc.)
    "Dockerfile",  # Used to containerize the app using Docker
    "requirements.txt",  # List of dependencies to be installed via pip
    "setup.py",  # For packaging the project (e.g., pip install .)
]

# Loop through each file in the list and create the necessary folders and empty files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the string path to a Path object for easier manipulation
    filedir, filename = os.path.split(filepath)  # Split path into directory and file name

    # If there's a directory (i.e., it's not a root file like setup.py), create the directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directory if it doesn't exist (recursive)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # If the file does not exist OR is empty, then create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:  # Open file in write mode (creates file if it doesn’t exist)
            pass  # No content for now — just create an empty file
        logging.info(f"Creating empty file: {filepath}")

    # If the file already exists and has content, log that it exists
    else:
        logging.info(f"{filename} already exists")  # Avoid overwriting existing files
