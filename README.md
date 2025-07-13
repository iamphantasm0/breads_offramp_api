---

# 🥖 Bread Africa Offramp API (FastAPI Wrapper)

A fully-featured **FastAPI backend** that wraps [Bread Africa’s Universal Offramp API](https://bread.africa). This project provides clean HTTP endpoints for quoting, transferring, and tracking crypto-to-fiat offramps using Bread's infrastructure.

> ⚠️ This project is independently built and **not affiliated with Bread Africa**.

---

## 🧩 Features

* ✅ Generate real-time crypto-to-cash quotes
* 💸 Create off-ramp transfers directly to fiat bank accounts
* 🔎 Track transfer status via unique reference
* 🧾 View historical transfer data by wallet address
* 🏦 Lookup bank accounts and fetch supported institutions
* 🌐 List supported tokens, currencies, and blockchains
* 📑 Swagger UI ready out-of-the-box

---

## 📂 Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── config.py            # App settings & Bread API base URL
│   ├── logger.py            # Logger setup
│   ├── models.py            # Pydantic models for payloads & responses
│   ├── offramp_client.py    # Bread API logic
│   └── routes.py            # FastAPI endpoints
├── main.py                  # App entrypoint & lifespan management
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone & Install

```bash
git clone https://github.com/your-username/bread-offramp-fastapi.git
cd bread-offramp-fastapi
pip install -r requirements.txt
```

### 2. Configure `.env` or use export:

```env
BREAD_API_BASE_URL=https://api.bread.africa
```

### 3. Run the API

```bash
uvicorn main:app --reload
```

Then visit:

* Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Available Endpoints

All routes are prefixed with `/offramp`.

| Method | Endpoint                     | Description                             |
| ------ | ---------------------------- | --------------------------------------- |
| `POST` | `/quote`                     | Get a crypto-to-fiat quote              |
| `POST` | `/transfer`                  | Create a transfer from crypto to fiat   |
| `POST` | `/lookup-account`            | Lookup bank account details             |
| `GET`  | `/status/{reference}`        | Fetch the status of a transfer          |
| `GET`  | `/get-transfers`             | Fetch all past transfers for an address |
| `GET`  | `/tokens?blockchain=...`     | Get tokens supported by a blockchain    |
| `GET`  | `/currencies`                | List supported fiat currencies          |
| `GET`  | `/blockchains`               | List supported blockchains              |
| `GET`  | `/institutions?currency=NGN` | Get banks supported for a currency      |

All endpoints return a consistent `ApiResponse`.

---

## 🧱 Models (Defined in `models.py`)

* `QuoteRequestPayload`
* `TransferRequestPayload`
* `LookupPayload`
* `ApiResponse`

---

## 🧼 Notes

* `offramp_client` is a singleton stored in `app.state` during app lifespan.
* Timeout is 30s for read, 60s for connect — adjust via `offramp_client.py`.
* Handles both `httpx.RequestError` and `httpx.HTTPStatusError` gracefully with logs.

---

Got it. Here’s a clean closing section you can add under the README to reference your bot:

---

## 🤖 Telegram Bot

This API powers a Telegram bot that makes crypto offramps even more accessible.

**Try it here:** [@bread\_offramp\_bot](https://t.me/bread_offramp_bot)

> WhatsApp version coming soon.

---

Let me know if you want to add a separate section for architecture, bot commands, or demo GIFs later.



## 👤 Author

**Zero (Phantasm)**
Telegram: [@iamphantasm0](https://t.me/iamphantasm0)
GitHub: [iamphantasm0](https://github.com/iamphantasm0)
Twitter: [@iamphantasm0](https://twitter.com/iamphantasm0)

---

## 📛 Disclaimer

Bread is a third-party service. This backend is for **educational or internal development** purposes.
For official documentation, visit [Bread Africa](https://bread.africa).

---
