import streamlit as st
from datetime import datetime, timedelta

def render_alerts_panel():
    """Render the alerts panel matching the TSX design"""
    
    # Sample alerts data
    alerts = [
        {
            "id": 1,
            "type": "High Risk",
            "message": "Downtown area shows 35% increase in theft incidents",
            "time": "2 hours ago",
            "severity": "high",
            "icon": "⚠️"
        },
        {
            "id": 2,
            "type": "Prediction",
            "message": "Model predicts spike in burglaries in North District next week",
            "time": "5 hours ago",
            "severity": "medium",
            "icon": "📈"
        },
        {
            "id": 3,
            "type": "Hotspot",
            "message": "New crime hotspot detected near Central Park area",
            "time": "1 day ago",
            "severity": "medium",
            "icon": "📍"
        },
        {
            "id": 4,
            "type": "Info",
            "message": "Weekly crime report generated successfully",
            "time": "2 days ago",
            "severity": "low",
            "icon": "🕒"
        },
    ]
    
    st.markdown("""
    <style>
    .alerts-panel {
        background: #1a1a2e;
        border: 1px solid #374151;
        border-radius: 0.5rem;
        padding: 1.5rem;
    }
    .alerts-title {
        color: white;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .alert-item {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        padding: 1rem;
        border-radius: 0.5rem;
        background: rgba(55, 65, 81, 0.5);
        margin-bottom: 1rem;
        transition: background-color 0.2s;
    }
    .alert-item:hover {
        background: rgba(55, 65, 81, 0.8);
    }
    .alert-icon {
        padding: 0.5rem;
        border-radius: 0.5rem;
        font-size: 1.25rem;
    }
    .alert-icon-high {
        background: rgba(239, 68, 68, 0.2);
    }
    .alert-icon-medium {
        background: rgba(234, 179, 8, 0.2);
    }
    .alert-icon-low {
        background: rgba(59, 130, 246, 0.2);
    }
    .alert-content {
        flex: 1;
    }
    .alert-header {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.25rem;
    }
    .alert-badge {
        padding: 0.25rem 0.5rem;
        border-radius: 0.375rem;
        font-size: 0.75rem;
        font-weight: 500;
        border: 1px solid;
    }
    .badge-high {
        border-color: #ef4444;
        color: #fca5a5;
    }
    .badge-medium {
        border-color: #eab308;
        color: #fde047;
    }
    .badge-low {
        border-color: #3b82f6;
        color: #93c5fd;
    }
    .alert-time {
        color: #9ca3af;
        font-size: 0.75rem;
    }
    .alert-message {
        color: #d1d5db;
        font-size: 0.875rem;
        margin: 0;
    }
    .icon-high {
        color: #f87171;
    }
    .icon-medium {
        color: #fbbf24;
    }
    .icon-low {
        color: #60a5fa;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Render the alerts panel
    st.markdown("""
    <div class="alerts-panel">
        <h3 class="alerts-title">Recent Alerts & Insights</h3>
        <div class="alerts-content">
    """, unsafe_allow_html=True)
    
    # Render each alert
    for alert in alerts:
        # Determine styles based on severity
        if alert["severity"] == "high":
            icon_class = "alert-icon-high"
            badge_class = "badge-high"
            icon_color_class = "icon-high"
        elif alert["severity"] == "medium":
            icon_class = "alert-icon-medium"
            badge_class = "badge-medium"
            icon_color_class = "icon-medium"
        else:
            icon_class = "alert-icon-low"
            badge_class = "badge-low"
            icon_color_class = "icon-low"
        
        st.markdown(f"""
        <div class="alert-item">
            <div class="alert-icon {icon_class}">
                <span class="{icon_color_class}">{alert['icon']}</span>
            </div>
            <div class="alert-content">
                <div class="alert-header">
                    <span class="alert-badge {badge_class}">{alert['type']}</span>
                    <span class="alert-time">{alert['time']}</span>
                </div>
                <p class="alert-message">{alert['message']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

# Optional: Function to add dynamic alerts from backend
def add_alert(alert_type, message, severity="medium"):
    """Add a new alert dynamically"""
    # This could be used to add alerts from your backend
    pass
