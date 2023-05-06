from pydantic import BaseModel

class Card(BaseModel):
    cor_fundo: str
    cor_texto: str
    fonte: str
