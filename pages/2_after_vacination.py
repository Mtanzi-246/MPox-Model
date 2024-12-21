import streamlit as st
import numpy as np
import scipy.integrate as si
import plotly.graph_objects as go

st.set_page_config(
    page_title="Monkey Pox",
    page_icon="🐒",
    layout="wide",
)

# function
def mpox(x, T, beta, gamma, sigma, u, alpha, pie, vac):
    """Function that stores the state variables of the system"""
    S = x[0]   # Susceptible humans
    E = x[1]   # Exposed humans
    I = x[2]   # Infected humans
    R = x[3]   # Recovered Humans
    V = x[4]   # Vaccinated

    # The differential equations
    Y = np.zeros(5)
    N = sum(x)  # total population

    Y[0] = pie * N - (u * S) - (beta * S * I / N) - (S * vac)
    Y[1] = (beta * S * I / N) - (u * E) - (E * alpha) + (0.15 * V * beta)
    Y[2] = (E * alpha) - (u * I) - (sigma * I) - (I * gamma)
    Y[3] = (gamma * I) - (R * u)
    Y[4] = (S * vac) - (0.15 * V * beta) - (V * u)
   
    return Y


st.sidebar.markdown("## Parameteres (rates)")
# Sidebar sliders for adjusting parameters in real-time
N = 1000000
beta = st.sidebar.slider("Transmission rate (beta)", 0.0, 1.0, 0.2761)
gamma = st.sidebar.slider("Recovery rate (gamma)", 0.0, 0.1, 0.047)
sigma = st.sidebar.slider("Disease induced death (sigma)", 0.0, 0.1, 0.03)
u = st.sidebar.slider("Natural death rate (u)", 0.0, 0.05, 0.012)
alpha = st.sidebar.slider("Rate of exposed to infectious (alpha)", 0.0, 0.1, 0.091)
pie = st.sidebar.slider("Birth rate (pie)", 0.0, 0.1, 0.02, 0.001)
vac = st.sidebar.slider("Vaccination rate (vac)", 0.0, 0.1, 0.03)

# Time parameters
time = st.slider("Time Duration in days", 1, 365, 50,5)
# time = time * 30
t_start = 0
t_end = time
t_step = time
T = np.linspace(t_start, t_end, t_step)

st.sidebar.markdown("## Compartments")

# Initial conditions
Suscept = st.sidebar.slider("Susceptible", 0.0,1.0,0.95,0.1)
Exposed = st.sidebar.slider("Exposed", 0.0,1.0,0.03,0.01)
Infectd = st.sidebar.slider("Infected", 0.0,1.0,0.02,0.01)
Recoverd = st.sidebar.slider("Recovered", 0.0,1.0,0.0,0.1)
vaccine= st.sidebar.slider("Vaccination", 0.0,1.0,0.0,0.1)

sol0 = np.array([N*Suscept, N*Exposed, Infectd*N, Recoverd, vaccine])

# Solving the system of differential equations
sol = si.odeint(mpox, sol0, T, args=(beta, gamma, sigma, u, alpha, pie, vac))
sol1 = sol.T

# Plotting with Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=T, y=sol1[0], mode='lines', name='Susceptible', line=dict(dash='dash', color='black')))
fig.add_trace(go.Scatter(x=T, y=sol1[1], mode='lines', name='Exposed', line=dict(dash='solid', color='blue')))
fig.add_trace(go.Scatter(x=T, y=sol1[2], mode='lines', name='Infected', line=dict(dash='dashdot', color='red')))
fig.add_trace(go.Scatter(x=T, y=sol1[3], mode='lines', name='Recovered', line=dict(dash='dash', color='green')))
fig.add_trace(go.Scatter(x=T, y=sol1[4], mode='lines', name='Vaccinated', line=dict(dash='solid', color='orange')))

# Adding titles and labels
fig.update_layout(
    title="Mpox Epidemiological Dynamics with Vaccination",
    xaxis_title="Time (Days)",
    yaxis_title="Population",
    legend_title="State Variables",
    height=600,
    autosize=True
)

# Show the plot in Streamlit
st.plotly_chart(fig)