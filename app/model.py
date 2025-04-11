from pydantic import BaseModel
from typing import List, Optional

# Define the data model for the document extraction request
class DocumentField(BaseModel):
    FieldName: str
    FieldType: Optional[str] = None
    FieldDescription: Optional[str] = None

class DocumentExtractionRequest(BaseModel):
    DocumentId: str
    DocumentType: str
    ExpectedFields: List[DocumentField]
    FileContent: str
    FileName: str
    MimeType: str
