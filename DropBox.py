import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BDiuU5vnyDFZAauL2V90ZUdOGvmu5GjLEJrgjgUNd1AN0YPxakTvHApUslH3VsBn8h7-AIDQcBN7uvQCk4Zj6-DQOQO1nzavaANSujgwIWAvUxlEJ3gbQ5FpSucA-QskYo68IJwLNYu_'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer')
    file_to = input('Enter the file path to upload to in your dropbox')  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()