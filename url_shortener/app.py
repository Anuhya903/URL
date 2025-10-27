import os
from flask import Flask, render_template, request, redirect, jsonify, url_for
import sqlite3
import random
import string
from datetime import datetime
import re

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS urls
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         original_url TEXT NOT NULL,
         short_code TEXT UNIQUE NOT NULL,
         created_at DATETIME NOT NULL,
         click_count INTEGER DEFAULT 0)
    ''')
    conn.commit()
    conn.close()

# Generate random short code
def generate_short_code():
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choice(characters) for _ in range(6))
        # Check if code exists
        conn = sqlite3.connect('urls.db')
        c = conn.cursor()
        existing = c.execute('SELECT id FROM urls WHERE short_code = ?', (code,)).fetchone()
        conn.close()
        if not existing:
            return code

# Validate URL
def is_valid_url(url):
    # Basic URL validation using regex
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None

@app.route('/')
def index():
    # Get URLs for statistics table
    conn = sqlite3.connect('urls.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    urls = c.execute('''
        SELECT original_url, short_code, created_at, click_count
        FROM urls ORDER BY created_at DESC
    ''').fetchall()
    conn.close()
    return render_template('index.html', urls=urls)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form.get('url')
    
    if not original_url:
        return jsonify({'error': 'Please provide a URL'}), 400
    
    if not is_valid_url(original_url):
        return jsonify({'error': 'Invalid URL format. Include http:// or https://'}), 400
    
    short_code = generate_short_code()
    
    try:
        conn = sqlite3.connect('urls.db')
        c = conn.cursor()
        c.execute(
            'INSERT INTO urls (original_url, short_code, created_at) VALUES (?, ?, ?)',
            (original_url, short_code, datetime.now())
        )
        conn.commit()
        conn.close()
        
        # FIX: Use url_for for correct URL generation
        short_url = url_for('redirect_to_url', short_code=short_code, _external=True)
        return jsonify({
            'original_url': original_url,
            'short_url': short_url,
            'short_code': short_code
        })
    except Exception as e:
        return jsonify({'error': 'An error occurred while shortening the URL'}), 500

@app.route('/<short_code>')
def redirect_to_url(short_code):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    result = c.execute(
        'SELECT original_url FROM urls WHERE short_code = ?',
        (short_code,)
    ).fetchone()
    
    if result:
        # Increment click count
        c.execute(
            'UPDATE urls SET click_count = click_count + 1 WHERE short_code = ?',
            (short_code,)
        )
        conn.commit()
        conn.close()
        return redirect(result[0])
    
    conn.close()
    return render_template('index.html', error='URL not found'), 404

if __name__ == '__main__':
    init_db()
    # Render deployment fix
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)