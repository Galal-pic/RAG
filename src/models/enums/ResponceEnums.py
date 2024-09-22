from enum import Enum

class ResponceSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_VALIDATE_NOT_SUPPORTED = "file_validate_not_supported"
    FILE_SIZE_LIMIT_EXCEEDED = "file_size_limit_exceeded"
    FILE_UPLOAED_SUCCESS = "file_aploaed_success"
    FILE_UPLOAED_FAILED = "file_upload_failed"
    PROCESSING_SUCCESS = "processing_success"
    PROCESSING_FAILED = "processing_failed"
