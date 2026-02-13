import requests
import pandas as pd
from datetime import datetime

def get_real_jobs():
    print("🚀 Fetching LIVE data from RemoteOK API...")
    
    # 1. The Magic Link (No scraping needed)
    url = "https://remoteok.com/api"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    response = requests.get(url, headers=headers)
    jobs = response.json()
    
    print(f"✅ API responded! Found {len(jobs)} total records.")
    
    # 2. Clean the Data
    data = []
    print("⚙️ Processing data...")
    
    for job in jobs:
        # The first item in their API is sometimes a "legal" text, skip it
        if "company" not in job: 
            continue
            
        # Extract fields
        try:
            title = job.get('position', 'N/A')
            company = job.get('company', 'N/A')
            tags = job.get('tags', []) # List of skills like ['python', 'react']
            location = job.get('location', 'Remote')
            date_posted = job.get('date', 'N/A')
            url = job.get('url', 'N/A')
            
            # Salary is often inside the description or tags in this API
            # But let's just save what we have first
            
            data.append({
                'Job Title': title,
                'Company': company,
                'Location': location,
                'Tags': ", ".join(tags), # Convert list to string "python, react"
                'Date': date_posted,
                'Apply Link': url
            })
        except Exception as e:
            continue

    # 3. Save to CSV
    df = pd.DataFrame(data)
    filename = "remote_jobs_live.csv"
    df.to_csv(filename, index=False)
    
    print(f"🎉 SUCCESS! Saved {len(data)} jobs to '{filename}'")
    print("👉 Open the file and check the 'Tags' column - that is your goldmine for analysis.")

if __name__ == "__main__":
    get_real_jobs()