#!/usr/bin/env python3
"""
Complete Sitemap Generator for geometry-dash-unbanned.github.io
Generates a comprehensive XML sitemap with all 429+ game pages
"""

import os
import glob
from datetime import datetime

def generate_complete_sitemap():
    base_url = "https://geometry-dash-unbanned.github.io"
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Start building the sitemap
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'''
    
    # Main pages
    main_pages = [
        ("/", "1.0", "daily"),
        ("/policy.html", "0.3", "monthly"),
        ("/term.html", "0.3", "monthly"),
        ("/dmca.html", "0.3", "monthly"),
        ("/sitemap.html", "0.5", "monthly")
    ]
    
    for url, priority, changefreq in main_pages:
        sitemap_content += f'''
  <url>
    <loc>{base_url}{url}</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>'''
    
    # Category pages
    categories = [
        "action", "adventure", "car", "fighting", "idle", "moto",
        "multiplayer", "new", "popular", "puzzle", "racing", "running",
        "shooting", "skill", "sports", "stickman", "threed", "twoplayer"
    ]
    
    for category in categories:
        sitemap_content += f'''
  <url>
    <loc>{base_url}/category/{category}.html</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>'''
    
    # Game pages - get all HTML files from play directory
    play_dir = "play"
    if os.path.exists(play_dir):
        game_files = glob.glob(os.path.join(play_dir, "*.html"))
        game_files.sort()  # Sort alphabetically
        
        for game_file in game_files:
            game_name = os.path.basename(game_file)
            game_url = f"/play/{game_name}"
            
            # Determine priority based on game popularity
            priority = "0.7"  # Default priority
            if "geometry-dash" in game_name.lower():
                priority = "0.9"
            elif any(popular in game_name.lower() for popular in [
                "8-ball-pool", "tunnel-rush", "slope", "retro-bowl", 
                "smash-karts", "temple-run-2", "moto-x3m", "football-legends"
            ]):
                priority = "0.8"
            
            sitemap_content += f'''
  <url>
    <loc>{base_url}{game_url}</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>'''
    
    # Close the sitemap
    sitemap_content += '''
</urlset>'''
    
    return sitemap_content

def main():
    print("Generating complete sitemap for geometry-dash-unbanned.github.io...")
    
    sitemap_content = generate_complete_sitemap()
    
    # Write to sitemap.xml
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    
    print(f"Sitemap generated successfully!")
    print(f"Total URLs: {sitemap_content.count('<url>')}")
    print(f"File saved as: sitemap.xml")

if __name__ == "__main__":
    main()
