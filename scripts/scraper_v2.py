import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
JOB_ROLE = "Data Science"
LOCATION = "India"
# ---------------------

def get_job_data():
    print(f"🚀 Starting Scraper for {JOB_ROLE} in {LOCATION}...")
    
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Keep this commented to see the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={JOB_ROLE.replace(' ', '+')}&txtLocation={LOCATION}"
    driver.get(url)
    
    # Wait longer for the page to fully load
    print("⏳ Waiting 10 seconds for page to load...")
    time.sleep(10) 
    
    # Check if page loaded
    print(f"📄 Current Page Title: {driver.title}")
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # BROADER SEARCH: specific class 'job-bx' instead of the full string
    jobs = soup.find_all('li', class_='job-bx')
    
    # Fallback if that fails: Try CSS selector
    if not jobs:
        print("⚠️ Standard search failed. Trying CSS selector...")
        jobs = soup.select('.job-bx')

    print(f"🔍 Found {len(jobs)} jobs. Extracting...")

    data = []
    for job in jobs:
        try:
            # We use 'getattr' to avoid crashing if an element is missing
            title_tag = job.find('h2')
            company_tag = job.find('h3', class_='joblist-comp-name')
            skills_tag = job.find('span', class_='srp-skills')

            title = title_tag.text.strip() if title_tag else "N/A"
            company = company_tag.text.strip() if company_tag else "N/A"
            skills = skills_tag.text.strip() if skills_tag else "N/A"
            
            # Get the link to the full job too
            link = title_tag.find('a')['href'] if title_tag and title_tag.find('a') else "N/A"

            data.append({
                'Job Title': title,
                'Company': company,
                'Skills': skills,
                'Link': link
            })
        except Exception as e:
            continue

    driver.quit()

    if len(data) > 0:
        df = pd.DataFrame(data)
        filename = "job_market_data.csv"
        df.to_csv(filename, index=False)
        print(f"✅ Success! Saved {len(data)} jobs to '{filename}'")
    else:
        print("❌ Still 0 jobs. The site might be blocking us or the page structure changed completely.")

if __name__ == "__main__":
    get_job_data()