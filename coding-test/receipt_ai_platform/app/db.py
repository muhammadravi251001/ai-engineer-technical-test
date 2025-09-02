import sqlite3
from typing import List, Dict, Any

DB_NAME = "receipts.db"

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS receipts (
    id INTEGER PRIMARY KEY,
    item TEXT,
    quantity INTEGER,
    unit_price REAL,
    price REAL,
    merchant TEXT,
    date TEXT
);
"""

INSERT_RECEIPT_QUERY = """
INSERT INTO receipts (item, quantity, unit_price, price, merchant, date)
VALUES (?, ?, ?, ?, ?, ?);
"""


def init_db(db_name: str = DB_NAME) -> None:
    with sqlite3.connect(db_name) as conn:
        conn.execute(CREATE_TABLE_QUERY)


def insert_receipt(
    items: List[Dict[str, Any]], merchant: str, date: str, db_name: str = DB_NAME
) -> None:
    values = [
        (i["item"], i["quantity"], i["unit_price"], i["price"], merchant, date)
        for i in items
    ]
    with sqlite3.connect(db_name) as conn:
        conn.executemany(INSERT_RECEIPT_QUERY, values)