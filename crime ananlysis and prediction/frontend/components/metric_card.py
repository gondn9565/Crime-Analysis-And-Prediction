import streamlit as st

def render_metric_card(title, value, icon, trend, trend_up=True):
    """
    Render a metric card component
    
    Args:
        title: Card title
        value: Main value to display
        icon: Emoji icon
        trend: Trend text
        trend_up: Whether trend is positive (True for up/good, False for down/bad)
    """
    
    trend_color = "trend-up" if trend_up else "trend-down"
    trend_icon = "📈" if trend_up else "📉"
    
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-header">
            <div class="metric-icon">{icon}</div>
            <span class="metric-title">{title}</span>
        </div>
        <div class="metric-value">{value}</div>
        <div class="metric-trend {trend_color}">
            {trend_icon} {trend}
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_metric_cards():
    """Render all metric cards in a grid"""
    
    st.markdown("""
    <style>
    .metric-card {
        background: #1a1a2e;
        border: 1px solid #374151;
        border-radius: 0.75rem;
        padding: 1.5rem;
        height: 100%;
        transition: all 0.2s ease;
    }
    .metric-card:hover {
        border-color: #4b5563;
        transform: translateY(-2px);
    }
    .metric-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 1rem;
    }
    .metric-icon {
        background: rgba(255,255,255,0.1);
        padding: 0.5rem;
        border-radius: 0.5rem;
        font-size: 1.25rem;
    }
    .metric-title {
        color: #9ca3af;
        font-size: 0.875rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .metric-value {
        color: white;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .metric-trend {
        font-size: 0.875rem;
        font-weight: 500;
    }
    .trend-up {
        color: #10b981;
    }
    .trend-down {
        color: #ef4444;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create 4 columns for the metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_metric_card(
            title="Total Crimes",
            value="1,432",
            icon="⚠️",
            trend="↓ 12% from last month",
            trend_up=False
        )
    
    with col2:
        render_metric_card(
            title="Violent Crimes",
            value="342",
            icon="📊",
            trend="↓ 8% from last month", 
            trend_up=False
        )
    
    with col3:
        render_metric_card(
            title="Prediction Accuracy",
            value="94.5%",
            icon="🎯",
            trend="↑ 2.3% improvement",
            trend_up=True
        )
    
    with col4:
        render_metric_card(
            title="Cities Covered",
            value="24",
            icon="🏙️",
            trend="↑ 3 new cities",
            trend_up=True
        )
