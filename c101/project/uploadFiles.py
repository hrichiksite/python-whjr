import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

access_token = '00000000000000'
transferData = TransferData(access_token)

file_from = input('Enter the file path to upload: ')
file_to = input('Enter the full path to upload to dropbox: ')
local_path = os.path.join(os.getcwd(), file_from)
relative_path = os.path.relpath()

# API v2
transferData.upload_file(file_from, file_to)
    
print('File uploaded successfully.')


