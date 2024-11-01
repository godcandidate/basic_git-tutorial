import  os
import subprocess
import shutil

# Function to restart a service
def restart_service(service_name):
    try:
	subprocess.run(['sudo','systemcl','restart',service_name], check=True)
	print(f"Service '{service_name}' restarted successfully.")
    except subprocess.CalledProcessError as e:
	print(f"Error restarting service '{service_name}': {e}"}

# Function to clear the temp folder
def clear_temp_folder(temp_folder):
    try:
	shutil.rmtree(temp_folder)
	os.makedirs(temp_folder)
	print(f"Temporay folder '{temp_folder}' cleared sucessfully.")
    except Exception as e:
	print(f:"Error clearing temporay folder '{temp_folder}':{e}")

if __name__ = "__main__":
    SERVICE_NAME = "your_service_name"   
    TEMP_FOLDER = "/path/to/temp/folder"

    restart_service(SERVICE_NAME)
    clear_temp_folder(TEMP_FOLDER) 
