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

## Usage

To use this via an API you POST a request to `http://127.0.0.1:7860/gradio_api/call/shot`. The request is a JSON document of the form:

```
{
    "data": [
        {
            "path": "\/Users\/rpage\/Development\/bhl_clip_classifier\/newmexicobotani00newmb_0084.jpg"
        },
        "blank;text;illustration"
    ]
}
```

The document has the absolute path to the image, and a list of “;” delimited labels.

The result of POSTing this document is a response that contains an `event_id`. This can then be used to create a URL to GET the actual result: `http://127.0.0.1:7860/gradio_api/call/shot/<event_id>`. The repsonse is [Server-Sent Events (SSE)](https://en.wikipedia.org/wiki/Server-sent_events) format. The folloowing PHP code can parse the result of the GET call:

```
function parse_gradio_sse($raw) {
    // split into lines
    $lines = preg_split("/\r\n|\n|\r/", trim($raw));

    $capture = false;
    $json_line = null;

    foreach ($lines as $line) {
        $line = trim($line);

        if ($line === "event: complete") {
            // we found the block we care about
            $capture = true;
            continue;
        }

        if ($capture && strpos($line, "data: ") === 0) {
            $json_line = substr($line, strlen("data: "));
            break;
        }
    }

    if ($json_line === null) {
        return null;
    }

    return json_decode($json_line, true);
}
```

