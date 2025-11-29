import gradio as gr
from transformers import pipeline

checkpoint = "openai/clip-vit-base-patch32"

classifier = pipeline(
    "zero-shot-image-classification",
    model=checkpoint
)

def shot(image, labels_text):
    if labels_text:
        labels = [lbl.strip() for lbl in labels_text.split(";") if lbl.strip()]
    else:
        labels = [
            'A page of printed text',
            'A page of handwritten text',
            'A blank page with no text',
            'A cover of a book',
            'A page of a book that contains a large illustration',
            'A page that features a table with multiple columns and rows',
        ]

    results = classifier(image, candidate_labels=labels)
    return {r["label"]: r["score"] for r in results}


demo = gr.Interface(
    fn=shot,
    inputs=[
        gr.Image(type="pil"),
        gr.Textbox(
            label="Labels",
            info="Separated by semicolon (;)",
            lines=6,
            value="""A page of printed text;
A page of handwritten text;
A blank page with no text;
A cover of a book;
A page of a book that contains a large illustration;
A page that features a table with multiple columns and rows""",
        ),
    ],
    outputs="label",
    examples=[['Journalsdateboo00DeanZ_0177.jpg',None], 
        ["newmexicobotani00newmb_0084.jpg",None],
        ["easternareacrui00natic_0004.jpg",None],
        ["1945fieldnotesla00klau_0318.jpg",None],
        ["sturmsfiguresofp01stur_0263.jpg",None]], 
    title="Zero-shot Image Classification of BHL Images",
    description="Upload a scanned BHL page and classify it"
)

demo.launch(
    server_name="127.0.0.1",   # local only
    server_port=7860,
    share=False                # do NOT expose publicly
)
