from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="From 4G to 6G", page_icon="📶", layout="wide")

# Quiet, low-colour design: neutral surfaces and one restrained accent.
st.markdown("""
<style>
:root { color-scheme: light; }
.stApp { background: #f6f7f8; color: #20262e; }
.block-container { max-width: 1180px; padding-top: 2.1rem; padding-bottom: 3rem; }
section[data-testid="stSidebar"] { background: #eef0f2; border-right: 1px solid #dfe3e7; }
h1, h2, h3 { letter-spacing: -0.035em; color: #20262e; }
.eyebrow { color: #647180; text-transform: uppercase; letter-spacing: .12em; font-size: .76rem; font-weight: 650; }
.intro { color: #5f6b78; font-size: 1.05rem; max-width: 780px; line-height: 1.65; }
.note { border: 1px solid #dfe3e7; border-left: 3px solid #7a8795; border-radius: 8px; padding: 14px 16px; background: #fff; color: #53606d; }
div[data-testid="stMetric"] { background: #fff; border: 1px solid #e1e5e9; padding: 16px 18px; border-radius: 10px; }
div[data-testid="stMetricLabel"] { color: #65717e; }
hr { border-color: #e0e4e8; }
</style>
""", unsafe_allow_html=True)

TECHS = ["4G LTE", "5G NSA", "5G SA", "6G Testbed (Simulated)"]
KPI = pd.DataFrame({
    "Technology": TECHS,
    "Average download (Mbps)": [31.94, 198.33, 429.85, 1651.73],
    "Average upload (Mbps)": [10.07, 33.61, 74.58, 502.97],
    "Average latency (ms)": [52.53, 25.80, 10.59, 0.93],
    "Energy (kWh per GB)": [0.06, 0.04, 0.03, 0.01],
    "Customer satisfaction (out of 5)": [3.91, 4.64, 4.88, 4.92],
    "Monthly revenue per user (INR)": [180.56, 261.66, 346.52, 904.58],
})
CITY = pd.DataFrame({
    "City tier": ["Metro", "Tier-2", "Tier-3"],
    "4G LTE": [36.1, 28.8, 21.9],
    "5G NSA": [221.9, 180.7, 139.3],
    "5G SA": [490.5, 385.4, 296.8],
    "6G Testbed (Simulated)": [1867.1, 1479.6, 1230.3],
})
PEAK = pd.DataFrame({
    "Technology": TECHS,
    "Off-peak download (Mbps)": [34.8, 215.3, 466.5, 1768.6],
    "Peak download (Mbps)": [23.8, 148.3, 328.8, 1256.0],
    "Speed drop (%)": [32, 31, 30, 29],
})
SLA = pd.DataFrame({
    "Use case": ["AR/VR", "Autonomous Vehicles", "Industrial IoT", "Online Gaming", "Remote Work", "Smart City IoT", "Telemedicine", "Video Streaming"],
    "Maximum latency (ms)": [10, 5, 10, 20, 50, 100, 10, 50],
    "4G LTE": [0, 0, 0, 0, 49, 100, 0, 48],
    "5G NSA": [0, 0, 0, 15, 100, 100, 0, 100],
    "5G SA": [45, 0, 41, 100, 100, 100, 47, 100],
    "6G Testbed (Simulated)": [100, 100, 100, 100, 100, 100, 100, 100],
})

st.sidebar.markdown("## Explore the analysis")
page = st.sidebar.radio("Sections", ["Overview", "Network performance", "City access", "Peak-hour congestion", "Use-case fit", "About the data"], label_visibility="collapsed")
st.sidebar.markdown("---")
st.sidebar.caption("Built from the accompanying Jupyter notebook. The notebook's data is synthetic; 6G is simulated.")

st.markdown('<div class="eyebrow">Network performance · research dashboard</div>', unsafe_allow_html=True)
st.title("From 4G to 6G")
st.markdown('<p class="intro">A clear, practical look at network performance and business impact — from download speed and latency to city-level access and service requirements.</p>', unsafe_allow_html=True)
st.markdown('<div class="note"><strong>Read this first:</strong> these figures come from a synthetic dataset, not a live telecom feed. The 6G results are simulated, and use-case latency limits are assumptions documented in the notebook.</div>', unsafe_allow_html=True)
st.write("")

if page == "Overview":
    st.subheader("The short version")
    a, b, c, d = st.columns(4)
    a.metric("5G SA download", "429.85 Mbps", "vs 31.94 Mbps on 4G")
    b.metric("5G SA latency", "10.59 ms", "vs 52.53 ms on 4G")
    c.metric("Tier-3 5G SA speed", "296.8 Mbps", "39% below metro")
    d.metric("Peak-hour speed drop", "29–32%", "across all generations")
    st.write("")
    left, right = st.columns([1.25, 1])
    with left:
        st.markdown("#### Download speed by generation")
        chart = px.bar(KPI, x="Technology", y="Average download (Mbps)", color_discrete_sequence=["#667788"])
        chart.update_layout(showlegend=False, plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=10,r=10,t=20,b=10), xaxis_title="", yaxis_title="Mbps")
        chart.update_xaxes(tickangle=-15, gridcolor="#edf0f2")
        chart.update_yaxes(gridcolor="#edf0f2")
        st.plotly_chart(chart, use_container_width=True)
    with right:
        st.markdown("#### What stands out")
        st.markdown("**5G standalone is the strongest practical step-up in this dataset.** It combines higher speed with lower latency than 4G and 5G NSA.")
        st.markdown("**Access is uneven.** Average 5G SA download speed is lower in Tier-2 and Tier-3 cities than in metros.")
        st.markdown("**Busy hours matter.** Peak-hour speeds fall by roughly 30% regardless of generation.")
        st.markdown("**Treat 6G carefully.** Its very high results are simulated targets, not proof of a deployed network's performance.")
    st.markdown("#### Key performance indicators")
    st.dataframe(KPI, hide_index=True, use_container_width=True)

