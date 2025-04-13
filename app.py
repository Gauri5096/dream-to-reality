from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyDYR2ApZgPNWruEO1yjT71p3rsxEbhYSHg"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_dream', methods=['POST'])
def process_dream():
    try:
        dream_text = request.json.get('dream')
        
        # Generate text response
        text_prompt = f"""You are a dream interpreter and reality transformer. 
        The user has shared this dream: {dream_text}
        
        Please provide a detailed analysis in the following format:
        
        1. Dream Interpretation:
        - Explain the symbolic meaning
        - Analyze the emotions and themes
        - Connect it to the dreamer's subconscious
        
        2. Reality Transformation:
        - How can this dream manifest in reality?
        - What opportunities or warnings does it present?
        
        3. Action Steps:
        - List 3-5 practical steps to bring this dream into reality
        - Include specific, actionable advice
        
        Make the response clear, insightful, and practical."""
        
        text_response = model.generate_content(text_prompt)
        
        return jsonify({
            'text_response': text_response.text
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 