import os
import re

files = ["index.html", "services.html", "tools.html", "releases.html", "about.html", "contact.html"]

os.makedirs("fr", exist_ok=True)
os.makedirs("ln", exist_ok=True)

for f in files:
    # Read root file
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # 1. Generate Lingala version (English content with adjusted paths)
    ln_content = content
    # Replace stylesheet link
    ln_content = ln_content.replace('href="styles.css"', 'href="../styles.css"')
    # Replace profile image
    ln_content = ln_content.replace('src="profile.jpg"', 'src="../profile.jpg"')
    
    # Replace language switcher
    # Target:
    # <a href="FILENAME" class="lang-link active">EN</a>
    # <a href="fr/FILENAME" class="lang-link">FR</a>
    # <a href="ln/FILENAME" class="lang-link">LN</a>
    
    # Replace active EN with link to parent
    ln_content = ln_content.replace(f'href="{f}" class="lang-link active">EN</a>', f'href="../{f}" class="lang-link">EN</a>')
    # Replace FR link with sibling path
    ln_content = ln_content.replace(f'href="fr/{f}" class="lang-link">FR</a>', f'href="../fr/{f}" class="lang-link">FR</a>')
    # Replace LN link with local active link
    ln_content = ln_content.replace(f'href="ln/{f}" class="lang-link">LN</a>', f'href="{f}" class="lang-link active">LN</a>')
    
    with open(os.path.join("ln", f), "w", encoding="utf-8") as file:
        file.write(ln_content)
        
    # 2. Generate French template version (to be translated)
    fr_content = content
    fr_content = fr_content.replace('href="styles.css"', 'href="../styles.css"')
    fr_content = fr_content.replace('src="profile.jpg"', 'src="../profile.jpg"')
    
    # Replace active EN with link to parent
    fr_content = fr_content.replace(f'href="{f}" class="lang-link active">EN</a>', f'href="../{f}" class="lang-link">EN</a>')
    # Replace FR link with local active link
    fr_content = fr_content.replace(f'href="fr/{f}" class="lang-link">FR</a>', f'href="{f}" class="lang-link active">FR</a>')
    # Replace LN link with sibling path
    fr_content = fr_content.replace(f'href="ln/{f}" class="lang-link">LN</a>', f'href="../ln/{f}" class="lang-link">LN</a>')
    
    with open(os.path.join("fr", f), "w", encoding="utf-8") as file:
        file.write(fr_content)

print("Path adjustments complete for fr/ and ln/ files.")
