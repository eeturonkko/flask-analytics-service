import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI environments
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/plot', methods=['POST'])
def create_plot():
    data = request.json.get('weights', [])

    if not data:
        return jsonify({'error': 'No weights provided'}), 400

    # Create a line plot
    plt.figure(figsize=(10, 6))
    weeks = range(1, len(data) + 1)
    plt.plot(weeks, data, marker='o', linestyle='-', color='b', markersize=8, linewidth=2)

    # Enhance the plot
    plt.title('Weekly Average Weights', fontsize=16)
    plt.xlabel('Week', fontsize=14)
    plt.ylabel('Weight (kg)', fontsize=14)
    plt.xticks(weeks)  # Set x-ticks to start from Week 1
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()

    # Save plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
