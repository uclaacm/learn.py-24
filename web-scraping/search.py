import pandas as pd
import json

JSON_FILENAME = '/Users/aazeltan/Desktop/learnpy/web-scraping/selenium/db.json'

def search_words(df):
    hint_to_search = input("Enter clue or part of clue: ").lower()
    solution_length = input("Enter the length of the solution (leave blank for any length): ")
    solution_letters = input("Enter characters that must be included in the solution (leave blank for any characters): ").lower()

    # Split the input hint into individual words
    hint_words = hint_to_search.lower().split()

    # Filter DataFrame based on input conditions
    filtered_df = df
    for word in hint_words:
        filtered_df = filtered_df[filtered_df['hint'].str.contains(word, case=False)]
    if solution_length:
        filtered_df = filtered_df[filtered_df['answer'].apply(len) == int(solution_length)]
    if solution_letters:
        filtered_df = filtered_df[filtered_df['answer'].apply(lambda x: all(char in x.lower() for char in solution_letters))]

    unique_solutions = set()  # To store unique solutions

    if filtered_df.empty:
        print("No matching clues and solutions found.")
        return

    print("Matching clues and solutions found:")
    for index, row in filtered_df.iterrows():
        if row['answer'] not in unique_solutions:
            unique_solutions.add(row['answer'])
            print(f"Clue: {row['hint']}")
            print(f"Solution: {row['answer']}")


def load_dataframe(filename) -> pd.DataFrame:
    # Load clues from JSON file
    """
    Sample JSON data for one clue entry:
    `clues_data` will contain a dictionary of these.
    "passage": [
        [
            "Passage of a planet across a star, e.g.",
            "TRANSIT"
        ]
    ],
    """
    with open(filename, 'r', encoding="utf-8") as file:
        json_obj = json.load(file)

    # Create dataframe
        # Sample tuple: (Fly buzzing around the house, e.g.", "fly", "PEST")
        # hint[0] gives the textual hint
        # hint[1] gives the crossword answer (a single word)
    df = pd.DataFrame([(hint[0], word, hint[1]) for word, hints in json_obj.items() for hint in hints],
                      columns=['hint', 'word', 'answer'])
    return df



def main():
    df = load_dataframe(JSON_FILENAME)
    # Search for words based on input hints
    while True:
        search_words(df)
        cont = input("Do you want to search again? (yes/no): ")
        if cont.lower() != 'yes':
            break

if __name__ == "__main__":
    main()  
