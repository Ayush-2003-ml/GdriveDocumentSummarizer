from google_auth_oauthlib.flow import InstalledAppFlow 
from googleapiclient.discovery import build 
from googleapiclient.http import MediaIoBaseDownload

import io
import os
import sys

sys.path.append("C:/Users/AYUSH\Desktop/FileSummarizer")
import config as config 

g_scope = config.scope 

class AuthenticatorService :
    
    # method for authorization and google drive service creation
    def authenticate_drive(self):
        try :
            _flow = InstalledAppFlow.from_client_secrets_file(
                config.authentication_credentials,  
                g_scope
            )

            _credentials = _flow.run_local_server(port=0)

            _service = build(
                            'drive', 
                            'v3',
                            credentials = _credentials
                            )

            return _service
        except Exception as ex:
            print("Exception is: ", str(ex))
            return None

    # method for listing files in a drive folder
    def list_files(self, service, folder_id):
        try :
            _query = f"'{folder_id}' in parents"

            _results = service.files().list(
                q = _query,
                fields = "files(id, name, mimeType)"
            ).execute()

            return _results.get('files', [])
        
        except Exception as ex:
            print("Exception is: ", str(ex))
            return None


    # method for downloading files locally from drive folder in chunks
    def download_file(self, service, file_id, filename):
        try :
            os.makedirs("C:/Users/AYUSH/Desktop/FileSummarizer\downloads", exist_ok=True)
            print("filename is:", filename)
            _request = service.files().get_media(fileId = file_id)

            _path = os.path.join("C:/Users/AYUSH/Desktop/FileSummarizer\downloads", filename)

            _fh = io.FileIO(_path, 'wb')

            _downloader = MediaIoBaseDownload(_fh, _request)

            _done = False

            while not _done:
                _status, _done = _downloader.next_chunk()

            return _path
        
        except Exception as ex:
            print("Exception is: ", str(ex))
            return None

    
_service = AuthenticatorService().authenticate_drive()
print("Service created :", _service)
_files = AuthenticatorService().list_files(_service, config.folder_id)
print ("files are:", _files)


