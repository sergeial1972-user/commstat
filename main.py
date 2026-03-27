#imports
import gradio as gr
import checker

with gr.Blocks() as ui:  # ← Добавьте ()
    url = gr.Textbox(label="URL", placeholder="enter url")
    result = gr.Textbox(label="Result", placeholder="enter result")
    check_btn = gr.Button("Check")
    check_btn.click(fn=checker.check, inputs=url, outputs=result)

ui.launch()
