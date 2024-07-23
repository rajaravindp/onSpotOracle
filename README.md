# Real Time Speech-to-Text-to-Text AI Assistant

**Combine speech recognition with AI-powered text generation** <br>
This application is capable of listening to user speech, transcribe it in real time and generate an AI response. <br>

![image](https://github.com/user-attachments/assets/99d83bca-05cc-4a35-b9ce-3597d8d59eee)

**Features**
- Real-time speech recognition
- Text generation
- Continuous interaction loop

**Requirements**
- Python 3.8 or higher
- llama-cpp-python
- llama-cpp-agent
All other requirements can be found installed using the environments.env file using: <br>
*conda env create -f environment.yml*

**Setup**
Configuring Llama-cpp and CMake is a pain. I shall upload a seperate tutorial on configuration.
- Install the required packages
-  Download model params and metadata from HuggingFace and place it into a separate /models dir. 
-  Run the script

**Note**
- Ensure your microphone is properly connected and configured.
- The application runs continuously until interrupted
