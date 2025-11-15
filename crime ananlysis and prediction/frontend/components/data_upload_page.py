import streamlit as st
import requests
import pandas as pd
import time
import io
from datetime import datetime

API_BASE = "http://172.16.2.69:5000"

def render_data_upload():
    """Render the complete data upload and processing page"""
    
    # Initialize session state
    if 'upload_state' not in st.session_state:
        st.session_state.upload_state = "idle"
    if 'upload_progress' not in st.session_state:
        st.session_state.upload_progress = 0
    if 'file_name' not in st.session_state:
        st.session_state.file_name = ""
    if 'file_size' not in st.session_state:
        st.session_state.file_size = ""
    if 'show_preview' not in st.session_state:
        st.session_state.show_preview = False
    if 'uploaded_data' not in st.session_state:
        st.session_state.uploaded_data = None
    
    # Page header
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h2 style="color: white; font-size: 1.875rem; font-weight: 600; margin-bottom: 0.5rem;">
            Data Upload & Processing
        </h2>
        <p style="color: #9ca3af; font-size: 1.125rem; margin: 0;">
            Upload and process crime datasets for analysis
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Render based on current state
    if st.session_state.upload_state == "idle":
        render_idle_state()
    elif st.session_state.upload_state == "uploading":
        render_uploading_state()
    elif st.session_state.upload_state == "processing":
        render_processing_state()
    elif st.session_state.upload_state == "success":
        if st.session_state.show_preview:
            render_preview_state()
        else:
            render_success_state()
    elif st.session_state.upload_state == "error":
        render_error_state()

