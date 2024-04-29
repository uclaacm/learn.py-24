from flask import Flask, render_template, request
import sqlite3
import json

app = Flask(__name__)

# Function to connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('clues.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to create the SQLite database
def create_database():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clues (
                id INTEGER PRIMARY KEY,
                hint TEXT,
                word TEXT,
                answer TEXT
                )''')
    conn.commit()
    conn.close()

# Function to insert data into the SQLite database
def insert_data(clues_data):
    conn = get_db_connection()
    c = conn.cursor()
    for word, hints in clues_data.items():
        for hint in hints:
            hint_text, word_answer = hint
            c.execute("INSERT INTO clues (hint, word, answer) VALUES (?, ?, ?)", (hint_text, word, word_answer))
    conn.commit()
    conn.close()

# Function to perform search
def search_words(hint_to_search, solution_length, solution_letters):
    conn = get_db_connection()
    c = conn.cursor()

    hint_words = hint_to_search.lower().split()
    query = "SELECT hint, answer FROM clues WHERE 1=1 "
    query_params = []
    for word in hint_words:
        query += "AND hint LIKE ? "
        query_params.append('%' + word + '%')

    c.execute(query, query_params)
    results = c.fetchall()
    
    filtered_results = set()
    for hint, answer in results:
        if solution_length and len(answer) != int(solution_length):
            continue
        if solution_letters and not all(char in answer.lower() for char in solution_letters):
            continue
        filtered_results.add((hint, answer))
    
    conn.close()
    return filtered_results

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    hint_to_search = request.form['hint']
    solution_length = request.form['length']
    solution_letters = request.form['letters'].lower()

    results = search_words(hint_to_search, solution_length, solution_letters)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    create_database()
    
    # Load clues from JSON file and insert into database
    with open('db.json', 'r') as file:
        clues_data = json.load(file)
        insert_data(clues_data)
    
    app.run(debug=True)
