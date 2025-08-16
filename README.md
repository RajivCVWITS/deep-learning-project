# deep-learning-project
1) Creating template.py file -> Logging, File and folder creation 
2) Filling requirements.txt
3) setup.py file content creation to make the src folder as local python package
4) Create Virtual Python environment and activate it
5) Install requirements.txt using pip
6) Write common.py file under utils folder to import these functions under any files in the project (load_json, save_json, create_directories, read_yaml, decode image, encode image, get file size, load binary data, save binary file)


### Workflow ###


1. Update config.yaml
2. Update secrets.yaml  [optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

### Data Ingestion Pipeline Setup ###

1. Configuration Setup (config.yaml)
This YAML file contains all the settings for data ingestion:
Where to store artifacts (artifacts_root)
Where to download and extract data (root_dir, local_data_file, unzip_dir)
The source URL for the data (source_URL)


2. Constants and Utilities (src/deep_learning_project/constants.py, src/deep_learning_project/utils/common.py)
constants.py

Defines paths like CONFIG_FILE_PATH and PARAMS_FILE_PATH so the rest of the code can refer to config files easily.
common.py

Provides utility functions:
read_yaml: Reads YAML files and returns their contents.
create_directories: Creates directories if they don’t exist.
Other helpers for file operations.


3. Configuration Manager (ConfigurationManager class)
Reads the config and params YAML files using read_yaml.
Creates the necessary directories using create_directories.
Provides a method to get a DataIngestionConfig object with all required paths and URLs.


4. Data Ingestion Logic (DataIngestion class)
Initialization:

Takes a DataIngestionConfig object (with all paths and URLs).
Download File:

Checks if the data file exists.
If not, creates the parent directory and downloads the zip file from the GitHub URL to the specified local path.
Extract Zip File:

Extracts the downloaded zip file into the specified directory.


5. Notebook or Script (research/01_data_ingestion.ipynb)
This is the entry point for running the pipeline.
It:
Sets the working directory.
Instantiates ConfigurationManager.
Gets the data ingestion config.
Instantiates DataIngestion.
Runs download_file() and extract_zip_file().
How the Folders Collaborate
config/: Stores configuration files.
src/deep_learning_project/: Contains reusable code (constants, utilities, classes).
artifacts/: Stores downloaded and extracted data.
research/: Contains notebooks/scripts that use the code from src to run the pipeline.

## Data Ingestion Flow Diagram ##
research/01_data_ingestion.ipynb
    |
    v
src/deep_learning_project/constants.py (paths to config files)
    |
    v
src/deep_learning_project/utils/common.py (read_yaml, create_directories)
    |
    v
src/deep_learning_project/ (ConfigurationManager, DataIngestion)
    |
    v
config/config.yaml (settings)
    |
    v
artifacts/data_ingestion/ (downloaded and extracted data)




### Prepare Base Model ###


Used 1 reference
Base model preparation is a key step in deep learning projects, especially when using transfer learning. Here’s why it’s needed:

Why Prepare a Base Model?
Transfer Learning:

You use a pre-trained model (like VGG, ResNet, etc.) that has already learned useful features from a large dataset (e.g., ImageNet).
This saves time and resources, and often improves performance for your specific task.
Customization:

You may need to modify the base model for your dataset:
Change the input size.
Add or remove layers.
Set the number of output classes.
Freeze or unfreeze layers for training.
Consistency:

Preparing the base model ensures your pipeline always starts from the same architecture and weights.
This makes experiments reproducible.
Efficiency:

Loading and saving the base model as an artifact avoids downloading or re-initializing it every time you run your pipeline.
Typical Steps in Base Model Preparation
Load a pre-trained model with the desired architecture and weights.
Configure input shape, output classes, and other parameters as per your config.
Save the base model for later use in training and evaluation.
Summary:
Preparing the base model sets up a strong, reusable foundation for your training pipeline, leveraging existing knowledge and making your workflow efficient and reproducible.