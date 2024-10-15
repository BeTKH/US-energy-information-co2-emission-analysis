# This code file should contain the code required to upload data to Azure Data Lake Storage.
# The problem should be able to run by the instructor using 'python ingestREST.py' (with their own API key).
# Store your key in a file with a .config appendix to avoid accidental check-in (.gitignore is setup to ignore .config)

# Assignment problems:
#   1a) [done] Upload the PopulationWithPercentIncrease.csv file from the IngestKaggle.py problem to the storage account created
#       for assignment 1.  Programmatically create a new container, assign-2, and a new directory,
#       upload-sample before uploading.
#   1b) [done] Take a screenshot of the uploaded file in your storage account, showing the full path.
#   1c) [done] Save the screenshot to the Data\Upload folder in git and push to GitHub.

# Points for this file: 15


# my code

from azure.storage.filedatalake import DataLakeServiceClient


# init storage acct url
def initialize_storage_account(storage_account_name, storage_account_key):
    service_client = DataLakeServiceClient(account_url=f"https://{storage_account_name}.dfs.core.windows.net",
                                           credential=storage_account_key)
    return service_client


# read SAS key from config
with open("sas.config") as f:
    sas_key = f.readline().strip()


# Init storage account
service_client = initialize_storage_account("assign1storebekalue", sas_key)


# Create a container
file_system_client = service_client.create_file_system(file_system="assign-2")
print("Container 'assign2' created successfully.")

# Create a dir inside  container
directory_client = file_system_client.create_directory(
    "Pop_Percent_Increase_dir")
print("Directory 'Pop_Percent_Increase_dir' created successfully.")

# -----------------Upload data file to the directory-----------------

# path to a file
file_name = "Data/WorldPopulation/PopulationWithPercentIncrease.csv"
file_client = directory_client.create_file("PopulationWithPercentIncrease.csv")

# Open the file from the relative path and upload its contents
with open(file_name, "r") as populationIncrease_file:
    file_contents = populationIncrease_file.read()

# Upload the file content to the Data Lake
file_client.upload_data(file_contents, overwrite=True)
print(f"File '{file_name}' uploaded successfully.")


print("UploadDataToADLS problem")
