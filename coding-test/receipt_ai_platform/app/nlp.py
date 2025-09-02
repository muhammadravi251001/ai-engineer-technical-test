import sqlite3
import textwrap
from dotenv import load_dotenv
from google import genai
from google.genai import types
from db import DB_NAME

load_dotenv()
MODEL_NAME = "gemini-1.5-flash"

client = genai.Client()

SCHEMA = textwrap.dedent("""
    CREATE TABLE receipts (
        id INTEGER PRIMARY KEY,
        item TEXT,
        quantity INTEGER,
        unit_price REAL,
        price REAL,
        date TEXT,
        merchant TEXT
    );
""")

EXAMPLES = textwrap.dedent("""
    Example rows in receipts table:
    id: 1, item: Grilled chicken sandwich, quantity: 2, unit_price: 8.5, price: 17.0, date: 11-04-2025, merchant: Your Company Inc.
    id: 2, item: Caesar salad, quantity: 1, unit_price: 7.0, price: 7.0, date: 11-04-2025, merchant: Your Company Inc.
    id: 3, item: Soft drinks, quantity: 3, unit_price: 2.0, price: 6.0, date: 11-04-2025, merchant: Your Company Inc.
""")


def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        ),
    )
    return response.text.strip()


def generate_sql(question: str) -> str:
    prompt = textwrap.dedent(f"""
        You are a text-to-SQL generator on a food receipts database.

        Here is the SQLite schema:
        {SCHEMA}

        Here are some example rows:
        {EXAMPLES}

        Generate a valid SQL query to answer this question:
        {question}

        Rules:
        - Only return the SQL query.
        - Do not include explanations or markdown formatting.
    """)
    sql = ask_gemini(prompt).strip("`")
    if sql.lower().startswith("sql"):
        sql = sql[3:].strip()
    return sql


def run_sql(question: str) -> str:
    sql_query = generate_sql(question)
    print(f"Generated SQL:\n{sql_query}")

    try:
        with sqlite3.connect(DB_NAME) as conn:
            cur = conn.cursor()
            cur.execute(sql_query)
            results = cur.fetchall()
    except Exception as e:
        results = [("SQL Error", str(e))]

    # Format into natural language
    format_prompt = textwrap.dedent(f"""
        You are a natural language formatter.

        The user asked: {question}
        The raw SQL result is: {results}

        Write a concise, human-friendly answer.
    """)
    return ask_gemini(format_prompt)