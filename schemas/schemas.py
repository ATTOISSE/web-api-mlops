from pydantic import BaseModel

class User(BaseModel):
    email: str
    nom: str
    prenom: str
    classe: str
    
    class Config:
        orm_mode = True
        from_attributes = True