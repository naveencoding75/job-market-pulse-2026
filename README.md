# 🛡️ Job Market Pulse 2026: The Security Surge

An automated, full-stack data pipeline and interactive dashboard that analyzes live remote job market trends.

## 🔗 Links
- **Live Demo:** [https://job-market-pulse-2026.vercel.app/](https://job-market-pulse-2026.vercel.app/)
- **Insight Report:** #1 Trend - Security & Go are outperforming standard Frontend frameworks.

## 📊 The Project
This project explores a key question for CS students: *Is the MERN stack still the king of remote work in 2026?* **I developed this automated pipeline to track how the demand for Security and Go is shifting in the 2026 remote landscape.** By analyzing live data rather than static datasets, I discovered a significant shift toward infrastructure and security over simple feature building.

<p align="center">
  <img src="dashboard-1.png" width="48%" />
  <img src="dashboard-2.png" width="48%" />
</p>

## ⚙️ How It Works (The Pipeline)

This project is a **Full-Stack Data Engineering** pipeline:

1. **Data Collection (Python):** A script in `scripts/api_scraper.py` fetches live records from the RemoteOK API.
2. **Automation (GitHub Actions):** A CI/CD workflow runs the scraper every 24 hours at midnight.
3. **Data Storage:** The cleaned data is committed back to the repository as `public/remote_jobs_live.csv`.
4. **The Dashboard (Next.js):** A modern React-based frontend (Tailwind CSS + Recharts) automatically pulls the new CSV and re-renders the insights.

## 🛠️ Tech Stack
- **Languages:** Python (Data Processing), JavaScript (Frontend/API)
- **Libraries:** Pandas, Requests, React, Recharts, PapaParse
- **Tools:** GitHub Actions (Automation), Vercel (Deployment)

## 🚀 Key Insights
- **Security** is the #1 in-demand skill in the analyzed remote sector.
- **Go (Golang)** shows higher growth potential than standard Node.js/Express for high-performance roles.

## 🗺️ Future Roadmap
As a Data Science student, I plan to evolve this project into a more robust market aggregator:
* **Multi-Source Aggregation:** Integrating JSearch and LinkedIn APIs.
* **NLP Classification:** Using Natural Language Processing to categorize job roles based on descriptions.
* **Historical Tracking:** Migrating to a relational database (MySQL) to store daily snapshots and visualize trends.

---

## 👨‍💻 About the Developer
I am a **B.Tech Computer Science (Data Science)** student at **Kazi Nazrul University**. I am passionate about bridging the gap between data engineering and full-stack web development. This project serves as a showcase of my ability to build end-to-end automated systems and derive actionable insights from live data.

**Seeking Internships in:** Data Science | Web Development | Data Engineering
