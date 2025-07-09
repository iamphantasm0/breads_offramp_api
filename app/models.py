from pydantic import BaseModel, Field
from typing import Optional, Any

# =================================================================
#                         NEW LOOKUP MODEL
# =================================================================
class LookupPayload(BaseModel):
    identifier: str = Field(..., example="2007761146", description="The 10-digit NUBAN account number.")
    institution: str = Field(..., example="090267", description="The official numeric code for the bank.")

# =================================================================
#                         REQUEST MODELS
# =================================================================
class OfframpQuoteRequest(BaseModel):
    currency: str = Field(..., example="NGN")

class QuoteRequestPayload(BaseModel):
    from_blockchain: int = Field(..., example=8453)
    from_token: str = Field(..., example="0x833589fcd6edb6e08f4c7c32d4f71b54bda02913")
    amount: float = Field(..., example=10)
    offramp: OfframpQuoteRequest

class Beneficiary(BaseModel):
    identifier: str = Field(..., example="2007761146")
    institution: str = Field(..., example="090267")
    name: str = Field(..., example="Adigwe, Oluwafiyibomi Chibuzor")

class OfframpTransferRequest(BaseModel):
    currency: str = Field(..., example="NGN")
    beneficiary: Beneficiary

class TransferRequestPayload(BaseModel):
    from_blockchain: int = Field(..., example=10)
    from_token: str = Field(..., example="0x0b2c639c533813f4aa9d7837caf62653d097ff85")
    amount: float = Field(..., example=10)
    offramp: OfframpTransferRequest

# =================================================================
#                         RESPONSE MODEL
# =================================================================
class ApiResponse(BaseModel):
    """A generic response model for the external API."""
    status: int
    message: str
    data: Optional[Any] = None