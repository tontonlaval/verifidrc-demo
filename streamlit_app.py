import streamlit as st
import time
import pandas as pd
import random

# Page Configuration
st.set_page_config(
    page_title="VerifiDRC | AI Skill Verification",
    page_icon="🇨🇩",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
    .main-header { font-size: 2.2rem; font-weight: 700; color: #1E3A8A; }
    .sub-header { font-size: 1.1rem; color: #4B5563; margin-bottom: 20px; }
    .badge-box { background-color: #F3F4F6; padding: 15px; border-radius: 8px; border-left: 5px solid #2563EB; }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="main-header">🇨🇩 VerifiDRC</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">An Anonymous, Skill-Verified Talent Marketplace for DRC — Powered by Google AI</div>', unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(["Candidate AI Audit (Demo)", "Employer Matchmaking Bridge", "DRC Architecture & Impact"])

# ---------------------------------------------------------
# TAB 1: CANDIDATE AI AUDIT
# ---------------------------------------------------------
with tab1:
    st.subheader("Candidate Vetting Engine")
    st.caption("Simulates dynamic skill evaluation powered by Gemini and PII stripping powered by Gemma 2.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        trade = st.selectbox(
            "Select Trade Category:",
            [
                "Education (Secondary School Teacher)",
                "Domestic & Care (Nanny / Housekeeper)",
                "Technical (Solar Inverter & Energy Technician)",
                "Corporate (Accounting & Admin Assistant)"
            ]
        )
        
        # Dynamic Scenarios
        scenarios = {
            "Education (Secondary School Teacher)": "Describe your pedagogical approach when a student consistently struggles with basic algebra in a overcrowded classroom.",
            "Domestic & Care (Nanny / Housekeeper)": "How do you respond if a toddler suddenly shows signs of fever while parents are away in Kinshasa traffic?",
            "Technical (Solar Inverter & Energy Technician)": "An Ekotek hybrid inverter shows low battery voltage during utility grid charging. What program settings (e.g. Program 01/16) do you troubleshoot first?",
            "Corporate (Accounting & Admin Assistant)": "How do you reconcile an unverified petty cash discrepancy of $150 before weekly payroll close?"
        }
        
        st.info(f"**Practical Assessment Challenge:**\n\n{scenarios[trade]}")
        
        candidate_input = st.text_area(
            "Candidate Real-World Response (Text or Voice Script Transcripts):",
            height=130,
            placeholder="Type practical scenario response here..."
        )
        
        audit_btn = st.button("Submit for Gemini AI Audit", type="primary")

    with col2:
        if audit_btn:
            if not candidate_input.strip():
                st.warning("Please enter a response to run the audit.")
            else:
                with st.spinner("Gemma 2 stripping PII (Name, Location, Dialect)..."):
                    time.sleep(1)
                with st.spinner("Gemini Pro auditing practical output competence..."):
                    time.sleep(1.5)
                
                st.success("✅ Audit Complete & Profile Vectorized")
                
                # Metrics Row
                m1, m2, m3 = st.columns(3)
                m1.metric("Competency Score", "94 / 100")
                m2.metric("Trust Level", "Verified ✅")
                m3.metric("Anonymized ID", "VEC-DRC-88204")
                
                st.markdown("### Gemma 2 Anonymization Log")
                st.code("""
[RAW DATA]: Stripped name, phone number, and location (Kinshasa, Gombe).
[VECTOR KEY]: VEC-DRC-88204-KIN
[BIAS SHIELD]: Gender, age, and family network hidden from employer view.
                """, language="text")
                
                st.markdown("### Verified Skill Vector Breakdown")
                st.progress(0.95, text="Trade Problem-Solving (95%)")
                st.progress(0.90, text="Situational Reliability (90%)")
                st.progress(0.92, text="Domain Logic & Execution (92%)")

# ---------------------------------------------------------
# TAB 2: EMPLOYER MATCHMAKING BRIDGE
# ---------------------------------------------------------
with tab2:
    st.subheader("Active Employer Matchmaking Portal")
    st.caption("Proactively bridges vetted candidate vectors directly to verified employer demand.")
    
    col_e1, col_e2 = st.columns([1, 2])
    
    with col_e1:
        st.markdown("**Post Open Role**")
        emp_city = st.selectbox("Select Target City:", ["Kinshasa", "Lubumbashi", "Goma", "Matadi", "Bukavu"])
        emp_trade = st.selectbox("Required Trade:", ["Education", "Domestic Services", "Solar/Technical", "Accounting"])
        min_score = st.slider("Minimum Skill Audit Score:", 70, 95, 85)
        
        search_btn = st.button("Find Matched Talent Vectors")

    with col_e2:
        st.markdown(f"**Live Match Candidates in {emp_city}**")
        
        # Sample Matched Data
        data = [
            {"Candidate Vector ID": "VEC-DRC-88204", "City": emp_city, "Verified Skill Score": "94/100", "Identity Status": "Fully Anonymized", "Payment Rail": "M-Pesa Verified"},
            {"Candidate Vector ID": "VEC-DRC-77312", "City": emp_city, "Verified Skill Score": "89/100", "Identity Status": "Fully Anonymized", "Payment Rail": "Orange Money Verified"},
            {"Candidate Vector ID": "VEC-DRC-91024", "City": emp_city, "Verified Skill Score": "87/100", "Identity Status": "Fully Anonymized", "Payment Rail": "Airtel Money Verified"}
        ]
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        if st.button("Trigger Proactive Job Push Alerts to Candidates"):
            st.success(f"📱 Automated job alert sent via local SMS/Mobile channels to 3 matched candidates in {emp_city}!")

# ---------------------------------------------------------
# TAB 3: DRC ARCHITECTURE & METRICS
# ---------------------------------------------------------
with tab3:
    st.subheader("National Reach & Technical Architecture")
    
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("Coverage", "Nationwide DRC")
    m_col2.metric("Key Hubs", "Kinshasa, Lubumbashi, Goma")
    m_col3.metric("Trade Support", "All Formal & Informal")
    m_col4.metric("AI Core", "Gemini + Gemma 2")
    
    st.markdown("---")
    
    st.markdown("""
    ### Technical Workflow Pipeline
    1. **Skill Input:** Candidates submit scenario answers or audio clips via mobile rails.
    2. **Gemma 2 Anonymization:** Local/edge model strips PII, dialect, gender, and family name to prevent bias.
    3. **Gemini Skill Audit:** Gemini evaluates structural domain competency and produces an objective skill vector.
    4. **Active Bridge:** Verified vector profiles are instantly indexed and pushed to matching enterprise or private employers.
    """)