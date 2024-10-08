from fastapi import FastAPI,APIRouter,Depends,UploadFile,status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings,Settings
from controllers import DataController 
from controllers import ProjectController
import aiofiles
from models import ResponceSignal
import logging
logger = logging.getLogger('uvicorn.error')

data_router  = APIRouter(
    prefix = '/api/v1/data',
    tags = ['api_v1','data']
)

@data_router.post('/upload/{project_id}')
async def upload_data(project_id : str,file:UploadFile,app_settings : Settings = Depends(get_settings)):
    # validate the file properties
    data_controller = DataController()
    is_valied,result_signal = data_controller.validate_uploaded_file(file=file)
    if not is_valied:
       return JSONResponse(
           status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": result_signal}
       )

    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = data_controller.generate_unique_filename(orig_file_name=file.filename , project_id=project_id)
    try:
        async with aiofiles.open(file_path, mode='wb') as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_SIZE):
                await f.write(chunk)
    except Exception as e:
          logger.error(f'Error while uploading file : {e}')
          return JSONResponse(
           status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": ResponceSignal.FILE_UPLOAED_FAILED }
       )

    return JSONResponse(
            content={"signal": ResponceSignal.FILE_UPLOAED_SUCCESS.value}
       )
        