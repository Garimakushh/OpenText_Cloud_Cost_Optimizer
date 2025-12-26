# ☁️ Cloud Cost Optimizer using LLMs

## 📌 Project Overview
The **Cloud Cost Optimizer** is an AI-powered system that analyzes cloud project requirements, generates synthetic cloud billing data, and provides intelligent cost optimization recommendations using **Large Language Models (LLMs)**.

This project demonstrates how **LLMs can be used for cloud cost estimation, optimization, and decision support**, making it suitable for enterprise cloud planning.

---

## 🎯 Aim
To build an **AI-driven cloud cost optimization system** that:
- Understands project requirements
- Simulates realistic cloud billing
- Analyzes costs against budget
- Recommends cost-saving strategies across **AWS, Azure, GCP, and open-source options**

---

## 🎯 Objectives
- Convert unstructured project descriptions into structured cloud profiles  
- Generate **synthetic, cloud-agnostic billing data**  
- Perform cost analysis against budget constraints  
- Generate **8–10 actionable, multi-cloud optimization recommendations**  
- Produce machine-readable reports (JSON) and exportable summaries  

---
## ✨ Features
- 🧠 LLM-powered understanding of project requirements  
- 💰 Synthetic cloud billing generation  
- 📊 Cost analysis & budget variance detection  
- ☁️ Multi-cloud recommendations (AWS, Azure, GCP, Open-source)  
- 🧾 Structured JSON outputs
- 🛡️ Robust handling of imperfect LLM outputs
- 🔍 Local & Google Colab execution support 

---

## 🧰 Tech Stack Used

| Category | Technology |
|--------|------------|
| Language | Python 3 |
| LLM | Meta-Llama-3-8B-Instruct |
| Framework | Hugging Face Transformers |
| Parsing | JSON, Regex |
| CLI Output | Rich |
| Runtime | Local / Google Colab |
| Version Control | Git & GitHub |

---

### Academic Integrity
 
- AI tools(ChatGpt -OpenAI) were used only for assistance and debugging.
- All code was implemented, tested, and validated.

---

## 🏗️ Project Architecture (Pipeline)

```text
User Input (Project Description)
        ↓
Profile Extractor (LLM)
        ↓
project_profile.json
        ↓
Billing Generator (LLM)
        ↓
mock_billing.json
        ↓
Cost Analyzer (LLM)
        ↓
cost_optimization_report.json
```
---

## 📂 File Structure

```text
Cloud_Cost_Optimizer/
│
├── main.py
├── llm_client.py
│
├── profile_extractor.py
├── billing_generator.py
├── cost_analyzer.py
├── report_exporter.py
│
├── project_description.txt
├── project_profile.json
├── mock_billing.json
├── cost_optimization_report.json
│
├── requirements.txt
└── README.md
```
---
## 🧠 Functional Modules (CLI Workflow)

The system follows a step-by-step interactive workflow:

### Get Google colab File here : [LINK](https://colab.research.google.com/drive/1SoIqtr71rPD2108e7yhNLsFpr2Gi53rv?usp=sharing)


---

### 1️⃣ Enter Project Description
- **Input**: Free-text project description entered by the user  
- **Output**: `project_profile.json`  
- Extracts:
  - Project name  
  - Monthly budget  
  - Tech stack  
  - Non-functional requirements  
![image](https://github.com/Garimakushh/OpenText_Cloud_Cost_Optimizer/blob/cfb871eaa3f54016231b7fbd7cb6bf4919079a4d/Screenshots/Option%201.png
)
---

### 2️⃣ Generate Synthetic Billing Data
- **Input**: `project_profile.json`  
- **Output**: `mock_billing.json`  
- Generates **12–20 realistic, cloud-agnostic billing records**  
- Budget-aware cost simulation across compute, database, storage, networking & monitoring  

---

### 3️⃣ Run Cost Analysis & Recommendations
- **Inputs**: `project_profile.json`, `mock_billing.json`  
- **Output**: `cost_optimization_report.json`  
- Calculates:
  - Total monthly cost  
  - Cost by service  
  - Budget variance  
  - Over-budget flag  
- Generates **8–10 multi-cloud optimization recommendations**
![image](https://github.com/Garimakushh/OpenText_Cloud_Cost_Optimizer/blob/cfb871eaa3f54016231b7fbd7cb6bf4919079a4d/Screenshots/Option%202%20%26%203.png
)
---

### 4️⃣ View Cost Optimization Report
- Displays the contents of `cost_optimization_report.json`.
- Allows quick inspection of total cost, service-wise spend & recommendations  

![image](https://github.com/Garimakushh/OpenText_Cloud_Cost_Optimizer/blob/cfb871eaa3f54016231b7fbd7cb6bf4919079a4d/Screenshots/Option%204.png)
---

### 5️⃣ Export HTML Report
- Converts `cost_optimization_report.json` into a user-friendly HTML file  
- Output file: `cost_report.html`  
- Can be shared with stakeholders  

---

### 6️⃣ Exit
- Safely exits the Cloud Cost Optimizer CLI application  

![image](https://github.com/Garimakushh/OpenText_Cloud_Cost_Optimizer/blob/cfb871eaa3f54016231b7fbd7cb6bf4919079a4d/Screenshots/Option%205%20%26%206.png)

---

## ▶️ How to Run on Google Colab

### Step 1: Open Google Colab
Go to: https://colab.research.google.com

### Step 2: Clone the Repository
```bash
git clone https://github.com/Garimakushh/OpenText_Cloud_Cost_Optimizer.git
```
### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Login to Hugging Face
```bash
from huggingface_hub import login
login()
```
### Step 5: Run the Application
```bash
python main.py
```
### Step 6: Use the Menu
Cloud Cost Optimizer
1. Enter project description
2. Generate synthetic billing data
3. Run cost analysis & recommendations
4. View cost optimization report
5. Export HTML report
6. Exit   
Choose: __

## 📄 Sample Output Files

- **project_profile.json** → Structured project requirements  
- **mock_billing.json** → Synthetic cloud billing data  
- **cost_optimization_report.json** → Cost analysis & optimization recommendations  


## 🛡️ Error Handling & Robustness

- Handles invalid or partial LLM responses gracefully  
- Safely extracts structured JSON using regex-based repair  
- Prevents crashes caused by malformed LLM output  
- Saves partial results whenever valid JSON blocks are found  
- Retries model calls automatically when empty or broken responses occur  

---

## 🚀 Future Enhancements

- Integration with real cloud billing APIs (AWS Cost Explorer, Azure Cost Management, GCP Billing)  
- Interactive dashboard-based visualization  
- Cost trend prediction using time-series ML models  
- FinOps policy automation  
- Multi-project comparison & portfolio analysis  

---

## 👨‍💻 Author

**Garima Kushwaha**  
Cloud & AI Enthusiast  
OpenText Pre-Boarding Project – FY26  

---

## 📜 License
This project is created for educational and evaluation purposes under OpenText pre-boarding guidelines.
 
---
<p align="center">
  Made with ❤️ by <a href="https://github.com/Garimakushh">Garima Kushwaha</a>
</p>

