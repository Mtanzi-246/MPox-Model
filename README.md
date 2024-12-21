# Monkeypox Mathematical Modeling

## Project Overview
This project aims to create a mathematical model for Monkeypox(MPox), a viral zoonotic disease caused by the monkeypox virus, which is in the same family as the variola virus (responsible for smallpox). Although monkeypox is generally less severe than smallpox, it can still cause significant illness in humans. The disease primarily occurs in Central and West Africa, though outbreaks have been reported globally.

The project utilizes mathematical modeling to better understand the spread and behavior of the disease, with the goal of providing insights that could help in managing outbreaks.

## Libraries and Technologies Used
- **Python**: The main programming language used for the project.
- **SciPy**: A Python library for scientific and technical computing, used for solving differential equations and performing integrations.
- **Matplotlib (PyPlot)**: For live updating of graphs and visualizing the results of the simulations.
- **Streamlit**: Used for deploying the project and creating interactive web applications to visualize the model in real-time.

## Installation

To run this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/MPox-Model.git


2. **Navigate into the project directory**:
   ```bash
   cd MPox-Model
   ```

3. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Monkeypox model and visualize the results:

1. **Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. The application will open in your browser, where you can interact with the model and see live graphs of the Monkeypox simulations.

## Contributing

Contributions are welcome! If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
