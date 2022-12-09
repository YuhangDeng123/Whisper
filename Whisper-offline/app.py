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
import requests

pipe = pipeline(model="YuhangDeng123/whisper-small-hi")  # change to "your-username/the-name-you-picked"

def transcribe(audio):
    text = pipe(audio)["text"]
    return text

def DownloadFile(mp3_url):
    file_name = 'test.mp3'
    res = requests.get(mp3_url + "?raw=true")
    music = res.content
    # 获取文件地址
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'ab') as file: #保存到本地的文件名
        file.write(res.content)
        file.flush()
    return file_path

def convert_to_wav(path):
    
    audio = AudioFileClip(path)
    audio_frame = audio.subclip(0, -2)
    audio_frame.write_audiofile(f"audio.wav")
    return f"audio.wav"   
     
def url_transcribe(url):
    path = DownloadFile(url)
    path_wav = convert_to_wav(path)
    audio_dataset = Dataset.from_dict({"audio": [path_wav]}).cast_column("audio", Audio(sampling_rate=16000))
    text = pipe(audio_dataset["audio"])
    os.remove(path)
    return text[0]["text"]



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
    with gr.Row():
        with gr.TabItem("Transcribe from GitHub URL"):
            url = gr.Text(max_lines=1, label="Transcribe from GitHub URL")
            Github_button = gr.Button("Submit")
            Github_outputs = [
                gr.Textbox(label="Recognized speech from GitHub URL")
            ]   
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
    Github_button.click(
    fn=url_transcribe,
    inputs=url,
    outputs=Github_outputs,
    )
demo.launch()