import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

# --- CONFIGURATION ---
FILE_NAME = "remote_jobs_live.csv"
# We want to ignore these generic words to find REAL tech skills
IGNORE_WORDS = ['remote', 'senior', 'engineer', 'developer', 'full time', 'hiring', 'mid', 'junior', 'manager', 'tech', 'engineering']
# ---------------------

def analyze_market():
    print(f"📊 Analyzing {FILE_NAME}...")
    
    try:
        df = pd.read_csv(FILE_NAME)
    except FileNotFoundError:
        print("❌ Error: CSV file not found. Run the scraper first!")
        return

    # 1. Extract all tags into a massive list
    all_tags = []
    
    for tags_string in df['Tags']:
        if isinstance(tags_string, str):
            # Split "python, react, sql" into ["python", "react", "sql"]
            tags = tags_string.split(',')
            
            # Clean up (remove spaces, make lowercase)
            for t in tags:
                clean_tag = t.strip().lower()
                # Only add if it's not a generic word
                if clean_tag not in IGNORE_WORDS and len(clean_tag) > 1:
                    all_tags.append(clean_tag)

    # 2. Count the skills
    tag_counts = Counter(all_tags)
    top_skills = tag_counts.most_common(10) # Top 10

    print("\n🏆 TOP 10 IN-DEMAND SKILLS (Live Data):")
    print("-" * 40)
    for skill, count in top_skills:
        print(f"{skill}: {count} jobs")
    print("-" * 40)

    # 3. Generate the "Jaw-Dropping" Chart
    # We use Seaborn because it looks way better than default Matplotlib
    plt.figure(figsize=(12, 6))
    
    # Create data for plotting
    skills = [x[0].upper() for x in top_skills]
    counts = [x[1] for x in top_skills]
    
    sns.barplot(x=skills, y=counts, palette='viridis')
    
    plt.title('The "Job Market Pulse": Top 10 Skills in Demand (Feb 2026)', fontsize=16, fontweight='bold')
    plt.ylabel('Number of Job Postings', fontsize=12)
    plt.xlabel('Technology', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save the chart
    chart_filename = "market_pulse_chart.png"
    plt.savefig(chart_filename, bbox_inches='tight', dpi=300)
    print(f"\n🖼️ Chart saved as '{chart_filename}'")
    print("👉 Open this image! This is your submission for the 'Visuals' prize.")
    
    plt.show()

if __name__ == "__main__":
    analyze_market()