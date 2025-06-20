import streamlit as st
import pandas as pd
from fpdf2 import FPDF
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="CSV to PDF Report Generator", layout="wide")

st.title("📊 CSV/Excel to PDF Report Generator")

uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1]
    if file_ext == "csv":
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Step 1: Preview Your Data")
    st.dataframe(df.head())

    st.subheader("Step 2: Select Columns to Include in the Report")
    selected_cols = st.multiselect("Choose columns:", df.columns.tolist(), default=df.columns.tolist()[:6])

    st.subheader("Step 3: (Optional) Add Chart to PDF")
    include_chart = st.checkbox("Include a chart of mean values (numeric columns only)", value=False)

    if st.button("📄 Generate PDF Report"):
        df_selected = df[selected_cols]

        chart_path = None
        if include_chart:
            numeric_cols = df_selected.select_dtypes(include='number').columns
            if not numeric_cols.empty:
                plt.figure(figsize=(10, 5))
                df_selected[numeric_cols].mean().sort_values().plot(kind='barh', color='skyblue')
                plt.title("Mean of Numeric Columns")
                plt.xlabel("Value")
                plt.tight_layout()
                chart_path = "chart.png"
                plt.savefig(chart_path)
                plt.close()

        class PDF(FPDF):
            def header(self):
                self.set_font("Arial", "B", 14)
                self.cell(0, 10, f"Auto Report: {uploaded_file.name}", ln=True, align="C")
                self.ln(5)

            def footer(self):
                self.set_y(-15)
                self.set_font("Arial", "I", 8)
                self.cell(0, 10, f"Page {self.page_no()}", align="C")

            def table(self, data):
                self.set_font("Arial", "B", 10)
                col_count = len(data.columns)
                page_width = self.w - 20
                col_width = max(25, page_width / col_count)

                for col in data.columns:
                    self.cell(col_width, 10, str(col)[:15], border=1, align='C')
                self.ln()

                self.set_font("Arial", "", 9)
                for i in range(len(data)):

                    for col in data.columns:
                        cell_text = str(data.iloc[i][col])
                        if len(cell_text) > 25:
                            cell_text = cell_text[:22] + "..."
                        self.cell(col_width, 10, cell_text, border=1)
                    self.ln()

            def chart(self, image_path):
                self.ln(5)
                self.image(image_path, x=20, w=250)
                self.ln(5)

        pdf = PDF(orientation='L')
        pdf.add_page()
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Sample Data Table", ln=True)
        pdf.table(df_selected)

        if include_chart and chart_path:
            pdf.add_page()
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, "Chart: Mean of Numeric Columns", ln=True)
            pdf.chart(chart_path)

        output_path = "final_report.pdf"
        pdf.output(output_path)

        with open(output_path, "rb") as f:
            st.success("✅ PDF Report Generated!")
            st.download_button("📥 Download PDF", f, file_name="report.pdf", mime="application/pdf")
