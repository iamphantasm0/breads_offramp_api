from fastapi import APIRouter, Query, Path, Request
from app.models import QuoteRequestPayload, TransferRequestPayload, ApiResponse, LookupPayload

# Create a router to group all offramp related endpoints
router = APIRouter(prefix="/offramp", tags=["Universal Offramp"])

@router.post("/lookup-account", response_model=ApiResponse, tags=["Universal Offramp"])
async def lookup_bank_account(request: Request, payload: LookupPayload):
    """
    Verifies bank account details and returns the account holder's name.
    """
    return await request.app.state.offramp_client.lookup_institution(payload)

@router.post("/quote", response_model=ApiResponse, tags=["Universal Offramp"])
async def get_offramp_quote(request: Request, payload: QuoteRequestPayload):
    """Get an offramp quote to turn any crypto into cash."""
    return await request.app.state.offramp_client.fetch_quote(payload)

@router.post("/transfer", response_model=ApiResponse, tags=["Universal Offramp"])
async def create_offramp_transfer(request: Request, payload: TransferRequestPayload):
    """Create an offramp transfer to send crypto to a bank account."""
    return await request.app.state.offramp_client.execute_transfer(payload)

@router.get("/status/{reference}", response_model=ApiResponse, tags=["Universal Offramp"])
async def get_transfer_status(
    request: Request,
    reference: str = Path(..., example="ACT_y7ehum289f5woy8")
):
    """Get the status of a specific transfer using its reference ID."""
    return await request.app.state.offramp_client.fetch_status(reference)

@router.get("/tokens", response_model=ApiResponse, tags=["Supported Assets"])
async def get_supported_tokens(
    request: Request,
    blockchain: int = Query(..., example=8453)
):
    """Get a list of supported tokens for a specific blockchain."""
    return await request.app.state.offramp_client.fetch_tokens(blockchain)

@router.get("/institutions", response_model=ApiResponse, tags=["Supported Assets"])
async def get_supported_institutions(
    request: Request,
    currency: str = Query(..., example="NGN", description="The currency to get supported institutions for (e.g., NGN, KES).")
):
    """
    Get a list of supported financial institutions (banks) for a specific currency.
    """
    return await request.app.state.offramp_client.fetch_institutions(currency)

@router.get("/currencies", response_model=ApiResponse, tags=["Supported Assets"])
async def get_supported_currencies(request: Request):
    """Get a list of supported fiat currencies for offramp."""
    return await request.app.state.offramp_client.fetch_currencies()

@router.get("/blockchains", response_model=ApiResponse, tags=["Supported Assets"])
async def get_supported_blockchains(request: Request):
    """Get a list of supported blockchains."""
    return await request.app.state.offramp_client.fetch_blockchains()