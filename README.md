# rder Management Microservice

A lightweight microservice built with **FastAPI** and **PostgreSQL/SQLite** for managing customer orders. Supports features like order creation, status updates, filtering, pagination, and more.

---

## Features

- Create and retrieve customer orders
- Update order status (e.g. pending → shipped)
- List orders with **pagination** and **filtering**
- API-ready with Pydantic validation
- Easy to deploy and extend

---

## Tech Stack

| Layer         | Technology         |
|---------------|--------------------|
| Framework     | FastAPI            |
| ORM           | SQLAlchemy         |
| DB            | SQLite (local), PostgreSQL (prod-ready) |
| Validation    | Pydantic           |
| Dev Tools     | Uvicorn, GitHub    |

---

## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/shaun33016/order-management
cd order-management
```
### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
uvicorn app.main:app --reload
```
API will be live at: http://127.0.0.1:8000/docs