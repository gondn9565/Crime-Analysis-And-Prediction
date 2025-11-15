import streamlit as st

def render_footer():
    """Render the dashboard footer"""
    st.markdown("""
    <style>
    .main-footer {
        background: #1a1a2e;
        border-top: 1px solid #374151;
        padding: 1rem 1.5rem;
        margin: 2rem -1rem -2rem -1rem;
        text-align: center;
    }
    .footer-text {
        color: #9ca3af;
        font-size: 0.875rem;
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="main-footer">
        <p class="footer-text">© 2025 AI Crime Analysis System - BTech CSE Final Year Project</p>
    </div>
    """, unsafe_allow_html=True)
