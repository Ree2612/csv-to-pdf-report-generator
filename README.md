# csv-to-pdf-report-generator
# A Streamlit app to convert CSV/Excel files into clean PDF reports with optional charts. 
# 📊 CSV/Excel to PDF Report Generator

A Streamlit-based Python app that:
- Uploads `.csv` or `.xlsx` files
- Lets the user select specific columns
- Optionally includes a bar chart (mean of numeric columns)
- Exports the data into a clean, formatted PDF report

🔗 Live Demo
Try the app here:  
[https://csv-to-pdf-report-generator-hrktrq2muf3muxqbqxnz2t.streamlit.app](https://csv-to-pdf-report-generator-hrktrq2muf3muxqbqxnz2t.streamlit.app)


## 🔧 Features
- Responsive UI
- Styled PDF export using `fpdf`
- Optional visualization with `matplotlib`

## 📦 Requirements

Install all dependencies:
```bash
pip install -r requirements.txt
```

##📝 Output
PDF will be generated as final_report.pdf
You can download it using the built-in Streamlit button

🚀 Run the App Locally
```bash
streamlit run app.py
```
Dashboard screenshots
![Screenshot (154)](https://github.com/user-attachments/assets/5f621150-8a0e-4dc4-991e-3ea35847279a)

After uploading csv file
![Screenshot (155)](https://github.com/user-attachments/assets/c992545a-e6b6-4a9a-890a-566409374df2)

The generated pdf:
[report (4).pdf](https://github.com/user-attachments/files/20761588/report.4.pdf)


