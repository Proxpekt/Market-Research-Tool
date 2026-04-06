# 🚀 Market Research Multi-Agent System (CrewAI)

A powerful **multi-agent market research system** built using **CrewAI** that automates end-to-end business analysis including:

- 📊 Market Research
- 🧠 Competitive Intelligence
- 👥 Customer Insights
- 📈 Product Strategy
- 💼 Business Analysis

The system leverages **AI agents + real-time web data** to generate structured, data-driven reports.

---

## 🧠 Architecture

This project follows a **sequential multi-agent pipeline**:
Market Research Agent
↓
Competitive Intelligence Agent
↓
Customer Insights Agent
↓
Product Strategy Agent
↓
Business Analyst Agent (Final Report)


Each agent:
- Specializes in a specific domain
- Uses outputs from previous agents (context sharing)
- Contributes to the final report

---

## ⚙️ Features

- 🤖 Multi-agent collaboration using CrewAI
- 🌐 Real-time web data using:
  - Serper (Google Search API)
  - Website scraping
  - Selenium-based scraping
- 🔗 Context-aware task chaining
- 📄 Automated report generation (`reports/report.md`)
- 🧩 Modular and extensible architecture

---

## 🛠️ Tech Stack

- **CrewAI** – Multi-agent orchestration
- **Python** – Core programming
- **SerperDevTool** – Web search
- **ScrapeWebsiteTool** – Web scraping
- **SeleniumScrapingTool** – Advanced scraping
- **dotenv** – Environment management

---

## 🔑 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/market-research-crew.git
cd market-research-crew
```

2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

3. Install dependencies
```bash
uv sync
```

4. Setup environment variables

Create a .env file:
```bash
MODEL=your_model_name
GOOGLE_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

5. Run the project
```bash
crewai run
```
---

## 📄 Output

The final report is generated at:

```bash
reports/report.md
```

### Includes:

- Market size (TAM, SAM, SOM)
- Industry trends
- Competitive analysis
- Customer insights
- Strategic recommendations

---

## 🚀 Use Case

This system can be used for:

- Startup idea validation
- Market analysis for new products
- Competitive intelligence
- Business strategy planning
- AI-powered consulting tools

---

## 🔥 Future Improvements
- Multi-crew orchestration
- Memory & long-term context
- API deployment (FastAPI / Streamlit)
- Dashboard visualization
- Cost optimization & caching

---
  
## 🧠 Key Learning

This project demonstrates:
- Multi-agent system design
- Task orchestration using CrewAI
