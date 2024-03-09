# Gemini API for python Template
# Dominic Minnich 2024
# This is a simple Flask web application that uses the Gemini API to generate content based on user input.


from flask import Flask, request, render_template, jsonify
# pip install -q -U google-generativeai
import google.generativeai as genai

app = Flask(__name__)

# Configure the generative AI API key
genai.configure(api_key="PUT YOUR API KEY HERE") # <<----<< You can get your API key from the Gemini website and put it here!

# Define the generation configuration for the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1, 
  "top_k": 1, 
  "max_output_tokens": 1000,
}

# Define the safety settings for content generation
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

# Create an instance of the generative model
model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get the question from the form data
    question = request.form['question']
    
    # Prepare the prompt parts for content generation
    prompt_parts = [question]
    
    # Generate the response using the model
    response = model.generate_content(prompt_parts)
    
    # Return the response as JSON
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)
