'''
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def render_charts_section():
    """Render the charts section with crime distribution and trends"""
    
    # Sample data matching the TSX
    crime_type_data = [
        {"name": "Theft", "value": 450},
        {"name": "Assault", "value": 320},
        {"name": "Burglary", "value": 280},
        {"name": "Robbery", "value": 190},
        {"name": "Vandalism", "value": 150},
    ]

    monthly_trend_data = [
        {"month": "Jan", "crimes": 420},
        {"month": "Feb", "crimes": 380},
        {"month": "Mar", "crimes": 450},
        {"month": "Apr", "crimes": 490},
        {"month": "May", "crimes": 520},
        {"month": "Jun", "crimes": 480},
        {"month": "Jul", "crimes": 510},
        {"month": "Aug", "crimes": 470},
    ]

    COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
    
    st.markdown("""
    <style>
    .chart-card {
        background: #1a1a2e;
        border: 1px solid #374151;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .chart-title {
        color: white;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .full-width-card {
        grid-column: 1 / -1;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create two columns for the first two charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Crime Distribution Pie Chart
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="chart-title">Crime Distribution by Type</h3>', unsafe_allow_html=True)
        
        df_pie = pd.DataFrame(crime_type_data)
        fig_pie = px.pie(
            df_pie,
            values='value',
            names='name',
            color_discrete_sequence=COLORS
        )
        
        # Customize the pie chart
        fig_pie.update_traces(
            textposition='inside',
            textinfo='percent+label',
            insidetextorientation='radial',
            marker=dict(line=dict(color='#1a1a2e', width=2))
        )
        
        fig_pie.update_layout(
            height=400,
            showlegend=False,
            paper_bgcolor='#1a1a2e',
            plot_bgcolor='#1a1a2e',
            font=dict(color='white'),
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Monthly Trend Line Chart
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="chart-title">Monthly Crime Trend</h3>', unsafe_allow_html=True)
        
        df_line = pd.DataFrame(monthly_trend_data)
        fig_line = px.line(
            df_line,
            x='month',
            y='crimes',
            markers=True
        )
        
        # Customize the line chart
        fig_line.update_traces(
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8, color='#1f77b4')
        )
        
        fig_line.update_layout(
            height=400,
            xaxis=dict(
                showgrid=True,
                gridcolor='#444',
                tickfont=dict(color='#888')
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='#444',
                tickfont=dict(color='#888')
            ),
            paper_bgcolor='#1a1a2e',
            plot_bgcolor='#1a1a2e',
            font=dict(color='white'),
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig_line, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Full width bar chart
    st.markdown('<div class="chart-card full-width-card">', unsafe_allow_html=True)
    st.markdown('<h3 class="chart-title">Crime Types Comparison</h3>', unsafe_allow_html=True)
    
    df_bar = pd.DataFrame(crime_type_data)
    fig_bar = px.bar(
        df_bar,
        x='name',
        y='value',
        color='name',
        color_discrete_sequence=COLORS
    )
    
    # Customize the bar chart
    fig_bar.update_layout(
        height=400,
        xaxis=dict(
            title="",
            showgrid=True,
            gridcolor='#444',
            tickfont=dict(color='#888')
        ),
        yaxis=dict(
            title="",
            showgrid=True,
            gridcolor='#444',
            tickfont=dict(color='#888')
        ),
        paper_bgcolor='#1a1a2e',
        plot_bgcolor='#1a1a2e',
        font=dict(color='white'),
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Optional: Function to update charts with real data
def update_charts_with_data(crime_data, trend_data):
    """Update charts with real data from backend"""
    # This can be used to dynamically update charts when you have real data
    pass
'''


import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def render_charts_section():
    """Render the charts section with crime distribution and trends"""
    
    # Sample data matching the TSX
    crime_type_data = [
        {"name": "Theft", "value": 450},
        {"name": "Assault", "value": 320},
        {"name": "Burglary", "value": 280},
        {"name": "Robbery", "value": 190},
        {"name": "Vandalism", "value": 150},
    ]

    monthly_trend_data = [
        {"month": "Jan", "crimes": 420},
        {"month": "Feb", "crimes": 380},
        {"month": "Mar", "crimes": 450},
        {"month": "Apr", "crimes": 490},
        {"month": "May", "crimes": 520},
        {"month": "Jun", "crimes": 480},
        {"month": "Jul", "crimes": 510},
        {"month": "Aug", "crimes": 470},
    ]

    COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
    
    st.markdown("""
    <style>
    .chart-card {
        background: #1a1a2e;
        border: 1px solid #374151;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .chart-title {
        color: white;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .full-width-card {
        grid-column: 1 / -1;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create two columns for the first two charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Crime Distribution Pie Chart
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="chart-title">Crime Distribution by Type</h3>', unsafe_allow_html=True)
        
        df_pie = pd.DataFrame(crime_type_data)
        fig_pie = px.pie(
            df_pie,
            values='value',
            names='name',
            color_discrete_sequence=COLORS
        )
        
        # Customize the pie chart
        fig_pie.update_traces(
            textposition='inside',
            textinfo='percent+label',
            insidetextorientation='radial',
            marker=dict(line=dict(color='#1a1a2e', width=2))
        )
        
        fig_pie.update_layout(
            height=400,
            showlegend=False,
            paper_bgcolor='#1a1a2e',
            plot_bgcolor='#1a1a2e',
            font=dict(color='white'),
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        # Added unique key parameter
        st.plotly_chart(fig_pie, use_container_width=True, key="crime_distribution_pie")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Monthly Trend Line Chart
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="chart-title">Monthly Crime Trend</h3>', unsafe_allow_html=True)
        
        df_line = pd.DataFrame(monthly_trend_data)
        fig_line = px.line(
            df_line,
            x='month',
            y='crimes',
            markers=True
        )
        
        # Customize the line chart
        fig_line.update_traces(
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8, color='#1f77b4')
        )
        
        fig_line.update_layout(
            height=400,
            xaxis=dict(
                showgrid=True,
                gridcolor='#444',
                tickfont=dict(color='#888')
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='#444',
                tickfont=dict(color='#888')
            ),
            paper_bgcolor='#1a1a2e',
            plot_bgcolor='#1a1a2e',
            font=dict(color='white'),
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        # Added unique key parameter
        st.plotly_chart(fig_line, use_container_width=True, key="monthly_trend_line")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Full width bar chart
    st.markdown('<div class="chart-card full-width-card">', unsafe_allow_html=True)
    st.markdown('<h3 class="chart-title">Crime Types Comparison</h3>', unsafe_allow_html=True)
    
    df_bar = pd.DataFrame(crime_type_data)
    fig_bar = px.bar(
        df_bar,
        x='name',
        y='value',
        color='name',
        color_discrete_sequence=COLORS
    )
    
    # Customize the bar chart
    fig_bar.update_layout(
        height=400,
        xaxis=dict(
            title="",
            showgrid=True,
            gridcolor='#444',
            tickfont=dict(color='#888')
        ),
        yaxis=dict(
            title="",
            showgrid=True,
            gridcolor='#444',
            tickfont=dict(color='#888')
        ),
        paper_bgcolor='#1a1a2e',
        plot_bgcolor='#1a1a2e',
        font=dict(color='white'),
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    # Added unique key parameter
    st.plotly_chart(fig_bar, use_container_width=True, key="crime_comparison_bar")
    st.markdown('</div>', unsafe_allow_html=True)

# Optional: Function to update charts with real data
def update_charts_with_data(crime_data, trend_data):
    """Update charts with real data from backend"""
    # This can be used to dynamically update charts when you have real data
    pass