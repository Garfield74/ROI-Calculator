# ai_roi_calculator_final.py

import streamlit as st
import matplotlib.pyplot as plt
from fpdf import FPDF
import io

# --- Branding ---
PRIMARY_COLOR = "#1A535C"       # CFOHub.ai Dark Teal
SECONDARY_COLOR = "#4ECDC4"     # Light Teal
ACCENT_COLOR = "#FF6B6B"        # Red for cost
FONT = "Arial"

st.set_page_config(page_title="CFOHub.ai - AI ROI Calculator", page_icon="💹", layout="wide")
st.markdown(f"<h1 style='color:{PRIMARY_COLOR};'>💹 CFOHub.ai AI ROI Calculator for Finance</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- Top 5 AI Finance Use Cases ---
st.header("📊 Top 5 AI Finance Use Cases - ROI Benchmarks")
st.markdown("""
| Use Case | Typical ROI Range | Key Benefits |
|----------|----------------|--------------|
| Accounts Payable Automation | 70% – 120% | Faster invoice processing, error reduction, staff redeployment |
| Forecasting AI | 80% – 150% | More accurate cash flow and revenue forecasting, strategic insights |
| Reconciliation AI | 60% – 110% | Automated bank/ledger reconciliation, fewer errors, faster close |
| Expense Management AI | 50% – 100% | Fraud detection, policy compliance, faster approvals |
| Financial Reporting AI | 65% – 130% | Automated report generation, improved accuracy, time savings |
""")
st.info("These ranges are typical in enterprises. Your results may vary based on company size, process complexity, and AI adoption level.")

# --- Finance Presets ---
st.header("0️⃣ Select Finance Use Case")
use_case = st.selectbox(
    "Choose a use case to pre-fill AI cost and benefit estimates:",
    ["Custom Inputs", "Accounts Payable Automation", "Forecasting AI", "Reconciliation AI"]
)

# Preset values dictionary
presets = {
    "Accounts Payable Automation": {
        "software_cost": 40000,
        "implementation_cost": 20000,
        "training_cost": 8000,
        "maintenance_cost": 4000,
        "other_costs": 2000,
        "time_saved_hours": 2.5,
        "tasks_automated": 1200,
        "hourly_cost": 45,
        "error_reduction": 10000,
        "revenue_uplift": 5000
    },
    "Forecasting AI": {
        "software_cost": 50000,
        "implementation_cost": 30000,
        "training_cost": 10000,
        "maintenance_cost": 5000,
        "other_costs": 0,
        "time_saved_hours": 3,
        "tasks_automated": 1000,
        "hourly_cost": 50,
        "error_reduction": 15000,
        "revenue_uplift": 20000
    },
    "Reconciliation AI": {
        "software_cost": 35000,
        "implementation_cost": 15000,
        "training_cost": 5000,
        "maintenance_cost": 3000,
        "other_costs": 1000,
        "time_saved_hours": 4,
        "tasks_automated": 800,
        "hourly_cost": 48,
        "error_reduction": 12000,
        "revenue_uplift": 8000
    }
}

# --- INPUTS: Use Presets or Custom ---
if use_case != "Custom Inputs":
    data = presets[use_case]
    software_cost = st.number_input("AI Software / Platform Cost ($)", value=data["software_cost"])
    implementation_cost = st.number_input("Implementation Cost ($)", value=data["implementation_cost"])
    training_cost = st.number_input("Training & Change Management Cost ($)", value=data["training_cost"])
    maintenance_cost = st.number_input("Maintenance & Support Cost ($)", value=data["maintenance_cost"])
    other_costs = st.number_input("Other Costs ($)", value=data["other_costs"])

    time_saved_hours = st.number_input("Time Saved per Task (hours)", value=data["time_saved_hours"])
    tasks_automated = st.number_input("Number of Tasks Automated (per year)", value=data["tasks_automated"])
    hourly_cost = st.number_input("Average Hourly Cost of Finance Staff ($)", value=data["hourly_cost"])
    error_reduction = st.number_input("Estimated Savings from Error Reduction ($)", value=data["error_reduction"])
    revenue_uplift = st.number_input("Revenue Uplift / Strategic Gains ($)", value=data["revenue_uplift"])
else:
    # Custom Inputs
    st.header("1️⃣ Enter Costs")
    software_cost = st.number_input("AI Software / Platform Cost ($)", min_value=0, value=50000)
    implementation_cost = st.number_input("Implementation Cost ($)", min_value=0, value=30000)
    training_cost = st.number_input("Training & Change Management Cost ($)", min_value=0, value=10000)
    maintenance_cost = st.number_input("Maintenance & Support Cost ($)", min_value=0, value=5000)
    other_costs = st.number_input("Other Costs ($)", min_value=0, value=0)

    st.header("2️⃣ Enter Benefits")
    time_saved_hours = st.number_input("Time Saved per Task (hours)", min_value=0.0, value=3.0)
    tasks_automated = st.number_input("Number of Tasks Automated (per year)", min_value=0, value=1000)
    hourly_cost = st.number_input("Average Hourly Cost of Finance Staff ($)", min_value=0.0, value=50.0)
    error_reduction = st.number_input("Estimated Savings from Error Reduction ($)", min_value=0.0, value=15000.0)
    revenue_uplift = st.number_input("Revenue Uplift / Strategic Gains ($)", min_value=0.0, value=20000.0)

# --- SCENARIO ANALYSIS ---
st.header("3️⃣ Scenario Analysis")
best_multiplier = st.slider("🌟 Best Case Multiplier", 1.0, 2.0, 1.2, 0.05)
worst_multiplier = st.slider("💼 Worst Case Multiplier", 0.5, 1.0, 0.8, 0.05)

def calculate_benefit(multiplier):
    return ((time_saved_hours * tasks_automated * hourly_cost) + error_reduction + revenue_uplift) * multiplier

benefit_base = calculate_benefit(1.0)
benefit_best = calculate_benefit(best_multiplier)
benefit_worst = calculate_benefit(worst_multiplier)

total_cost = software_cost + implementation_cost + training_cost + maintenance_cost + other_costs

def calculate_roi(benefit):
    return ((benefit - total_cost) / total_cost) * 100

roi_base = calculate_roi(benefit_base)
roi_best = calculate_roi(benefit_best)
roi_worst = calculate_roi(benefit_worst)

# --- RESULTS ---
st.header("4️⃣ Results")
col1, col2, col3 = st.columns(3)
col1.metric("Total Cost ($)", f"{total_cost:,.2f}", delta_color="inverse")
col2.metric("Base Case ROI (%)", f"{roi_base:.2f}%")
col3.metric("Payback Period (Years)", f"{total_cost / benefit_base:.2f}")

st.subheader("Scenario Summary")
st.info(f"💼 Worst Case Benefit: ${benefit_worst:,.2f} → ROI: {roi_worst:.2f}%")
st.success(f"🌟 Best Case Benefit: ${benefit_best:,.2f} → ROI: {roi_best:.2f}%")

# --- Visualization ---
st.header("5️⃣ Visualization")
fig, ax = plt.subplots(figsize=(7,5))
ax.bar(["Cost", "Worst Case", "Base Case", "Best Case"],
       [total_cost, benefit_worst, benefit_base, benefit_best],
       color=[ACCENT_COLOR, "#FFA500", SECONDARY_COLOR, PRIMARY_COLOR])
ax.set_ylabel("USD ($)")
ax.set_title("AI Investment vs Benefit (Scenario Analysis)", fontsize=14, color=PRIMARY_COLOR)
st.pyplot(fig)

# --- PDF REPORT ---
st.header("6️⃣ Download CFO-Ready PDF Report")
if st.button("📄 Generate PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font(FONT, 'B', 16)
    pdf.set_text_color(26, 83, 92)  # PRIMARY_COLOR RGB
    pdf.cell(0, 10, "CFOHub.ai AI ROI Calculator Report", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font(FONT, '', 12)
    pdf.set_text_color(0, 0, 0)
    
    pdf.cell(0, 8, f"Use Case: {use_case}", ln=True)
    pdf.cell(0, 8, f"Total Cost: ${total_cost:,.2f}", ln=True)
    pdf.cell(0, 8, f"Base Case Benefit: ${benefit_base:,.2f}", ln=True)
    pdf.cell(0, 8, f"Base Case ROI: {roi_base:.2f}%", ln=True)
    pdf.ln(5)
    pdf.cell(0, 8, f"Worst Case Benefit: ${benefit_worst:,.2f} → ROI: {roi_worst:.2f}%", ln=True)
    pdf.cell(0, 8, f"Best Case Benefit: ${benefit_best:,.2f} → ROI: {roi_best:.2f}%", ln=True)
    
    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)
    
    st.download_button("📥 Download PDF", pdf_buffer, "CFOHub_AI_ROI_Report.pdf", "application/pdf")

st.markdown("---")
st.markdown("<p style='color:gray;'>CFOHub.ai - Empowering Finance Leaders with AI Insights</p>", unsafe_allow_html=True)
