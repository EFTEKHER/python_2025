import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import time

# Page configuration
st.set_page_config(
    page_title="Iris Vision: Futuristic Flower Classification",
    page_icon="🌺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for futuristic design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700&display=swap');

    .main {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #ffffff;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: white;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Orbitron', sans-serif;
        color: #ffffff !important;
        text-shadow: 0 0 10px rgba(0,230,255,0.7), 0 0 20px rgba(0,230,255,0.5);
    }
    
    p, div, span {
        font-family: 'Orbitron', sans-serif;
        color: #ffffff !important;
    }

    .neon-border {
        border: 1px solid #00e6ff;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0,230,255,0.8);
        padding: 20px;
        background: rgba(16,14,41,0.7);
        margin-bottom: 20px;
    }

    .metric-card {
        background: rgba(16, 14, 41, 0.7);
        border: 1px solid #00e6ff;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 0 15px rgba(0, 230, 255, 0.5);
        text-align: center;
        height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .stButton button {
        width: 100%;
        background: linear-gradient(135deg, #00e6ff, #0077ff);
        color: white;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 12px;
        box-shadow: 0 0 10px rgba(0,230,255,0.7);
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        box-shadow: 0 0 20px rgba(0,230,255,0.9);
        transform: translateY(-2px);
    }
    
    div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column;"] > div[data-testid="stVerticalBlock"] {
        border: 1px solid #00e6ff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 0 15px rgba(0,230,255,0.5);
        background: rgba(16,14,41,0.7);
    }
    
    /* Confusion matrix styling */
    .confusion-matrix {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
    }
    
    .confusion-matrix .xaxislabel, .confusion-matrix .yaxislabel {
        color: black !important;
        font-weight: bold;
    }
    
    .confusion-matrix .xticklabel, .confusion-matrix .yticklabel {
        color: black !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'animate_prediction' not in st.session_state:
    st.session_state.animate_prediction = False

# Load dataset
@st.cache_resource
def load_data():
    return load_iris()

iris = load_data()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
@st.cache_resource
def train_model():
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    return clf

clf = train_model()
y_pred = clf.predict(X_test)

# Title
st.markdown("<h1 style='text-align: center;'>🌺 IRIS VISION</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Futuristic Flower Classification System</h3>", unsafe_allow_html=True)

st.markdown("""
<div class="neon-border">
    <p style='text-align: center; font-size: 18px;'>
    This advanced system uses quantum-inspired machine learning algorithms to classify Iris flowers with unprecedented accuracy. 
    Explore the data, visualize patterns, and make predictions with our neural interface.
    </p>
</div>
""", unsafe_allow_html=True)

# Dashboard metrics
st.markdown("<h2>Quantum Classification Dashboard</h2>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    accuracy = clf.score(X_test, y_test)
    st.markdown(f"""
    <div class="metric-card">
        <h3>Model Accuracy</h3>
        <h2>{accuracy:.2%}</h2>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Data Points</h3>
        <h2>{len(X)}</h2>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Features</h3>
        <h2>{len(iris.feature_names)}</h2>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Species</h3>
        <h2>{len(iris.target_names)}</h2>
    </div>
    """, unsafe_allow_html=True)

# Data Explorer
st.markdown("<h2>Data Explorer</h2>", unsafe_allow_html=True)
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("<h3>Dataset Preview</h3>", unsafe_allow_html=True)
    st.dataframe(df.head(10), use_container_width=True, height=300)
with col2:
    st.markdown("<h3>Statistical Summary</h3>", unsafe_allow_html=True)
    st.dataframe(df.describe(), use_container_width=True, height=300)

# AI Model Performance
st.markdown("<h2>AI Model Performance</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3>Classification Report</h3>", unsafe_allow_html=True)
    report = classification_report(y_test, y_pred, target_names=iris.target_names, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    st.dataframe(report_df, use_container_width=True)

with col2:
    st.markdown("<h3>Confusion Matrix</h3>", unsafe_allow_html=True)
    cm = confusion_matrix(y_test, y_pred)
    
    # Create a custom figure with white background for the confusion matrix
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=iris.target_names, 
                yticklabels=iris.target_names,
                ax=ax)
    ax.set_xlabel('Predicted', color='black', fontweight='bold')
    ax.set_ylabel('Actual', color='black', fontweight='bold')
    ax.tick_params(axis='x', colors='black')
    ax.tick_params(axis='y', colors='black')
    
    # Set color of tick labels to black
    for label in ax.get_xticklabels():
        label.set_color('black')
    for label in ax.get_yticklabels():
        label.set_color('black')
        
    st.pyplot(fig)

# Data Visualizations
st.markdown("<h2>Data Visualizations</h2>", unsafe_allow_html=True)

# Create a copy of the data for visualization
df_viz = pd.DataFrame(iris.data, columns=iris.feature_names)
df_viz['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

col1, col2 = st.columns(2)

with col1:
    # Scatter plot
    st.markdown("<h3>Feature Relationships</h3>", unsafe_allow_html=True)
    x_axis = st.selectbox("X-Axis", iris.feature_names, index=0)
    y_axis = st.selectbox("Y-Axis", iris.feature_names, index=1)
    
    fig = px.scatter(df_viz, x=x_axis, y=y_axis, color='species',
                     title=f"{y_axis} vs {x_axis} by Species",
                     color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                      font=dict(color='white'))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # 3D Scatter plot
    st.markdown("<h3>3D Feature Space</h3>", unsafe_allow_html=True)
    fig = px.scatter_3d(df_viz, x='sepal length (cm)', y='sepal width (cm)', z='petal length (cm)',
                        color='species', symbol='species',
                        color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                      font=dict(color='white'),
                      scene=dict(xaxis=dict(backgroundcolor='rgba(0,0,0,0)'),
                                 yaxis=dict(backgroundcolor='rgba(0,0,0,0)'),
                                 zaxis=dict(backgroundcolor='rgba(0,0,0,0)')))
    st.plotly_chart(fig, use_container_width=True)

# Parallel coordinates
st.markdown("<h3>Parallel Coordinates</h3>", unsafe_allow_html=True)
df_viz['species_code'] = df_viz['species'].astype('category').cat.codes

fig = px.parallel_coordinates(df_viz, color="species_code",
                              color_continuous_scale=px.colors.diverging.Tealrose,
                              labels={col: col.replace(" (cm)", "") for col in df_viz.columns if col not in ['species', 'species_code']})

# Update color bar to show species names
fig.update_layout(
    coloraxis_colorbar=dict(
        title="Species",
        tickvals=[0, 1, 2],
        ticktext=iris.target_names,
    ),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white')
)
st.plotly_chart(fig, use_container_width=True)

# Prediction Interface
st.markdown("<h2>Neural Prediction Interface</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("<div class='neon-border'>", unsafe_allow_html=True)
    st.markdown("<h3>Input Parameters</h3>", unsafe_allow_html=True)
    
    sepal_length = st.slider("Sepal Length (cm)", float(X["sepal length (cm)"].min()), 
                            float(X["sepal length (cm)"].max()), float(X["sepal length (cm)"].mean()), 
                            key="pred_sepal_length")
    sepal_width = st.slider("Sepal Width (cm)", float(X["sepal width (cm)"].min()), 
                           float(X["sepal width (cm)"].max()), float(X["sepal width (cm)"].mean()), 
                           key="pred_sepal_width")
    petal_length = st.slider("Petal Length (cm)", float(X["petal length (cm)"].min()), 
                            float(X["petal length (cm)"].max()), float(X["petal length (cm)"].mean()), 
                            key="pred_petal_length")
    petal_width = st.slider("Petal Width (cm)", float(X["petal width (cm)"].min()), 
                           float(X["petal width (cm)"].max()), float(X["petal width (cm)"].mean()), 
                           key="pred_petal_width")
    
    if st.button("🚀 Launch Quantum Analysis", use_container_width=True):
        st.session_state.animate_prediction = True
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    if st.session_state.animate_prediction:
        with st.spinner("Quantum analysis in progress..."):
            # Simulate processing
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for percent_complete in range(101):
                time.sleep(0.02)
                progress_bar.progress(percent_complete)
                status_text.text(f"Analyzing floral patterns... {percent_complete}%")
            
            # Make prediction
            input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            prediction = clf.predict(input_data)
            probability = clf.predict_proba(input_data)[0]
            
            # Display results
            st.markdown("<div class='neon-border'>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #00ffcc;'>Prediction: {iris.target_names[prediction][0]}</h2>", unsafe_allow_html=True)
            
            # Create a visualization of probabilities
            fig = go.Figure(go.Bar(
                x=probability,
                y=iris.target_names,
                orientation='h',
                marker_color=px.colors.qualitative.Set2
            ))
            
            fig.update_layout(
                title="Prediction Confidence Levels",
                xaxis_title="Probability",
                yaxis_title="Species",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                xaxis=dict(range=[0, 1])
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Reset animation state
            st.session_state.animate_prediction = False
            
            # Celebration
            st.balloons()
    else:
        st.markdown("<div style='height: 400px; display: flex; justify-content: center; align-items: center;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00e6ff; text-align: center;'>Awaiting neural input parameters<br>⬅️ Configure settings and launch analysis</h3>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #00e6ff;'>", unsafe_allow_html=True)
st.markdown("### 🌌 Quantum Machine Learning Interface v2.0")
st.markdown("### ⚡ Powered by Streamlit & Scikit-Learn")
st.markdown("</div>", unsafe_allow_html=True)