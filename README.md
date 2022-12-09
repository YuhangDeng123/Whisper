# Whisper (For Cantonese)
The file description of ID2223_Lab2 and the answers of Task 2.
# Whisper-offline
The is the code of inference program (Hugging Face Space), which can achieve: 1. Allow users to upload audio files locally and output transcribed text. 2. Allow users to speak into the microphone and transcribe what he/she says. 3. Allow users to paste the URL of the audio file, and transcribe what is spoken.
# Whisper-online
The is the code of inference program (Hugging Face Space), which can achieve: Allows users to speak into a microphone and output transcribed text online in real time.
# whisper-small-hi
This is a whisper-small model that has been fine-tuned and trained, and can be used to transcribe Cantonese and output text.
# zh-HK-radio
These are some Cantonese audio clips that can be used to test the hugging face program to verify the effectiveness of the model.
# whisper_feature_pipeline.ipynb / .py
The is the feature engineering pipeline which can be used to run feature engineering on CPUs
# whisper_training_pipeline.ipynb / .py
The is the training pipeline which can be used to fine-tune and train the whisper model on GPUs
# Hugging Face Spaces public URL of Whisper-offline function for Interactive UI.
https://huggingface.co/spaces/YuhangDeng123/Whisper-offline
# Hugging Face Spaces public URL of Whisper-online function for Interactive UI.
https://huggingface.co/spaces/YuhangDeng123/Whisper-online
# Hugging Face Spaces public URL of fine-tuned and trained whisper-small model for cantonese.
https://huggingface.co/YuhangDeng123/whisper-small-hi



# The answers of Task 2 - Describe the ways that can be used to improve model performance.(The model-centric approaches)
1. Tuning the hyperparameters: We can adjust the batch size, learning rate, and max steps number to optimize the model. First, we can adjust the batch size. As the batch size increases, the speed at which the model processes the same amount of data during training would increase, so the model can converge faster, and it is easy to reach local optimum. Since different local optimum points have different precision, adjusting the batch size can find the local optimum point with the best system performance. Dynamically adjust the batch size, making the batch size larger in the early stage of training can make the convergence faster, and making the batch size smaller in the later stage can improve the convergence accuracy and get better performance. Secondly, we can adjust the learning rate of the model to improve the performance of the model. A larger learning rate can increase the convergence speed, and is conducive to jumping out of the local optimum, but it will also make the system swing in a larger area near the optimal value. A smaller learning rate will lead to slower convergence and may be trapped in a local optimum, but better convergence accuracy can be obtained. In order to improve the performance of the system, the learning rate can be dynamically adjusted. In the early stage of training, a larger learning rate is used to accelerate convergence, and in the later stage of training, a smaller learning rate is used to approach the optimal point. Finally, We can also adjust the max steps number to improve the performance of the system. By increasing the max steps number, we will find that the validation loss will continue to decrease and finally stabilize. This indicates that the system is approaching the convergence point. If we continue to increase the step number at this time, it will cause the system to overfit on the training set, which will reduce the performance of the system. Therefore, fine-tuning the max steps number can be used to find the optimal convergence point and improve system performance.
2. Change the fine-tuning model architecture: We used the whisper-small model this time. Whisper has launched a total of six models that can be used for speech recognition. By choosing a more advanced model such as whisper-medium or whisper-large, the performance of the system can be improved, but this will have higher requirements on the graphics card and will take more time. Wav2Vec 2.0 is another speech recognition model that may be used to improve system performance.

# The answers of Task 2 - Describe the ways that can be used to improve model performance.(The data-centric approaches)
1. Tun
2. 



