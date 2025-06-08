# Order Management Microservice

A lightweight microservice built with **FastAPI** and **SQLite** for managing customer orders. Supports features like order creation, status updates, filtering, pagination, and more.

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
| DB            | SQLite             |
| Validation    | Pydantic           |
| Dev Tools     | Uvicorn, GitHub    |
| Deployment    | Docker, AWS EC2    |

---

## Setup Instructions (Local)

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

---

## Running with Docker

### 1. Build Docker Image
```bash
docker build -t order-management .
```

### 2. Run the Container
``` bash
docker run -d -p 8000:8000 order-management
```
Visit: http://localhost:8000/docs

---

## Deploy on AWS EC2

Public IP: `http://<your-ec2-ip>:8000/docs`
(Replace with your real EC2 IP)

Ensure port 8000 is open in EC2 security group

---

## API Endpoints

---

| Method        | Endpoint              | Description                |
|---------------|-----------------------|----------------------------|
| POST          | `/orders/`            | Create a new order         |
| GET           | `/orders/{order_id}`  | Retrieve a specific order  |
| PUT           | `/orders/{order_id}`  | Update an order’s status   |
| GET           | `/orders/`            | List orders with filters   |

---

## Sample API Usage

### Create Order

**POST** `/orders/`

```json
{
  "customer_name": "Ramesh",
  "item_name": "TV",
  "quantity": 1,
  "status": "pending"
}

```
----------
### Get Order by ID

**GET** `/orders/1`

```json
{
  "customer_name": "Ramesh",
  "item_name": "TV",
  "quantity": 1,
  "status": "pending",
  "id": 4,
  "created_at": "2025-06-07T08:32:45.549545"
}
```

----------

### Update Order Status

**PUT** `/orders/1`

```json
{
  "status": "shipped"
}

```
----------

### List Orders with Pagination & Filtering

**GET** `/orders/?skip=0&limit=10&status=pending' \`

#### 🔍 Query Parameters:

-   `status`: Filter orders by status
    
-   `skip`: Number of records to skip (for pagination)
    
-   `limit`: Max number of records to return
    

#### Example Response:

```json
[
  {
    "customer_name": "Shaun",
    "item_name": "Books",
    "quantity": 10,
    "status": "pending",
    "id": 2,
    "created_at": "2025-06-07T07:31:34.175437"
  },
  {
    "customer_name": "Rajesh",
    "item_name": "Remote",
    "quantity": 1,
    "status": "pending",
    "id": 3,
    "created_at": "2025-06-07T07:55:09.038571"
  },
  {
    "customer_name": "Ramesh",
    "item_name": "TV",
    "quantity": 1,
    "status": "pending",
    "id": 4,
    "created_at": "2025-06-07T08:32:45.549545"
  }
]

```
---

## Running Tests

This project includes unit tests for core functionality like order creation, retrieval, status updates, and filtering.

To run the tests:

```bash
pytest
```

---

## Optional Features Implemented

-   Dockerized microservice
-   Deployed on AWS EC2

----------