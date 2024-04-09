from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__, static_url_path='/static')

# Load the best model
best_model = load_model('best_model_Cnn_gru.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():
    # Extract query parameters
    split_width = request.args.get('split_width', default=0.5, type=float)
    dis_bw_rings = request.args.get('dis_bw_rings', default=0.4, type=float)
    freq_ghz = request.args.get('freq_ghz', default=0, type=float)
    
    # Reshape input data to match the model's input shape
    input_features = np.array([[split_width, dis_bw_rings, freq_ghz]])
    input_features_reshaped = input_features.reshape((input_features.shape[0], input_features.shape[1], 1))
    
    # Predict
    prediction = best_model.predict(input_features_reshaped)
    
    # Convert prediction results to Python native types
    s11_prediction = float(prediction[0][0])
    vswr_prediction = float(prediction[0][1])
    
    # Check if values are optimal
    s11_optimal = "Optimal" if s11_prediction <= -10 else "Not Optimal"
    vswr_optimal = "Optimal" if vswr_prediction < 2 else "Not Optimal"
    
    # Return the prediction along with optimal status
    return render_template('result.html', s11=s11_prediction, vswr=vswr_prediction, s11_optimal=s11_optimal, vswr_optimal=vswr_optimal)


if __name__ == '__main__':
    app.run(debug=True)
