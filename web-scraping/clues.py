import sqlite3
import json

def create_database():
    conn = sqlite3.connect('clues.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clues (
                id INTEGER PRIMARY KEY,
                hint TEXT,
                word TEXT,
                answer TEXT
                )''')
    conn.commit()
    conn.close()

def insert_data(clues_data):
    conn = sqlite3.connect('clues.db')
    c = conn.cursor()
    for word, hints in clues_data.items():
        for hint in hints:
            hint_text, word_answer = hint
            c.execute("INSERT INTO clues (hint, word, answer) VALUES (?, ?, ?)", (hint_text, word, word_answer))
    conn.commit()
    conn.close()

def search_words():
    hint_to_search = input("Enter clue or part of clue: ")
    solution_length = input("Enter the length of the solution (leave blank for any length): ")
    solution_letters = input("Enter characters that must be included in the solution (leave blank for any characters): ").lower()
    
    conn = sqlite3.connect('clues.db')
    c = conn.cursor()

    # Split the input hint into individual words
    hint_words = hint_to_search.lower().split()

    # Construct a dynamic query with multiple OR conditions to search for each word in the hint
    query = "SELECT hint, answer FROM clues WHERE 1=1 "
    query_params = []
    for word in hint_words:
        query += "AND hint LIKE ? "
        query_params.append('%' + word + '%')

    c.execute(query, query_params)
    results = c.fetchall()
    
    # Filter results based on solution length and letters
    filtered_results = set()  # To store unique solutions
    for hint, answer in results:
        if solution_length and len(answer) != int(solution_length):
            continue
        if solution_letters and not all(char in answer.lower() for char in solution_letters):
            continue
        filtered_results.add((hint, answer))
    
    conn.close()

    if not filtered_results:
        print("No matching clues and solutions found.")
        return

    print("Matching clues and solutions found:")
    for hint, answer in filtered_results:
        print(f"Clue: {hint}")
        print(f"Solution: {answer}")


# Load clues from JSON file
with open('/Users/aazeltan/Desktop/learnpy/web-scraping/db.json', 'r') as file:
    clues_data = json.load(file)

# Create the database
create_database()

# Insert data into the database
insert_data(clues_data)

# Search for words based on input hints
while True:
    search_words()
    cont = input("Do you want to search again? (yes/no): ")
    if cont.lower() != 'yes':
        break
