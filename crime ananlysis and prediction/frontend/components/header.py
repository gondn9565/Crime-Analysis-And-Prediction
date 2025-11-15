import streamlit as st

def render_header():  # ← Make sure this is render_header, not Header
    """Render the dashboard header matching the TSX design"""
    st.markdown("""
    <style>
    .main-header {
        background: #0f4c75;
        border-bottom: 1px solid #374151;
        padding: 1rem 1.5rem;
        margin: -2rem -1rem 2rem -1rem;
    }
    .header-content {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    .header-icon {
        background: rgba(255, 255, 255, 0.1);
        padding: 0.5rem;
        border-radius: 0.5rem;
    }
    .header-title {
        color: white;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 0;
    }
    .header-subtitle {
        color: #bfdbfe;
        font-size: 0.875rem;
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="main-header">
        <div class="header-content">
            <div class="header-icon">
                <span style="color: white; font-size: 1.5rem;">🛡️</span>
            </div>
            <div>
                <h1 class="header-title">AI Crime Analysis System</h1>
                <p class="header-subtitle">Real-time Crime Prediction & Analytics</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
