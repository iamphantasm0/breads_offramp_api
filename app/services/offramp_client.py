import httpx
from fastapi import HTTPException
from watchfiles import awatch

from app.config import settings
from app.models import QuoteRequestPayload, TransferRequestPayload, LookupPayload, History
from app.logger import logger

class OfframpClient:
    def __init__(self, base_url: str):
        # Define a longer timeout (30 seconds for read, 60 for connect)
        timeout = httpx.Timeout(30.0, connect=60.0)

        self._client = httpx.AsyncClient(
            base_url=base_url,
            headers={'Content-Type': 'application/json'},
            timeout=timeout # Apply the new timeout
        )

    async def close(self):
        """Closes the HTTP client sessions."""
        await self._client.aclose()

    async def _request(self, method: str, endpoint: str, **kwargs):
        """Internal helper to make requests and handle errors."""
        try:
            response = await self._client.request(method, endpoint, **kwargs)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(f"API returned an error: {e.response.status_code} - {e.response.text}")
            raise HTTPException(status_code=e.response.status_code, detail=e.response.json())
        except httpx.RequestError as e:
            logger.error(f"Network request to {e.request.url} failed.", exc_info=True)
            raise HTTPException(status_code=503, detail=f"Service unavailable: A network error occurred. See server logs for details.")

    async def fetch_quote(self, payload: QuoteRequestPayload):
        return await self._request("POST", "/get-quote", json=payload.model_dump())

    async def fetch_history(self, address: str):
        return await self._request("GET", "/get-transfers", params={"address": address})

    async def execute_transfer(self, payload: TransferRequestPayload):
        return await self._request("POST", "/create-transfer", json=payload.model_dump())

    async def fetch_status(self, reference: str):
        return await self._request("GET", "/get-status", params={"reference": reference})

    async def fetch_tokens(self, blockchain_id: int):
        return await self._request("GET", "/get-tokens", params={"blockchain": blockchain_id})

    async def fetch_currencies(self):
        return await self._request("GET", "/get-currencies")

    async def lookup_institution(self, payload: LookupPayload):
        """
        Looks up/verifies bank account details before a transfer.
        """
        url = f"{settings.BREAD_API_BASE_URL}/lookup-institution"
        return await self._request("POST", url, json=payload.model_dump())

    async def fetch_institutions(self, currency: str):
        """
        Fetches the list of supported institutions for a given currency.
        """
        url = f"{settings.BREAD_API_BASE_URL}/get-institutions"
        return await self._request("GET", url, params={"currency": currency})

    async def fetch_blockchains(self):
        return await self._request("GET", "/get-blockchains")

# Create a single instance to be managed by the app's lifespan
offramp_client = OfframpClient(base_url=settings.BREAD_API_BASE_URL)