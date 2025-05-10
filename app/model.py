from pydantic import BaseModel
from typing import List, Optional, Dict

# Define the data model for the document extraction request

class Rule(BaseModel):
    RuleType: str  # e.g., "name_match", "over_18"
    RuleDescription: str
    MatchType: Optional[str] = None  # e.g., "exact", "partial"

class DocumentField(BaseModel):
    FieldName: str
    FieldType: Optional[str] = None
    FieldDescription: Optional[str] = None
    FormValue: Optional[str] = None
    FieldRules: List[Rule]
    # Rules: Optional[List[Rule]] = []

class DocumentExtractionRequest(BaseModel):
    DocumentId: str
    DocumentType: str
    ExpectedFields: List[DocumentField]
    FileContent: str
    FileName: str
    MimeType: str

{'document_type': 'Birth Certificate', 
 'extracted_fields': 
 [{'FullName': 'OLUWATOYIN OMOLARAJO', 
   'extracted_value': 'OLUWATOYIN OMOLARAJO', 
   'rules_check': [], 
   'confidence_score': 1.0}, 
   {'DateOfBirth': '4th May 2024', 'extracted_value': '4th May 2024', 'rules_check': [{'date_match': 'pass'}, {'over_18': 'fail'}], 'confidence_score': 0.8}, {'IssuingAuthority': 'Ondo State of Nigeria', 'extracted_value': 'Ondo State of Nigeria', 'rules_check': [{'authority_match': 'pass'}], 'confidence_score': 1.0}, {'PlaceOfBirth': 'ILE-OLUJI', 'extracted_value': 'ILE-OLUJI', 'rules_check': [], 'confidence_score': 1.0}], 'confidence_score': 0.8, 'is_valid': False, 
 'validation_message': 'Date of Birth is not over 18 years old'}