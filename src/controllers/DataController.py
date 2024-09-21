from .BaseController import BaseController
from fastapi import FastAPI,APIRouter,Depends,UploadFile
from models import ResponceSignal
from .ProjectController import ProjectController
import re
import os
class DataController(BaseController):
    def __init__(self):
        super().__init__()
    
    def validate_uploaded_file(self, file:UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False , ResponceSignal.FILE_TYPE_NOT_SUPPORTED.value
        if file.size > self.app_settings.FILE_MAX_SIZE * 1048676:
            return False, ResponceSignal.FILE_SIZE_LIMIT_EXCEEDED.value
        
        return True,ResponceSignal.FILE_UPLOAED_SUCCESS
    

    def generate_unique_filename(self,orig_file_name:str,project_id:str):
        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)
        cleaned_filename = self.get_clean_filename(orig_file_name=orig_file_name)
        new_filpath = os.path.join(project_path , random_key+"_"+cleaned_filename)
        while os.path.exists(new_filpath):
            random_key = self.generate_random_string()
            new_filpath = os.path.join(project_path , random_key+"_"+cleaned_filename)
        return new_filpath

    def get_clean_filename(self,orig_file_name:str):

        cleaned_filename = re.sub(r'[^\w.]','',orig_file_name.strip())
        cleaned_filename = cleaned_filename.replace(' ', '-')
        return cleaned_filename
