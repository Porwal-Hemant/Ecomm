from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load and preprocess the dataset
items_dataset = pd.read_csv('amazon_data.csv')
columns_to_remove = ['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12']
items_dataset = items_dataset.drop(columns=columns_to_remove)

# Preprocessing
items_dataset['Title'] = items_dataset['Title'].str.lower().str.replace('&', 'and')
items_dataset['Category'] = items_dataset['Category'].str.lower().str.replace('&', 'and')
items_dataset['Sub-Category'] = items_dataset['Sub-Category'].str.lower().str.replace('&', 'and')

items_dataset['tags'] = items_dataset['Title'] + items_dataset['Category'] + items_dataset['Sub-Category']
items_dataset['tags'] = items_dataset['tags'].apply(lambda x: " ".join(x))

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.json.get('query', '').lower()

    # Filter items where tags contain the user input
    matching_items = items_dataset[items_dataset['tags'].str.contains(user_input, case=False, na=False)]

    if not matching_items.empty:
        return jsonify(matching_items[['Title']].to_dict(orient='records'))
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run(port=5000, debug=True)



