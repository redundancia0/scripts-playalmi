import os
import shutil
import requests

ruta = "redundandia0-backups.duckdns.org:8080"

def compress_folder(folder_path, zip_path):
    shutil.make_archive(zip_path, 'zip', folder_path)

def send_backup(zip_file):
    api_url = f"http://{ruta}/api/backup/receive"

    try:
        with open(zip_file, 'rb') as file:
            files = {'file': file}
            response = requests.post(api_url, files=files)
            if response.status_code == 200:
                print("Backup file uploaded successfully.")
            else:
                print(f"Failed to upload backup file. Status code: {response.status_code}")
    except FileNotFoundError:
        print("Backup file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    folder_to_compress = "/home/"
    zip_file = "/tmp/home_backup"
    compress_folder(folder_to_compress, zip_file)
    zip_file += ".zip"
    send_backup(zip_file)
