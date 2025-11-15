
'''
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_BASE = "http://172.16.2.69:5000"

# --- EXISTING CODE ---
def render_file_upload_card():
    """Render the simplified file upload card"""
    
    if 'current_file_name' not in st.session_state:
        st.session_state.current_file_name = ""
    
    st.markdown("""
    <style>
    .upload-card-simple {
        background: #1a1a2e;
        border: 1px solid #374151;
        border-radius: 0.75rem;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    .upload-card-title {
        color: white;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .upload-zone-simple {
        border: 2px dashed #4b5563;
        border-radius: 0.5rem;
        padding: 2rem;
        text-align: center;
        background: rgba(255,255,255,0.02);
        transition: all 0.3s ease;
    }
    .upload-zone-simple:hover {
        border-color: #1f77b4;
        background: rgba(31, 119, 180, 0.05);
    }
    .upload-icon-simple {
        font-size: 3rem;
        margin-bottom: 1rem;
        opacity: 0.7;
    }
    .upload-text-simple {
        color: #d1d5db;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    .upload-hint-simple {
        color: #9ca3af;
        font-size: 0.875rem;
        margin-bottom: 1rem;
    }
    .file-name-display {
        color: #1f77b4;
        font-weight: 500;
        margin: 1rem 0;
        padding: 0.5rem;
        background: rgba(31, 119, 180, 0.1);
        border-radius: 0.375rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="upload-card-simple">
        <div class="upload-card-title">
            <span>📊</span>
            Upload Crime Data
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="upload-zone-simple">
        <div class="upload-icon-simple">📁</div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choose file",
        type=["csv", "xls", "xlsx"],
        label_visibility="collapsed",
        key="simple_uploader"
    )
    
    if uploaded_file is not None:
        st.session_state.current_file_name = uploaded_file.name
        st.markdown(f"""
        <div class="file-name-display">
            📄 {uploaded_file.name}
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📤 Upload to System", use_container_width=True):
            handle_file_upload(uploaded_file)
    else:
        st.markdown("""
        <div class="upload-text-simple">
            Drag and drop your CSV file here or click to browse
        </div>
        <div class="upload-hint-simple">
            Supports CSV, XLS, XLSX (Max 10MB)
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def handle_file_upload(uploaded_file):
    """Handle file upload to backend"""
    with st.spinner("Uploading file..."):
        try:
            files = {"file": (uploaded_file.name, uploaded_file, "text/csv")}
            response = requests.post(f"{API_BASE}/api/upload", files=files, timeout=30)
            
            if response.status_code == 200:
                st.success("✅ File uploaded successfully!")
                response_data = response.json()
                if response_data:
                    with st.expander("📋 Upload Results", expanded=True):
                        st.json(response_data)
                st.session_state.current_file_name = ""
                st.rerun()
            else:
                st.error(f"❌ Upload failed: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("🚫 Cannot connect to backend server. Please make sure the backend is running.")
        except requests.exceptions.Timeout:
            st.error("⏰ Upload timeout. Please try again.")
        except Exception as e:
            st.error(f"💥 Unexpected error: {e}")

# --- NEW DASHBOARD RENDER FUNCTION ---
def render_dashboard():
    """Render main dashboard with upload + visual analytics"""
    st.title("🧠 AI Crime Dashboard Overview")

    # 1️⃣ File upload card
    render_file_upload_card()

    st.divider()

    # 2️⃣ Fetch stats from backend
    st.subheader("📈 Live Statistics")
    try:
        response = requests.get(f"{API_BASE}/api/stats", timeout=10)
        response.raise_for_status()
        stats = response.json()
    except Exception as e:
        st.error(f"⚠️ Could not fetch backend stats: {e}")
        return

    cols = st.columns(4)
    cols[0].metric("Total Crimes", stats.get("totalCrimes", 0), stats.get("totalDelta", 0))
    cols[1].metric("Violent Crimes", stats.get("violentCrimes", 0), stats.get("violentDelta", 0))
    cols[2].metric("Prediction Accuracy", f"{stats.get('predictionAccuracy', 0)}%", stats.get("accuracyDelta", 0))
    cols[3].metric("Cities Covered", stats.get("citiesCovered", 0), stats.get("citiesDelta", 0))

    st.divider()

    # 3️⃣ Charts
    st.subheader("📊 Visual Analytics")

    if "monthlyTrend" in stats and stats["monthlyTrend"]:
        df = pd.DataFrame(stats["monthlyTrend"])
        fig = px.line(df, x="name", y="value", markers=True, title="Monthly Crime Trend", color_discrete_sequence=["#0EA5E9"])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No monthly trend data available.")

    if "distributionByType" in stats and stats["distributionByType"]:
        df2 = pd.DataFrame(stats["distributionByType"])
        fig2 = px.pie(df2, values="value", names="type", title="Crime Distribution by Type")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No distribution data available.")

    st.caption("© 2025 AI Crime Analysis Dashboard — Powered by Streamlit + Flask")

'''


import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_BASE = "http://172.16.2.69:5000"

