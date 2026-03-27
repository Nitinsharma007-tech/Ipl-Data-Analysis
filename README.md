# 🏏 IPL Match Winner Predictor (Machine Learning + Streamlit)

## 📌 Project Overview

This project is a Machine Learning-based web application that predicts the winner of an IPL match using key match factors like toss result, teams, and venue.

The goal of this project is to analyze historical IPL data and build a predictive model that can estimate match outcomes in real-time through an interactive UI.

---

## 🚀 Features

* 🔮 Predict match winner based on:

  * Teams playing
  * Toss winner
  * Toss decision (bat/field)
  * Stadium (venue)
* 🎯 Dropdown-based input (no spelling errors)
* 📊 Machine Learning model (Random Forest)
* 🌐 Interactive UI using Streamlit
* ⚡ Fast and real-time predictions

---

## 🧠 Machine Learning Workflow

### 1. Data Collection

* Dataset: IPL matches dataset (`matches.csv`)
* Contains match-level details like teams, toss, venue, and winner

### 2. Data Preprocessing

* Removed null values
* Selected relevant features
* Converted categorical data using Label Encoding

### 3. Feature Engineering

* Created target variable:

  * `team1_win` (1 if team1 wins, else 0)

### 4. Model Training

* Algorithm used: **Random Forest Classifier**
* Train-Test Split: 80-20

### 5. Evaluation

* Accuracy Score
* Confusion Matrix
* Classification Report

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **Matplotlib, Seaborn**
* **Streamlit**

---

## 📁 Project Structure

```
IPL_DATA_ANALYSIS/
│
├── model_files/
│   ├── model.pkl
│   ├── le_team.pkl
│   ├── le_toss.pkl
│   ├── le_venue.pkl
│
├── streamlit.py
├── matches.csv
├── main.py / app.ipynb
├── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone Repository

```
git clone <your-repo-link>
cd IPL_DATA_ANALYSIS
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Streamlit App

```
streamlit run streamlit.py
```

---

## 🎯 Example Prediction

Input:

* Team 1: Mumbai Indians
* Team 2: Chennai Super Kings
* Toss Winner: CSK
* Toss Decision: Field
* Venue: Chepauk

Output:
👉 Predicted Winner: Chennai Super Kings

---

## ⚠️ Limitations

* Model uses limited features (no player-level data)
* Does not consider real-time form or injuries
* Accuracy depends on historical patterns only

---

## 🔥 Future Improvements

* Add last 5 match performance
* Head-to-head statistics
* Player-level analysis
* Win probability percentage
* Deploy on cloud (Streamlit Cloud / Render)
* Add AI chatbot integration

---

## 🙌 Acknowledgment

This project is built as part of a Machine Learning learning journey and demonstrates practical implementation of data science concepts on real-world sports data.

---

## 📬 Contact

If you have any suggestions or improvements, feel free to connect!
