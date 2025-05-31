"""
Social Media Search Linker

This script generates direct search URLs for a given term across various social media platforms.
It creates links for both user/profile searches and content/keyword searches (e.g., posts,
videos, tags) related to the provided search term.

Usage:
    python social_search_linker.py <search_term>

Replace <search_term> with the actual username, email, or keyword you want to search for.
The script will generate an HTML file named `search_links.html` in the same directory.
Open `search_links.html` in your web browser to access the clickable search links.

Note:
- This tool does not bypass any platform-specific privacy settings, login
  requirements, or search restrictions.
- Finding a user or specific content is not guaranteed; results depend on platform
  search capabilities and user/content visibility settings.
"""
import urllib.parse

def generate_search_urls(search_term):
    """
    Generates search URLs for various social media platforms.

    Args:
        search_term: The username or keyword to search for.

    Returns:
        A dictionary of platform names and their corresponding search URLs.
    """
    platforms = {
        # Profile/User Searches
        "Twitter Profile": "https://twitter.com/USERNAME",
        "Twitter User Search": "https://twitter.com/search?q=USERNAME&f=user", # Changed label for clarity
        "Instagram Profile": "https://www.instagram.com/USERNAME/",
        "Facebook User Search": "https://www.facebook.com/search/top/?q=USERNAME", # Changed label for clarity
        "TikTok Profile": "https://www.tiktok.com/@USERNAME",
        "TikTok User Search": "https://www.tiktok.com/search/user?q=USERNAME", # Changed label for clarity
        "Twitch Profile": "https://www.twitch.tv/USERNAME",
        "Twitch User Search": "https://www.twitch.tv/search?term=USERNAME", # Changed label for clarity
        # Content Searches
        "Twitter Content Search": "https://twitter.com/search?q=KEYWORD",
        "Instagram Tag Search": "https://www.instagram.com/explore/tags/TAGKEYWORD/",
        "Facebook Posts Search": "https://www.facebook.com/search/posts/?q=KEYWORD",
        "TikTok Video Search": "https://www.tiktok.com/search/video?q=KEYWORD",
        "Twitch Content Search": "https://www.twitch.tv/search?term=KEYWORD", # Re-using general search, labeled as content
    }

    generated_urls = {}
    encoded_search_term = urllib.parse.quote_plus(search_term)
    instagram_tag_term = search_term.lower().replace(" ", "")

    for platform, url_template in platforms.items():
        if "USERNAME" in url_template:
            generated_urls[platform] = url_template.replace("USERNAME", encoded_search_term)
        elif "TAGKEYWORD" in url_template:
            generated_urls[platform] = url_template.replace("TAGKEYWORD", instagram_tag_term)
        elif "KEYWORD" in url_template:
            generated_urls[platform] = url_template.replace("KEYWORD", encoded_search_term)
        else: # Should not happen with current platform list
            generated_urls[platform] = url_template


    return generated_urls

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Error: Please provide a search term as a command-line argument.")
        print("Usage: python social_search_linker.py <search_term>")
    else:
        user_input = sys.argv[1] # Original search term for display
        search_links = generate_search_urls(user_input)

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Social Media Search Links</title>
    <style>
        body {{ font-family: sans-serif; margin: 20px; background-color: #f4f4f4; color: #333; }}
        h1 {{ color: #0056b3; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ background-color: #fff; margin-bottom: 8px; padding: 12px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        a {{ text-decoration: none; color: #007bff; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>Generated Search Links for "{user_input}"</h1>
    <ul>
"""
        for platform, link in search_links.items():
            html_content += f'        <li><a href="{link}" target="_blank">{platform}: {link}</a></li>\n'

        html_content += """    </ul>
</body>
</html>
"""
        try:
            with open("search_links.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"\nSuccessfully generated `search_links.html` with your search links for \"{user_input}\".")
        except IOError as e:
            print(f"\nError writing to file: {e}")