elif page == "Network performance":
    st.subheader("Compare network generations")
    metric = st.selectbox("Choose a metric", ["Average download (Mbps)", "Average upload (Mbps)", "Average latency (ms)", "Energy (kWh per GB)", "Customer satisfaction (out of 5)", "Monthly revenue per user (INR)"])
    chart = px.bar(KPI, x="Technology", y=metric, color_discrete_sequence=["#667788"])
    chart.update_layout(showlegend=False, plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=10,r=10,t=25,b=10), xaxis_title="", yaxis_title=metric)
    chart.update_xaxes(tickangle=-15, gridcolor="#edf0f2")
    chart.update_yaxes(gridcolor="#edf0f2")
    st.plotly_chart(chart, use_container_width=True)
    st.dataframe(KPI, hide_index=True, use_container_width=True)

elif page == "City access":
    st.subheader("The digital divide: metro vs smaller cities")
    st.caption("Average download speed in Mbps, as reported by the notebook's grouped results.")
    chosen = st.multiselect("Network generations", TECHS, default=["4G LTE", "5G NSA", "5G SA"])
    melted = CITY.melt(id_vars="City tier", var_name="Technology", value_name="Average download (Mbps)")
    melted = melted[melted["Technology"].isin(chosen)]
    chart = px.bar(melted, x="City tier", y="Average download (Mbps)", color="Technology", barmode="group", color_discrete_sequence=["#8c969f", "#667788", "#34495e", "#b6bdc4"])
    chart.update_layout(plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=10,r=10,t=20,b=10), legend_title_text="", xaxis_title="", yaxis_title="Mbps")
    chart.update_yaxes(gridcolor="#edf0f2")
    st.plotly_chart(chart, use_container_width=True)
    st.dataframe(CITY, hide_index=True, use_container_width=True)
    st.markdown('<div class="note">In the notebook results, Tier-3 5G SA averages about 296.8 Mbps, compared with 490.5 Mbps in metro areas — approximately 39% lower.</div>', unsafe_allow_html=True)

elif page == "Peak-hour congestion":
    st.subheader("Peak hours reduce speed across generations")
    st.caption("The notebook defines peak hours as 18:00–23:00.")
    selected = st.multiselect("Network generations", TECHS, default=TECHS)
    data = PEAK[PEAK["Technology"].isin(selected)]
    compare = data.melt(id_vars=["Technology", "Speed drop (%)"], value_vars=["Off-peak download (Mbps)", "Peak download (Mbps)"], var_name="Period", value_name="Download (Mbps)")
    chart = px.bar(compare, x="Technology", y="Download (Mbps)", color="Period", barmode="group", color_discrete_sequence=["#aeb7c0", "#526578"])
    chart.update_layout(plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=10,r=10,t=20,b=10), legend_title_text="", xaxis_title="", yaxis_title="Mbps")
    chart.update_xaxes(tickangle=-15, gridcolor="#edf0f2")
    chart.update_yaxes(gridcolor="#edf0f2")
    st.plotly_chart(chart, use_container_width=True)
    st.dataframe(data, hide_index=True, use_container_width=True)

elif page == "Use-case fit":
    st.subheader("Does latency meet the use-case requirement?")
    st.caption("Percent of records meeting each maximum latency threshold in the notebook. Thresholds are assumptions, not universal standards.")
    generation = st.selectbox("Network generation", TECHS, index=2)
    view = SLA[["Use case", "Maximum latency (ms)", generation]].rename(columns={generation: "Records meeting threshold (%)"})
    chart = px.bar(view, x="Use case", y="Records meeting threshold (%)", color_discrete_sequence=["#667788"])
    chart.update_layout(showlegend=False, plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=10,r=10,t=20,b=10), xaxis_title="", yaxis_title="Records meeting threshold (%)", yaxis_range=[0,100])
    chart.update_xaxes(tickangle=-25, gridcolor="#edf0f2")
    chart.update_yaxes(gridcolor="#edf0f2")
    st.plotly_chart(chart, use_container_width=True)
    st.dataframe(view, hide_index=True, use_container_width=True)
    st.markdown('<div class="note">The notebook reports that autonomous-vehicle use cases meet the 5 ms threshold 0% of the time on 5G SA. The simulated 6G rows meet all listed thresholds in this synthetic dataset.</div>', unsafe_allow_html=True)

else:
    st.subheader("About the analysis")
    st.markdown("This dashboard is based on `5G_6G_analysis.ipynb`, which compares 4G LTE, 5G NSA, 5G SA, and simulated 6G across speed, latency, congestion, energy, revenue, and customer satisfaction.")
    st.markdown("#### Limitations stated in the notebook")
    st.markdown("- The dataset is synthetic, with 6G rows simulated from published research targets.\n- Use-case latency thresholds are assumptions.\n- Results should not be presented as live network measurements.\n- The notebook suggests replacing synthetic data with sources such as Ookla or TRAI data for future validation.")
    st.markdown("#### Files included")
    st.code("5G_6G_analysis.ipynb  # original analysis\napp.py                 # Python dashboard\nrequirements.txt        # packages needed\nREADME.md               # setup instructions", language="text")

st.divider()
st.caption("A student research dashboard · Built with Python and Streamlit · Results are illustrative, not live network telemetry.")
