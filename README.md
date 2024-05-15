# Speech-Recognition-App
Python Speech Recognition Desktop Application with using Electron Js for designing

# Voice-Translator | Development of speech recognition software in python
### INTRODUCTION
Speech recognition is the process of converting spoken language into written text. Python provides various libraries to implement speech recognition functionality. One popular library is the SpeechRecognition library. It supports multiple speech recognition engines, including Google Cloud-Based Speech Recognition, Sphinx, and Wit.ai. In this introduction, I'll provide an overview of speech recognition functionalities and outline the libraries commonly used in Python for conversion.


### Architecture of software and structure
It includes the following tasks:
- Input Speech through a microphone or audio files;
- Speech Recognition. Utilize a speech recognition engine;
- Language Detection. Libraries like Google Cloud Translation API can assist with language detection;
- Translation. Using translation service or library to translate the recognized text;
- Text-to-Speech Conversion;
- User Interface. Design an intuitive and user-friendly interface for our app;
- Error Handling;
- Integration and Deployment;
- Testing and Improvement.
  
![how it works](https://github.com/GornizolCoder-GC/LIVE-Translator/assets/82934751/3633e343-2d9c-4249-9fff-d4dc2b58bfaa)


## Development of the application

I used ElectronJs, a JS framework, to create the user interface, and it helped me communicate using Python code. Interprocess Communication (IPC) between Electron and Python. Electronic applications can execute Python scripts using a child process. And you can see how they interact with each other below:

![IPC](https://github.com/GornizolCoder-GC/LIVE-Translator/assets/82934751/1da3bbed-0c5c-4fb1-9c6a-b8f3a1af8617)


## Software Interface

It is a desktop application. It is including 3 pages. They are **/Home**,  **/Main**,  **/Translation**.  
![designsoftware](https://github.com/GornizolCoder-GC/LIVE-Translator/assets/82934751/8a9381b6-31e7-4136-9c83-9db32a1fb8b9)

## Programm requirements

Please read below before starting this project :
- Python: Ensure that Python is installed on your system;
- Python Libraries: Install the required Python libraries using pip:
- To set up the Electron.js development environment, you'll need Node.js and npm (Node Package Manager) installed.
- Install the required Electron.js dependencies 	
- Electron.js communicates with Python scripts using the ’child_process’ module. Ensure that your operating system has Python properly configured as an executable and added to the system's PATH environment variable. 

## How to run this project ?

To use this program, we should write:
```terminal
> npm start  in terminal.
```
But if we need python library, we have to be in **_python environment_!** and then run above command.

```terminal
> .env\Scripts\activate  in terminal.
```

**Remember!**

For the actual operation of the application, we can say something only after the microphone icon appears on the taskbar menu after pressing the recorder button:

![microphoneicon](https://github.com/GornizolCoder-GC/LIVE-Translator/assets/82934751/3bfb138c-bbb3-49e3-b6e6-af76f6b366d6)


