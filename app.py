from flask import Flask, jsonify

app = Flask(__name__)

# Simulated in-memory storage
data_storage = {
    'processed_data': None
}

# Mock data to simulate fetching from an external service
mock_data = [
    {'name': 'Item 1', 'value': 10},
    {'name': 'Item 2', 'value': 20},
    {'name': 'Item 3', 'value': 30}
]


def process_data(data):
    """
    Process the fetched data by transforming text to uppercase and summing values.

    Parameters:
    - `data` (list): A list of dictionaries where each dictionary contains a 'name' (str) and 'value' (int or float).

    Returns:
    - dict: A dictionary containing:
        - `processed_items` (list): A list of dictionaries with the 'name' field in uppercase and the original 'value'.
        - `total_value` (int or float): The sum of all 'value' fields from the input data.
    """
    processed = []
    total_value = 0
    for item in data:
        processed_item = {
            'name': item['name'].upper(),
            'value': item['value']
        }
        processed.append(processed_item)
        total_value += item['value']

    return {
        'processed_items': processed,
        'total_value': total_value
    }


@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    """
    Endpoint to simulate fetching and processing data from an external service.

    Returns:
    - JSONResponse: A JSON response containing the processed data.
    """

    global data_storage
    # Simulate data retrieval
    data = mock_data
    # Process the data
    processed_data = process_data(data)
    # Store processed data
    data_storage['processed_data'] = processed_data
    return jsonify(processed_data)


@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    """
    Endpoint to retrieve the processed data stored in memory.

    Returns:
    - JSONResponse: A JSON response containing the processed data.
    - 404 Error: If no processed data is found in memory, returns a JSON response with an error message.
    """
    global data_storage

    if data_storage['processed_data'] is None:
        return jsonify({'error': 'No processed data found'}), 404

    return jsonify(data_storage['processed_data'])


if __name__ == '__main__':
    app.run(debug=True)
