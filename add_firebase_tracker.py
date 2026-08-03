import os
import glob

html_files = glob.glob('*.html')
tracker_script = '<script type="module" src="firebase_tracker.js"></script>'

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'firebase_tracker.js' not in content:
        # Try to insert before </body>
        if '</body>' in content:
            content = content.replace('</body>', f'    {tracker_script}\n</body>')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added to {file_path}")
            count += 1
        else:
            print(f"Warning: No </body> found in {file_path}")

print(f"Total files updated: {count}")
