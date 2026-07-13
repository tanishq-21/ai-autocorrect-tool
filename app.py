from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

# load model and tokenizer
print("Loading model...")
MODEL_PATH = "vennify/t5-base-grammar-correction"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)
print("Model loaded!")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/autocorrect", methods=["POST"])
def autocorrect():
    data = request.get_json()
    text = data.get("text", "").strip()
    
    if not text:
        return jsonify({"corrected_text": ""})
    
    try:
        # convert text to tokens
        inputs = tokenizer(text, return_tensors="pt").input_ids
        
        # run model prediction
        outputs = model.generate(inputs, max_length=128, num_beams=4)
        
        # decode back to string
        corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return jsonify({"corrected_text": corrected_text})
        
    except Exception as e:
        print(f"Prediction error: {e}")
        return jsonify({"corrected_text": text, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)