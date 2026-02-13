# 🛡️ Job Market Pulse 2026: The Security Surge

An automated, full-stack data pipeline and interactive dashboard that analyzes live remote job market trends.

## 🔗 Links
- **Live Demo:** (https://job-market-pulse-2026.vercel.app/)
- **Insight Report:** #1 Trend - Security & Go are outperforming standard Frontend frameworks.

## 📊 The Project
This project explores a key question for CS students: *Is the MERN stack still the king of remote work in 2026?* By analyzing live data, I discovered a significant shift toward infrastructure and security over simple feature building.

![Dashboard Preview](dashboard-preview.png)

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
