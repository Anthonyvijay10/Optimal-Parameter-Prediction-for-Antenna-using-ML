Antenna Optimal Size Predictor
This is a web application that predicts the optimal size of an antenna based on input features using a Convolutional Neural Network (CNN) followed by a Gated Recurrent Unit (GRU) model.

Overview
The Antenna Optimal Size Predictor is a tool designed to help engineers and researchers in the field of antenna design to estimate the optimal size of an antenna given certain parameters such as split width, radius, and frequency.

Features
Predicts two key metrics: S11 and VSWR
Web-based interface for easy input and visualization of results
Utilizes a deep learning model for accurate predictions
Usage
Clone the repository:
bash
Copy code
git clone <repository_url>
cd Antenna-Optimal-Size-Predictor
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Flask application:
bash
Copy code
python app.py
Open your web browser and go to http://localhost:5000 to access the application.

Enter the values for split width, radius, and frequency in the provided input fields.

Click on the "Predict" button to see the predicted values for S11 and VSWR.

Model Architecture
The neural network model used in this application consists of a combination of Convolutional Neural Network (CNN) and Gated Recurrent Unit (GRU) layers. This architecture was chosen for its ability to capture both spatial and temporal patterns in the input data.

Data
The dataset used to train the model should be stored in a CSV file named data.csv. The file should contain columns for split width, radius, frequency, S11, and VSWR.

Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.
