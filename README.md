# conversationalrpg

## Getting Started

Clone the repo:

```
git clone https://github.com/feiIin/conversationalrpg.git
```

Install the dependencies using `bash setup.sh`. Alternatively, find the installation instructions in the next section below:

## Installation

We use Python=3.7 for our framework. Some of the main libraries require by each component are:

- ASR `SpeechRecognition`
- DM ``
- NLG 
- NLU `rasa, spacy`
- TTS `gtts, playsound`
- DB `pymongo, bs4`
- bot `pynput`

To have the full pipeline running, follow the steps: 
```
conda create --name witchat python=3.7 -y
eval "$(conda shell.bash hook)"
conda activate witchat

pip install -r requirements.txt

# Refer https://stackoverflow.com/a/60599224/3776827
conda install -c tdido gtts-token
```

For gtts to work properly, you might have to install `mpg321`. 

- On mac: `brew install mpg321`
- On ubuntu: `apt-get install mpg321`

For Mac to properly make pyaudio work:
- brew install portaudio
- pip install pyaudio