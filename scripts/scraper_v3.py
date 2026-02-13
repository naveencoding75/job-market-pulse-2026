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
    print(f"🚀 Starting Scraper v3 (The Robust One)...")
    
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Keep commented to see browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={JOB_ROLE.replace(' ', '+')}&txtLocation={LOCATION}"
    driver.get(url)
    
    print("⏳ Waiting 15 seconds for page to fully render...")
    time.sleep(15) 
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # --- THE FIX: NUCLEAR SEARCH ---
    # Instead of looking for a specific class, we look for ALL list items
    # and check if they "look" like a job (contain an h2 title).
    all_list_items = soup.find_all('li')
    print(f"👀 Scanned {len(all_list_items)} list items on the page.")
    
    data = []
    
    for item in all_list_items:
        # Check if this list item has an H2 (Title) and H3 (Company)
        # This ignores navigation menus, footers, etc.
        title_tag = item.find('h2')
        company_tag = item.find('h3')
        
        if title_tag and company_tag:
            try:
                title = title_tag.text.strip()
                company = company_tag.text.strip()
                
                # Skills are usually in a span, but let's be safe
                skills_tag = item.find('span', class_='srp-skills')
                skills = skills_tag.text.strip() if skills_tag else "Check Link"
                
                link = title_tag.find('a')['href'] if title_tag.find('a') else "N/A"

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
        print(f"✅ SUCCESS! Found {len(data)} jobs.")
        print(f"📂 Saved to: {filename}")
    else:
        print("❌ Still 0 jobs.")
        print("DEBUG INFO:")
        print("1. Did the browser open and show a list of jobs?")
        print("2. If yes, the HTML structure is completely different than expected.")

if __name__ == "__main__":
    get_job_data()