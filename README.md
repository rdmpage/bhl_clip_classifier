# BHL Clip Classifier

This is a slight reworking of Mike Trizna’s [BHL Clip Classifier](https://huggingface.co/spaces/MikeTrizna/bhl_clip_classifier). It is designed to be run locally.

## Install

### Step 1: Create a Python virtual environment

```
python3 -m venv .venv 
source .venv/bin/activate
```

### Step 2: Install requirements

```
pip install -r requirements.txt
```

### Step 3: Run

```
python app.py
```

The first time you run the app it will download the model from Huggingface. The app will be available in your browser at http://127.0.0.1:7860

![Screenshot](https://github.com/rdmpage/bhl_clip_classifier/raw/main/screenshot.png)

