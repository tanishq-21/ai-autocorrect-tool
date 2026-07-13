# Pinnacle AI Autocorrect Tool

This web application is pretty straightforward - it takes sentences with bad grammar or ones that are just plain wrong and uses a special AI tool to fix them on its own. The backend is built with Python and Flask, and the frontend is simple, using HTML, CSS, and JavaScript to make it work.

This project uses a special tool called `t5-base-grammar-correction` from a company called Hugging Face. Normally, you would use a kind of helper tool to make it work, but in this case, the project loads the tool's brain and its special dictionary directly. This helps prevent problems that can happen when the helper tool gets updated, so the project can run without any issues.

## Features
- Full-stack integration combining a Flask backend with a classic HTML frontend.
- AI-based grammar correction (fixes tenses, spelling, and prepositions).
- Real-time character counter limited to 500 characters.
- Clear button to reset the UI and a one-click Copy button to grab the output instantly.

## Project Structure
```text
pinnacle-autocorrect-tool/
│
├── app.py               (Flask backend server)
├── requirements.txt     (Python dependencies)
├── README.md            (Project documentation)
└── templates/
    └── index.html           (Frontend UI)

##Setup and Installation

To get started, you'll want to copy or download the entire project folder to your computer.

To get started, open a terminal and navigate to your project folder. From there, you'll need to install the necessary Python libraries to move forward with your project.

Bash
pip install flask transformers torch
To get the Flask server up and running, you need to execute the main script.

Bash
python app.py
Once you see "Model loaded!" on the terminal, open a web browser and navigate to the specified address.

Plaintext
[http://127.0.0.1:5000](http://127.0.0.1:5000)


## How It Works under the Hood

Here's how it works on the backend, in the app.py file: the server gets some text from the frontend, breaks it down into smaller parts, and then uses a special tool called AutoModelForSeq2SeqLM to make corrections. After that, it sends the cleaned-up text back to the frontend as a JSON response.

Frontend (index.html): Uses standard JavaScript fetch() to send the input text to the backend asynchronously without reloading the page, updating the DOM dynamically once the result arrives.


You're all set now, just save that file and your entire project will be officially documented and ready to move forward.