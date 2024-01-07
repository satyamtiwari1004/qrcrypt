import dropbox
import os
import datetime




class TransferData:
    def __init__(self):
        self.access_token = ''
    def upload_file(self, strpath):
        dbx =dropbox.Dropbox(self.access_token)
        head, tail = os.path.split(strpath)
        t1=datetime.date.today()
        file_to2="/"+str(t1)+"/"+tail
        with open(strpath, 'rb') as f:
            dbx.files_upload(f.read(), file_to2,mode=dropbox.files.WriteMode.overwrite)
        
        return file_to2 
    def download_file(self,fileto1):
        try:
            dbx =dropbox.Dropbox(self.access_token)
            path="C:/QrCrypt"+fileto1
            head, tail = os.path.split(path)
            self.createdir(head)
            with open(path, "wb") as f:
                    metadata, res = dbx.files_download(path=fileto1)
                    f.write(res.content)
            return path
        except OSError:
            pass
    def createdir(self,path):
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            pass
