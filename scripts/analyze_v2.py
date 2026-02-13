import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

# --- CONFIGURATION ---
FILE_NAME = "remote_jobs_live.csv"

# WE ONLY WANT THESE SPECIFIC TECH SKILLS
# This is a "Whitelist" approach - much more accurate for Data Science projects
TECH_STACK = {
    'python', 'react', 'node', 'javascript', 'typescript', 'sql', 'aws', 'docker', 
    'kubernetes', 'java', 'c++', 'c#', 'go', 'rust', 'php', 'ruby', 'rails', 
    'swift', 'kotlin', 'flutter', 'dart', 'html', 'css', 'tailwind', 'bootstrap',
    'mongodb', 'postgresql', 'mysql', 'redis', 'graphql', 'rest api', 'linux',
    'git', 'github', 'jenkins', 'terraform', 'azure', 'gcp', 'openai', 'llm',
    'machine learning', 'data science', 'pandas', 'numpy', 'pytorch', 'tensorflow',
    'excel', 'tableau', 'power bi', 'figma', 'jira', 'scrum', 'agile', 'saas',
    'devops', 'sysadmin', 'security', 'blockchain', 'web3', 'solidity', 'next.js',
    'vue', 'angular', 'svelte', 'django', 'flask', 'fastapi', 'spring', 'laravel'
}
# ---------------------

def analyze_market_v2():
    print(f"📊 Running 'Pro' Analysis on {FILE_NAME}...")
    
    try:
        df = pd.read_csv(FILE_NAME)
    except FileNotFoundError:
        print("❌ Error: CSV file not found.")
        return

    real_skills = []
    
    for tags_string in df['Tags']:
        if isinstance(tags_string, str):
            tags = tags_string.split(',')
            for t in tags:
                clean_tag = t.strip().lower()
                # CHECK: Is this actually a tech skill?
                if clean_tag in TECH_STACK:
                    real_skills.append(clean_tag)
                # Special case: Map 'js' to 'javascript'
                elif clean_tag == 'js':
                    real_skills.append('javascript')
                # Special case: Map 'node.js' to 'node'
                elif 'node' in clean_tag:
                    real_skills.append('node')

    # Count and get Top 10
    skill_counts = Counter(real_skills)
    top_skills = skill_counts.most_common(10)

    print("\n🏆 TOP 10 HARD TECH SKILLS (Filtered):")
    print("-" * 40)
    for skill, count in top_skills:
        print(f"{skill.upper()}: {count} jobs")
    print("-" * 40)

    # Generate Chart
    plt.figure(figsize=(12, 6))
    
    skills = [x[0].upper() for x in top_skills]
    counts = [x[1] for x in top_skills]
    
    # FIXED: Added 'hue' and 'legend=False' to fix your warning
    sns.barplot(x=skills, y=counts, hue=skills, palette='magma', legend=False)
    
    plt.title('The Real Job Market Pulse: Top 10 Tech Stacks (Feb 2026)', fontsize=16, fontweight='bold')
    plt.ylabel('Active Job Postings', fontsize=12)
    plt.xlabel('Tech Stack', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    
    chart_filename = "market_pulse_chart_v2.png"
    plt.savefig(chart_filename, bbox_inches='tight', dpi=300)
    print(f"\n🖼️ Chart saved as '{chart_filename}'")
    
    plt.show()

if __name__ == "__main__":
    analyze_market_v2()