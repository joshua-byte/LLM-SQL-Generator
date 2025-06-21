import os
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import google.generativeai as genai

# ========== CONFIGURE FLASK ==========
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# ========== CONFIGURE GEMINI ==========
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "your_api_key")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# ========== PROMPT BUILDER ==========
def build_prompt(nl_query: str, schema_dict: dict) -> str:
    schema_text = "\n".join(
        [f"Table: {table}({', '.join(columns)})" for table, columns in schema_dict.items()]
    )
    return f"""You are an expert SQL generator.
Use the following database schema to generate a valid SQL query.

Schema:
{schema_text}

Prompt: {nl_query.strip()}

SQL:"""

# ========== SQL GENERATOR ==========
def sql_generator(natural_lang: str, schema_dict: dict) -> str:
    prompt = build_prompt(natural_lang, schema_dict)
    response = model.generate_content(prompt)
    return response.text.strip()

# ========== ROUTES ==========

@app.route('/')
def serve_frontend():
    """Serve the main HTML file"""
    return send_from_directory('.', 'index.html')

@app.route('/generate-sql', methods=['POST'])
def generate_sql():
    """API endpoint to generate SQL from natural language"""
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        # Validate required fields
        if 'prompt' not in data or not data['prompt'].strip():
            return jsonify({'error': 'Prompt is required'}), 400
        
        if 'schema' not in data:
            return jsonify({'error': 'Schema is required'}), 400
        
        prompt = data['prompt'].strip()
        schema = data['schema']
        
        # Validate schema format
        if not isinstance(schema, dict):
            return jsonify({'error': 'Schema must be a dictionary'}), 400
        
        for table_name, columns in schema.items():
            if not isinstance(columns, list):
                return jsonify({'error': f'Table "{table_name}" must have an array of columns'}), 400
            if len(columns) == 0:
                return jsonify({'error': f'Table "{table_name}" must have at least one column'}), 400
        
        # Generate SQL using Gemini
        sql = sql_generator(prompt, schema)
        
        return jsonify({'sql': sql})
        
    except Exception as e:
        print(f"Error generating SQL: {e}")
        return jsonify({'error': 'Failed to generate SQL. Please try again.'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# ========== MAIN ==========
if __name__ == '__main__':
    print("🚀 Starting Gemini SQL Generator Server...")
    print("📄 Frontend: http://localhost:8000")
    print("🔗 API: http://localhost:8000/generate-sql")
    print("🛑 Press Ctrl+C to stop\n")
    
    app.run(host='0.0.0.0', port=8000, debug=True)
