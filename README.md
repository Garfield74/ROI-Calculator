# CFOHub.ai AI ROI Calculator for Finance

## Description
This is a Streamlit web application designed for finance professionals to calculate the Return on Investment (ROI) for adopting AI technologies in their departments. It provides a user-friendly interface to input costs, estimate benefits, and analyze different scenarios to make informed decisions about AI investments.

## Features
- **Preset Use Cases:** Quickly load typical costs and benefits for common finance AI applications like Accounts Payable Automation, Forecasting, and Reconciliation.
- **Customizable Inputs:** Flexibility to enter your own data for a bespoke ROI calculation.
- **Scenario Analysis:** Compare worst-case, base-case, and best-case scenarios to understand the potential range of outcomes.
- **Visualizations:** A bar chart to visually compare costs and benefits.
- **PDF Reports:** Generate and download a "CFO-ready" PDF summary of the ROI analysis.
- **Branded UI:** A clean and professional user interface with CFOHub.ai branding.

## How to Run
This project is configured to run in a Dev Container, for example, using GitHub Codespaces.

1.  **Open in a Dev Container:** Open this repository in a Dev Container environment like GitHub Codespaces. The container will be automatically built with all the necessary dependencies.
2.  **Application Autostart:** The Streamlit application is configured to start automatically once the container is up and running.
3.  **Access the Application:** The application will be available on port `8501`. If you are using Codespaces, the port will be forwarded automatically, and you can open the application in a new browser tab.

If you want to run the application locally without a Dev Container:
1. **Install dependencies:**
   ```bash
   pip install streamlit matplotlib fpdf
   ```
2. **Run the app:**
   ```bash
   streamlit run roi_calculator.py
   ```

## Use Cases
The application includes presets for the following use cases:
- Accounts Payable Automation
- Forecasting AI
- Reconciliation AI

You can also use the "Custom Inputs" option to model any other AI-related financial use case.

## Dependencies
- `streamlit`
- `matplotlib`
- `fpdf`

These dependencies are automatically installed when using the provided Dev Container configuration.
