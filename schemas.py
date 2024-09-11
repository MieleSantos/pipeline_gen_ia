from pydantic import BaseModel,EmailStr,field_validator,PositiveFloat,PositiveInt
from datetime import datetime
from enum import Enum

class ProdutoEnum(str,Enum):
    produto_1 = "ZapFlow com Gemini"
    produto_2 = "ZapFlow com chatGPT"
    produto_3 = "ZapFlow com Llama3.0"

class Vendas(BaseModel):
    email: EmailStr
    data_venda: datetime
    hora_venda: datetime
    valor_venda: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
    
    @field_validator("produto")
    def categoria_deve_estar_no_enum(csl, v):
        return v    
