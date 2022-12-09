# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:37:44 2022

@author: Kenneth
"""

from transformers import pipeline
import gradio as gr
from pytube import YouTube
from datasets import Dataset, Audio
import os
from moviepy.editor import AudioFileClip
import time

pipe = pipeline(model="YuhangDeng123/whisper-small-hi")  # change to "your-username/the-name-you-picked"

def transcribe(audio):
    text = pipe(audio)["text"]
    return text

with gr.Blocks() as demo:
    gr.Markdown("Whisper-Small Cantonese Recognition")
    with gr.Row():
        with gr.TabItem("Upload An Audio File"):
            upload_file = gr.Audio(source="upload", type="filepath",label="Upload An Audio File")
            upload_button = gr.Button("Submit")
            upload_outputs = [gr.Textbox(label="Recognized result from uploaded audio file"),]
    with gr.Row():
        with gr.TabItem("Record from Microphone"):
            record_file = gr.Audio(source="microphone", type="filepath",label="Record from microphone")
            record_button = gr.Button("Submit")
            record_outputs = [gr.Textbox(label="Recognized result from Microphone"),]  
    upload_button.click(
        fn=transcribe,
        inputs=upload_file,
        outputs=upload_outputs,
    )
    
    record_button.click(
        fn=transcribe,
        inputs=record_file,
        outputs=record_outputs,
    )    
demo.launch()