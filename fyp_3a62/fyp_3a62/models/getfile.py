# got it from here https://stackoverflow.com/questions/38511444/python-download-files-from-google-drive-using-url
import requests
import shutil
import os

file_id = '1tVmSjGPl_su_hvFaHAYXQ3qexQ4P7p9n' #get shareable link of file and take id between d/ /view
destination = 'model.pt' #location of the file in 2b13.1936207.emily google drive
source_dir = '../fyp_3a62'
target_dir = '../fyp_3a62/fyp_3a62/static/nlp'

if os.path.exists(target_dir+'/'+destination):
    os.remove(target_dir+'/'+destination)

def download_file_from_google_drive(id, destination):
    URL = "https://drive.google.com/uc?export=download&confirm=no_antivirus"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def getfile(destination, source_dir, target_dir):

    download_file_from_google_drive(file_id, destination) #get file from drive

    # moving file to desired location
    if os.path.exists(target_dir+'/'+destination):
        print ("File exists in destination")
    else:
        shutil.move(source_dir+'/'+destination, target_dir+'/'+destination)

getfile(destination, source_dir, target_dir)
