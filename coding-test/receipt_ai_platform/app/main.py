import gradio as gr
from ocr import extract_receipt_text, parse_receipt
from db import init_db, insert_receipt
from nlp import run_sql
from datetime import datetime

init_db()


def upload_receipt(path: str) -> dict:
    text = extract_receipt_text(path)
    data = parse_receipt(text)
    insert_receipt(
        items=data["items"],
        merchant=data["merchant"],
        date=data["date"] or datetime.now().strftime("%d-%m-%Y")
    )
    return data


def ask_ai(question: str) -> str:
    if question.strip():
        results = run_sql(question)
        return results
    return "Please add the question first."


def ask_ai_with_status(question: str):
    yield "Processing your question..."
    result = run_sql(question)
    yield result


with gr.Blocks() as demo:
    gr.Markdown("## Upload your food receipt")
    with gr.Row():
        img_input = gr.Image(type="filepath")
        output = gr.JSON()
    upload_btn = gr.Button("Upload")
    upload_btn.click(upload_receipt, inputs=img_input, outputs=output)

    gr.Markdown("## Ask about your receipts")
    question_input = gr.Textbox(label="Ask a question")
    answer_output = gr.Markdown()
    ask_btn = gr.Button("Ask")
    ask_btn.click(ask_ai_with_status, inputs=question_input, outputs=answer_output)

demo.launch(server_name="0.0.0.0", server_port=7860)