def render_idle_state():
    """Render the initial upload state"""
    st.markdown("""
    <style>
    .upload-container {
        background: #1a1a2e;
        border: 1px solid #374151;
        border-radius: 0.75rem;
        padding: 2rem;
    }
    .upload-zone {
        border: 2px dashed #4b5563;
        border-radius: 0.5rem;
        padding: 3rem 2rem;
        text-align: center;
        background: rgba(255,255,255,0.02);
        transition: all 0.3s ease;
        margin-bottom: 1.5rem;
    }
    .upload-zone:hover {
        border-color: #1f77b4;
        background: rgba(31, 119, 180, 0.05);
    }
    .upload-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        opacity: 0.7;
    }
    .upload-text {
        color: #d1d5db;
        font-size: 1.25rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    .upload-hint {
        color: #9ca3af;
        font-size: 0.875rem;
        margin-bottom: 1.5rem;
    }
    .info-box {
        background: rgba(55, 65, 81, 0.5);
        border-radius: 0.5rem;
        padding: 1rem;
        margin-top: 1.5rem;
    }
    .info-title {
        color: white;
        font-weight: 500;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .column-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.75rem;
    }
    .column-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: #9ca3af;
        font-size: 0.875rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    
    # Upload zone
    st.markdown("""
    <div class="upload-zone">
        <div class="upload-icon">📁</div>
        <div class="upload-text">Upload Crime Dataset</div>
        <div class="upload-hint">
            Drag and drop your CSV file here or click to browse
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose CSV file",
        type=["csv"],
        label_visibility="collapsed",
        key="data_uploader"
    )
    
    if uploaded_file is not None:
        handle_file_selection(uploaded_file)
    
    # Requirements info
    st.markdown("""
    <div class="info-box">
        <div class="info-title">
            <span style="color: #1f77b4;">ℹ️</span> Required CSV Columns
        </div>
        <div class="column-grid">
            <div class="column-item">
                <span style="color: #1f77b4;">📅</span> Date
            </div>
            <div class="column-item">
                <span style="color: #1f77b4;">📊</span> Crime Type
            </div>
            <div class="column-item">
                <span style="color: #1f77b4;">📍</span> Location
            </div>
            <div class="column-item">
                <span style="color: #1f77b4;">⚠️</span> Severity
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # File requirements
    st.markdown("""
    <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 1rem; color: #6b7280; font-size: 0.875rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem;">
            <span>📄</span> Supported format: CSV only
        </div>
        <div style="display: flex; align-items: center; gap: 0.5rem;">
            <span>💾</span> Maximum file size: 100 MB
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def handle_file_selection(uploaded_file):
    """Handle file selection and validation"""
    if not uploaded_file.name.endswith('.csv'):
        st.session_state.upload_state = "error"
        st.session_state.file_name = uploaded_file.name
        st.rerun()
        return
    
    if uploaded_file.size > 100 * 1024 * 1024:  # 100 MB
        st.session_state.upload_state = "error"
        st.session_state.file_name = uploaded_file.name
        st.rerun()
        return
    
    st.session_state.file_name = uploaded_file.name
    st.session_state.file_size = f"{uploaded_file.size / (1024 * 1024):.2f} MB"
    st.session_state.upload_state = "uploading"
    st.session_state.upload_progress = 0
    st.rerun()

def render_uploading_state():
    """Render uploading progress state"""
    st.markdown("""
    <style>
    .progress-container {
        background: #1a1a2e;
        border: 1px solid #374151;
        border-radius: 0.75rem;
        padding: 2rem;
        text-align: center;
    }
    .progress-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 5rem;
        height: 5rem;
        background: rgba(31, 119, 180, 0.2);
        border-radius: 50%;
        margin-bottom: 1rem;
    }
    .progress-title {
        color: white;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .progress-file {
        color: #9ca3af;
        margin-bottom: 0.25rem;
    }
    .progress-size {
        color: #6b7280;
        font-size: 0.875rem;
    }
    .progress-bar-container {
        margin: 2rem 0;
    }
    .progress-info {
        display: flex;
        justify-content: between;
        color: #9ca3af;
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="progress-container">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="progress-icon">
        <span style="font-size: 2rem; color: #1f77b4;">⏳</span>
    </div>
    <div class="progress-title">Uploading File...</div>
    <div class="progress-file">{}</div>
    <div class="progress-size">{}</div>
    """.format(st.session_state.file_name, st.session_state.file_size), unsafe_allow_html=True)
    
    # Progress bar
    progress = st.progress(st.session_state.upload_progress)
    
    # Simulate upload progress
    if st.session_state.upload_progress < 100:
        time.sleep(0.1)
        st.session_state.upload_progress += 10
        st.rerun()
    else:
        st.session_state.upload_state = "success"
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_processing_state():
    """Render data processing state"""
    st.markdown("""
    <style>
    .stats-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 1rem;
        margin-top: 1.5rem;
    }
    .stat-box {
        background: rgba(55, 65, 81, 0.5);
        border-radius: 0.5rem;
        padding: 1rem;
        text-align: center;
    }
    .stat-label {
        color: #9ca3af;
        font-size: 0.75rem;
        margin-bottom: 0.25rem;
    }
    .stat-value {
        color: white;
        font-size: 1.25rem;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="progress-container">
        <div class="progress-icon" style="background: rgba(234, 179, 8, 0.2);">
            <span style="font-size: 2rem; color: #eab308;">🔍</span>
        </div>
        <div class="progress-title">Processing Data...</div>
        <div class="progress-file">Analyzing and validating crime dataset</div>
    """, unsafe_allow_html=True)
    
    # Progress bar
    progress = st.progress(st.session_state.upload_progress)
    
    # Stats
    st.markdown("""
    <div class="stats-grid">
        <div class="stat-box">
            <div class="stat-label">Rows Scanned</div>
            <div class="stat-value">{}</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Validated</div>
            <div class="stat-value" style="color: #10b981;">{}</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Errors</div>
            <div class="stat-value" style="color: #ef4444;">{}</div>
        </div>
    </div>
    """.format(
        int((st.session_state.upload_progress / 100) * 5420),
        int((st.session_state.upload_progress / 100) * 5380),
        int((st.session_state.upload_progress / 100) * 40)
    ), unsafe_allow_html=True)
    
    # Simulate processing
    if st.session_state.upload_progress < 100:
        time.sleep(0.15)
        st.session_state.upload_progress += 5
        st.rerun()
    else:
        st.session_state.show_preview = True
        # Load sample data for preview
        st.session_state.uploaded_data = get_sample_data()
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_success_state():
    """Render upload success state"""
    st.markdown("""
    <style>
    .success-container {
        background: #1a1a2e;
        border: 1px solid #374151;
        border-radius: 0.75rem;
        padding: 2rem;
        text-align: center;
    }
    .success-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 5rem;
        height: 5rem;
        background: rgba(16, 185, 129, 0.2);
        border-radius: 50%;
        margin-bottom: 1rem;
    }
    .stats-grid-large {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 1rem;
        margin: 2rem 0;
    }
    .stat-box-large {
        background: rgba(55, 65, 81, 0.5);
        border-radius: 0.5rem;
        padding: 1.5rem;
        text-align: center;
    }
    .alert-success {
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1.5rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: #10b981;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="success-container">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-icon">
        <span style="font-size: 2rem; color: #10b981;">✅</span>
    </div>
    <div class="progress-title">Upload Successful!</div>
    <div class="progress-file">{}</div>
    <div class="progress-size">{}</div>
    """.format(st.session_state.file_name, st.session_state.file_size), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="alert-success">
        <span>✅</span> File uploaded successfully and ready for processing
    </div>
    """, unsafe_allow_html=True)
    
    # Stats
    st.markdown("""
    <div class="stats-grid-large">
        <div class="stat-box-large">
            <div class="stat-label">Total Records</div>
            <div class="stat-value">5,420</div>
        </div>
        <div class="stat-box-large">
            <div class="stat-label">Date Range</div>
            <div class="stat-value">365</div>
            <div class="stat-label">days</div>
        </div>
        <div class="stat-box-large">
            <div class="stat-label">Locations</div>
            <div class="stat-value">142</div>
        </div>
        <div class="stat-box-large">
            <div class="stat-label">Crime Types</div>
            <div class="stat-value">18</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Process Data", use_container_width=True):
            st.session_state.upload_state = "processing"
            st.session_state.upload_progress = 0
            st.rerun()
    
    with col2:
        if st.button("👁️ View Sample", use_container_width=True):
            st.session_state.show_preview = True
            st.session_state.uploaded_data = get_sample_data()
            st.rerun()
    
    with col3:
        if st.button("📁 Upload New", use_container_width=True):
            reset_upload_state()
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_preview_state():
    """Render data preview state"""
    st.markdown("""
    <style>
    .preview-container {
        background: #1a1a2e;
        border: 1px solid #374151;
        border-radius: 0.75rem;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .preview-header {
        display: flex;
        justify-content: between;
        align-items: center;
        margin-bottom: 1rem;
    }
    .badge-success {
        background: #10b981;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.75rem;
        font-weight: 500;
        display: inline-flex;
        align-items: center;
        gap: 0.25rem;
    }
    .table-container {
        border: 1px solid #374151;
        border-radius: 0.5rem;
        overflow: hidden;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Data Preview Card
    st.markdown('<div class="preview-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        <div style="color: white; font-size: 1.25rem; font-weight: 600; margin-bottom: 0.25rem;">
            Data Preview
        </div>
        <div style="color: #9ca3af; font-size: 0.875rem;">
            Showing first 5 rows of {}
        </div>
        """.format(st.session_state.file_name), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="badge-success">
            <span>✅</span> Processed
        </div>
        """, unsafe_allow_html=True)
    
    # Data table
    if st.session_state.uploaded_data is not None:
        st.dataframe(
            st.session_state.uploaded_data,
            use_container_width=True,
            hide_index=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Quick Statistics Card
    st.markdown('<div class="preview-container">', unsafe_allow_html=True)
    st.markdown("""
    <div style="color: white; font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem;">
        Quick Statistics
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(4)
    stats = [
        ("Total Records", "5,420", "100% valid", "green"),
        ("Most Common", "Theft", "1,842 cases", "white"),
        ("Peak Month", "July", "562 incidents", "white"),
        ("Hotspot Area", "Downtown", "High risk", "red")
    ]
    
    for i, (title, value, subtitle, color) in enumerate(stats):
        with cols[i]:
            st.markdown(f"""
            <div style="background: rgba(55, 65, 81, 0.5); border-radius: 0.5rem; padding: 1rem;">
                <div style="color: #9ca3af; font-size: 0.75rem; margin-bottom: 0.5rem;">{title}</div>
                <div style="color: white; font-size: 1.5rem; font-weight: 600; margin-bottom: 0.25rem;">{value}</div>
                <div style="color: {'#ef4444' if color == 'red' else '#10b981' if color == 'green' else '#9ca3af'}; font-size: 0.75rem;">{subtitle}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📁 Upload New Dataset", use_container_width=True):
            reset_upload_state()
    with col2:
        if st.button("📊 Export Report", use_container_width=True):
            st.success("Report exported successfully!")

def render_error_state():
    """Render error state"""
    st.markdown("""
    <style>
    .error-container {
        background: #1a1a2e;
        border: 1px solid #374151;
        border-radius: 0.75rem;
        padding: 2rem;
        text-align: center;
    }
    .error-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 5rem;
        height: 5rem;
        background: rgba(239, 68, 68, 0.2);
        border-radius: 50%;
        margin-bottom: 1rem;
    }
    .alert-error {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1.5rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: #ef4444;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="error-container">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="error-icon">
        <span style="font-size: 2rem; color: #ef4444;">❌</span>
    </div>
    <div class="progress-title">Upload Failed</div>
    <div class="progress-file">{}</div>
    """.format(st.session_state.file_name), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="alert-error">
        <span>❌</span> Invalid file format or file size exceeds 100 MB. Please upload a valid CSV file.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 Try Again", use_container_width=True):
        reset_upload_state()
    
    st.markdown('</div>', unsafe_allow_html=True)

def get_sample_data():
    """Get sample data for preview"""
    return pd.DataFrame({
        'ID': [1, 2, 3, 4, 5],
        'Date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19'],
        'Crime Type': ['Theft', 'Assault', 'Burglary', 'Vandalism', 'Robbery'],
        'Location': ['Downtown District', 'North Area', 'East Industrial', 'Central Park', 'West Mall'],
        'Severity': ['Medium', 'High', 'High', 'Low', 'High']
    })

def reset_upload_state():
    """Reset all upload state variables"""
    st.session_state.upload_state = "idle"
    st.session_state.upload_progress = 0
    st.session_state.file_name = ""
    st.session_state.file_size = ""
    st.session_state.show_preview = False
    st.session_state.uploaded_data = None
    st.rerun()