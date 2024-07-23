import speech_recognition as sr
from llama_cpp import Llama
from llama_cpp_agent.providers import LlamaCppPythonProvider

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize llama-cpp with your model
llama_model = Llama(r"C:\Users\aravind.palepu\Documents\audio\mymodels\mistral-7b-instruct-v0.2.Q5_K_S.gguf", n_batch=1024, n_threads=10, n_gpu_layers=40)

def main():
    try:
        while True:
            with sr.Microphone() as source: # Audio source: default mic
                print("Please speak into the microphone...")
                # Adjusting for ambient noise 
                recognizer.adjust_for_ambient_noise(source)
                # Listen for audio input
                audio = recognizer.listen(source)

            try:
                # Recognize speech
                text = recognizer.recognize_google(audio)
                print("Audio transcription: ", text)

                # Response gen
                prompt = f"User said: {text}\nAI response:"
                response = llama_model(prompt, max_tokens=100, stop=["User said:", "\n"], echo=False)
                
                print("AI response:", response['choices'][0]['text'].strip())

            except sr.UnknownValueError:
                print("Audio not recognized")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

    except KeyboardInterrupt:
        print("Stopping application.")

if __name__ == "__main__":
    main()
