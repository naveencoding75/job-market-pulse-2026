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
    print(f"Starting Scraper for {JOB_ROLE} in {LOCATION}...")
    
    # 1. Setup Chrome Browser
    # We use 'Headless = False' so you can see the browser open and work
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    # This automatically downloads the correct driver for your Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # 2. Build the URL
    # We are using TimesJobs because it's easy to scrape
    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={JOB_ROLE.replace(' ', '+')}&txtLocation={LOCATION}"
    driver.get(url)
    
    # 3. Wait for page to load
    time.sleep(5) 
    
    # 4. Extract Data
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    
    data = []
    print(f"Found {len(jobs)} jobs on Page 1. Extracting...")

    for job in jobs:
        try:
            # Extract specific details
            title = job.find('h2').text.strip()
            company = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            
            # Add to our list
            data.append({
                'Job Title': title,
                'Company': company,
                'Skills': skills
            })
        except Exception as e:
            continue # Skip any bad rows

    # 5. Save to CSV
    if len(data) > 0:
        df = pd.DataFrame(data)
        filename = "job_market_data.csv"
        df.to_csv(filename, index=False)
        print(f"Success! Saved {len(data)} jobs to '{filename}'")
    else:
        print("No jobs found. Check your internet or try again.")
    
    driver.quit()

if __name__ == "__main__":
    get_job_data()