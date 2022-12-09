from transformers import pipeline
import gradio as gr
import time

pipe= pipeline(model="YuhangDeng123/whisper-small-hi")

def transcribe(audio, state=""):
    text = pipe(audio)["text"]
    state += text + " "
    return state, state

gr.Interface(
    title="Whisper-Small Online Cantonese Recognition",
    fn=transcribe, 
    inputs=[
        gr.Audio(source="microphone", type="filepath", streaming=True), 
        "state"
    ],
    outputs=[
        "textbox",
        "state"
    ],
    live=True).launch()