# --- EXISTING CODE ---
def render_file_upload_card():
    """Render the simplified file upload card"""
    
    if 'current_file_name' not in st.session_state:
        st.session_state.current_file_name = ""
    
    st.markdown("""
    <style>
    .upload-card-simple {
        background: #1a1a2e;
        border: 1px solid #374151;
        border-radius: 0.75rem;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    .upload-card-title {
        color: white;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .upload-zone-simple {
        border: 2px dashed #4b5563;
        border-radius: 0.5rem;
        padding: 2rem;
        text-align: center;
        background: rgba(255,255,255,0.02);
        transition: all 0.3s ease;
    }
    .upload-zone-simple:hover {
        border-color: #1f77b4;
        background: rgba(31, 119, 180, 0.05);
    }
    .upload-icon-simple {
        font-size: 3rem;
        margin-bottom: 1rem;
        opacity: 0.7;
    }
    .upload-text-simple {
        color: #d1d5db;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    .upload-hint-simple {
        color: #9ca3af;
        font-size: 0.875rem;
        margin-bottom: 1rem;
    }
    .file-name-display {
        color: #1f77b4;
        font-weight: 500;
        margin: 1rem 0;
        padding: 0.5rem;
        background: rgba(31, 119, 180, 0.1);
        border-radius: 0.375rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="upload-card-simple">
        <div class="upload-card-title">
            <span>📊</span>
            Upload Crime Data
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="upload-zone-simple">
        <div class="upload-icon-simple">📁</div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choose file",
        type=["csv", "xls", "xlsx"],
        label_visibility="collapsed",
        key="simple_uploader"
    )
    
    if uploaded_file is not None:
        st.session_state.current_file_name = uploaded_file.name
        st.markdown(f"""
        <div class="file-name-display">
            📄 {uploaded_file.name}
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📤 Upload to System", use_container_width=True):
            handle_file_upload(uploaded_file)
    else:
        st.markdown("""
        <div class="upload-text-simple">
            Drag and drop your CSV file here or click to browse
        </div>
        <div class="upload-hint-simple">
            Supports CSV, XLS, XLSX (Max 10MB)
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def handle_file_upload(uploaded_file):
    """Handle file upload to backend"""
    with st.spinner("Uploading file..."):
        try:
            files = {"file": (uploaded_file.name, uploaded_file, "text/csv")}
            response = requests.post(f"{API_BASE}/api/upload", files=files, timeout=30)
            
            if response.status_code == 200:
                st.success("✅ File uploaded successfully!")
                response_data = response.json()
                if response_data:
                    with st.expander("📋 Upload Results", expanded=True):
                        st.json(response_data)
                st.session_state.current_file_name = ""
                st.rerun()
            else:
                st.error(f"❌ Upload failed: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("🚫 Cannot connect to backend server. Please make sure the backend is running.")
        except requests.exceptions.Timeout:
            st.error("⏰ Upload timeout. Please try again.")
        except Exception as e:
            st.error(f"💥 Unexpected error: {e}")


# --- NEW DASHBOARD RENDER FUNCTION ---
def render_dashboard():
    """Render main dashboard with upload + visual analytics"""
    st.title("🧠 AI Crime Dashboard Overview")

    # 1️⃣ File upload card
    render_file_upload_card()

    st.divider()

    # 2️⃣ Fetch stats from backend
    st.subheader("📈 Live Statistics")
    try:
        response = requests.get(f"{API_BASE}/api/stats", timeout=10)
        response.raise_for_status()
        stats = response.json()
    except Exception as e:
        st.error(f"⚠️ Could not fetch backend stats: {e}")
        return

    cols = st.columns(4)
    cols[0].metric("Total Crimes", stats.get("totalCrimes", 0), stats.get("totalDelta", 0))
    cols[1].metric("Violent Crimes", stats.get("violentCrimes", 0), stats.get("violentDelta", 0))
    cols[2].metric("Prediction Accuracy", f"{stats.get('predictionAccuracy', 0)}%", stats.get("accuracyDelta", 0))
    cols[3].metric("Cities Covered", stats.get("citiesCovered", 0), stats.get("citiesDelta", 0))

    st.divider()

    # 3️⃣ Charts
    st.subheader("📊 Visual Analytics")

    if "monthlyTrend" in stats and stats["monthlyTrend"]:
        df = pd.DataFrame(stats["monthlyTrend"])
        fig = px.line(df, x="name", y="value", markers=True, title="Monthly Crime Trend", color_discrete_sequence=["#0EA5E9"])
        st.plotly_chart(fig, use_container_width=True, key="dashboard_monthly_trend")
    else:
        st.info("No monthly trend data available.")

    if "distributionByType" in stats and stats["distributionByType"]:
        df2 = pd.DataFrame(stats["distributionByType"])
        fig2 = px.pie(df2, values="value", names="type", title="Crime Distribution by Type")
        st.plotly_chart(fig2, use_container_width=True, key="crime_distribution_pie")
    else:
        st.info("No distribution data available.")

    st.caption("©️ 2025 AI Crime Analysis Dashboard — Powered by Streamlit + Flask")