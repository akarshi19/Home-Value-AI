# Home Value AI 🌟

Welcome to **Home Value AI**, a project that predicts the price of houses based on key features such as location, number of bedrooms (BHK), square footage, and number of bathrooms. This project uses a **Linear Regression Model** built with Python and integrates it with a web interface using Flask. The website's frontend is crafted using HTML, CSS, and JavaScript.

---

## 🌈Features
- Predict house prices with high accuracy based on user input.
- Interactive and user-friendly web interface.
- Lightweight and scalable architecture.

---

## 🏗️Architecture
![R](https://github.com/akarshi19/Home-Value-AI/blob/master/images/architecture.jpg)


The architecture of the project is as follows:

### 1. **ML Model**
- **Input:** Raw data.
- **Pipeline:**
  1. Data Cleaning: Preprocess raw data to remove noise and prepare datasets.
  2. Dataset Preparation: Splits data into training and testing sets.
  3. Training: Train a Linear Regression model on the dataset.
  4. Testing: Evaluate the trained model on the testing dataset.
  5. Build Model: Finalize the model for predictions.
  6. Prediction: Use the model to predict house prices.

### 2. **Flask Layer**
- Acts as the middle layer between the ML model and the website.
- Handles requests from the website and communicates with the ML model.
- Returns predictions to the website.

### 3. **Website**
- **Frontend:** HTML, CSS, JavaScript for user interaction.
- Sends user inputs (location, BHK, square feet, bathrooms) to the Flask layer.
- Displays the predicted house price based on the ML model’s response.

**Diagram Overview:**
- Data flows from the website to the Flask layer as requests.
- Flask sends these inputs to the ML model.
- ML model processes the data and returns predictions back to the Flask layer.
- Flask layer sends the predictions to the website to display to the user.

---

##  🧑‍💻Technology Stack
### 1. **Machine Learning**
- Language: Python
- Model: Linear Regression

### 2. **Web Framework**
- Flask

### 3. **Frontend**
- HTML
- CSS
- JavaScript

---

## 🛠️Installation and Setup

### Prerequisites
- Python (>=3.7)
- Flask (>=2.0)
- Libraries: NumPy, Pandas, Scikit-learn
- Browser for frontend testing

### Steps
1. Clone the repository:
   ```bash
   git clone  https://github.com/akarshi19/Home-Value-AI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Home-Value-AI
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask server:
   ```bash
   python main.py
   ```
5. Open the website in your browser:
   ```
   http://localhost:5000
   ```

---

## 🚀Usage
1. Open the website in your browser.
2. Enter the following details:
   - **Location**: Enter the city or area.
   - **BHK**: Enter the number of bedrooms.
   - **Square Feet**: Enter the total square footage.
   - **Bathrooms**: Enter the number of bathrooms.
3. Click on the "Predict" button.
4. View the predicted price of the house.

---

## 📁File Structure
```
Home Value AI
├── main.py                # Flask application
├── templates
│   ├── predict.html        # Main HTML file
├── model
│   ├── LinearRegressionModel1.pkl  # Trained ML model
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## 🔮Future Enhancements
- Add more advanced ML models (e.g., Random Forest, Gradient Boosting).
- Enhance the frontend design with responsive frameworks like Bootstrap.
- Add support for more features, such as amenities and proximity to landmarks.

---

## 🤝Contributing
We welcome contributions! Feel free to open issues and pull requests to improve the project.

---

## 📣License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## 📞 Contact Information

If you have any questions, feedback, or suggestions, feel free to reach out!

- **Email**: [akarshigmathur@gmail.com](mailto:akarshigmathur@gmail.com)
- **GitHub**: [akarshi19](https://github.com/akarshi19)
- **LinkedIn**: [Akarshi Mathur](https://www.linkedin.com/in/akarshimathur19/)


