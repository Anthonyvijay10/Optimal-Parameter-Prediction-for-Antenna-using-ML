from flask import Flask, request, render_template
from xgboost import XGBRegressor
import numpy as np
import joblib

app = Flask(__name__, static_url_path='/static')

# Load the model
best_model = joblib.load('xgboost_regression_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():
    # Extract query parameters
    split_width = request.args.get('split_width', default=0, type=float)
    dis_bw_rings = request.args.get('dis_bw_rings', default=0, type=float)
    freq_ghz = request.args.get('freq_ghz', default=0, type=float)
    
    # Prepare input features as a numpy array
    input_features = np.array([[split_width, dis_bw_rings, freq_ghz]])
    
    # Predict using XGBoost model
    prediction = best_model.predict(input_features)
    
    # Convert prediction results to Python native types if necessary
    s11_prediction = prediction[0][0]
    vswr_prediction = prediction[0][1]
    
    # Check if values are optimal
    s11_optimal = "Optimal" if s11_prediction <= -20 else "Not Optimal"
    vswr_optimal = "Optimal" if vswr_prediction < 2 else "Not Optimal"
    
    # Return the prediction along with optimal status
    return render_template('result.html', s11=s11_prediction, vswr=vswr_prediction, 
                           s11_optimal=s11_optimal, vswr_optimal=vswr_optimal)

if __name__ == '__main__':
    app.run(debug=True)
