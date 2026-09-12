from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="Customer API")


DATABASE = "customers.db"


# -------------------------
# Database
# -------------------------

def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


create_table()


# -------------------------
# Pydantic Models
# -------------------------

class CustomerCreate(BaseModel):
    name: str
    balance: float


class Customer(CustomerCreate):
    id: int


# -------------------------
# GET /
# -------------------------

@app.get("/")
def home():
    return {
        "message": "Customer API is running"
    }


# -------------------------
# POST /customers
# -------------------------

@app.post("/customers", response_model=Customer)
def create_customer(customer: CustomerCreate):

    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO customers (name, balance)
        VALUES (?, ?)
        """,
        (customer.name, customer.balance)
    )

    customer_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return {
        "id": customer_id,
        "name": customer.name,
        "balance": customer.balance
    }


# -------------------------
# GET /customers
# -------------------------

@app.get("/customers", response_model=list[Customer])
def get_customers():

    connection = get_connection()

    rows = connection.execute(
        "SELECT id, name, balance FROM customers"
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]


# -------------------------
# GET /customers/{id}
# -------------------------

@app.get("/customers/{customer_id}", response_model=Customer)
def get_customer(customer_id: int):

    connection = get_connection()

    row = connection.execute(
        """
        SELECT id, name, balance
        FROM customers
        WHERE id = ?
        """,
        (customer_id,)
    ).fetchone()

    connection.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return dict(row)


# -------------------------
# PUT /customers/{id}
# -------------------------

@app.put("/customers/{customer_id}", response_model=Customer)
def update_customer(
    customer_id: int,
    customer: CustomerCreate
):

    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE customers
        SET name = ?, balance = ?
        WHERE id = ?
        """,
        (
            customer.name,
            customer.balance,
            customer_id
        )
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    connection.close()

    return {
        "id": customer_id,
        "name": customer.name,
        "balance": customer.balance
    }


# -------------------------
# DELETE /customers/{id}
# -------------------------

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):

    connection = get_connection()

    cursor = connection.execute(
        """
        DELETE FROM customers
        WHERE id = ?
        """,
        (customer_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    connection.close()

    return {
        "message": "Customer deleted successfully",
        "id": customer_id
    }