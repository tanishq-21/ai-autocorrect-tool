# AI Autocorrect Tool

## A web application that automatically fixes grammar and spelling errors using deep learning.

This open-source Python Flask web application serves as an automated grammar checker and English sentence correction tool powered by natural language processing (NLP). By utilizing the Hugging Face Transformers library, this software provides real-time text editing, sentence optimization, and spell-checking capabilities directly within a responsive web UI. If you are looking for an alternative to Grammarly or an AI writing assistant that can fix verb tenses, incorrect prepositions, and structural syntax errors locally, this deep learning application provides an efficient full-stack solution for developers and writers alike.

---

```text
[ User Text Input ] 
       │
       ▼ (Asynchronous JavaScript fetch() POST Request)
 ┌──────────────┐
 │ Flask Server │ ◄─── (Loads t5-base-grammar-correction Model)
 └──────┬───────┘
        │
        ├─► [ AutoTokenizer ]  ──► Converts raw text into numerical tokens
        ├─► [ Seq2Seq Model ]  ──► Evaluates syntax and predicts corrections
        └─► [ Decode Output ]  ──► Converts tokens back into clean English text
        │
        ▼ (JSON Response Data)
[ Updated UI Display ]
```
---
Installation & Usage Guide (For Users)
If you just want to run this application on your local machine to use the tool, follow these straightforward steps:

1. Download the Project: Download and extract the project zip folder to your computer.

2. Open Terminal/Command Prompt: Navigate to the folder where you extracted the project files.

3. Install the Requirements: Run the following command to download the necessary packages:
```text
pip install flask transformers torch
```

4. Launch the Tool: Start the application by running:
```text
python app.py
```

5. Open in Browser: Wait until the console says the model is loaded, then open your web browser and go to:
```text
http://127.0.0.1:5000
```

Local Development Setup (For Contributors)

If you want to modify the source code, build features, or debug the application, setup your environment using these guidelines:

1. Fork and Clone: Fork this repository to your GitHub account and clone it locally:
```text
git clone [https://github.com/YOUR_USERNAME/pinnacle-autocorrect-tool.git](https://github.com/YOUR_USERNAME/pinnacle-autocorrect-tool.git)
cd pinnacle-autocorrect-tool
```

2. Environment Isolation: We highly recommend developing inside a virtual environment:
```text
python -m venv venv
# Activate on Windows:
.\venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate
```

3. Editable Installation: Install packages and ensure your dependencies are mapped correctly:
```text
pip install -r requirements.txt
```

Roadmap & Known Issues

Known Issues
1. Initial Model Download Delay: The first execution requires an ~892MB download of the t5-base-grammar-correction configuration files, which may temporarily freeze execution depending on network bandwidth.
2. High CPU/RAM Overhead: Running deep learning sequence-to-sequence generation via PyTorch locally can cause latency on lower-end host machines without dedicated GPU acceleration.

Future Roadmap
1. Implement user toggle options to choose between different model sizes (e.g., small, base, large).
2. Migrate heavy local model execution to API endpoint handling for lower client-side latency.
3. Add multi-language text translation and correction capabilities.
