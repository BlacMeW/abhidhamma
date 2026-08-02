import os
import re

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all occurrences of the SEO block
    # It starts with <!-- SEO & Open Graph Meta Tags --> and ends with </script>\n</head>
    # Since my injection adds </head> at the end, let's just find all blocks starting with <!-- SEO ...
    
    parts = html.split('<!-- SEO & Open Graph Meta Tags -->')
    if len(parts) > 2:
        print(f"Fixing duplicates in {filepath}")
        # There's more than one block!
        # The true HTML before the first block is parts[0]
        # The last part contains the rest of the HTML after the last block
        # Actually, let's just use regex to remove ALL blocks completely and re-insert ONCE.
        
        # Remove anything from <!-- SEO & Open Graph Meta Tags --> up to </head> (non-greedy)
        # But wait, if there are multiple blocks, they might be stacked:
        # <!-- SEO ... --> ... </script>
        # <!-- SEO ... --> ... </script>
        # </head>
        
        # Let's remove ALL <!-- SEO ... --> and everything up to the next </script> or just remove the blocks.
        pass

    # A better approach: remove everything between the first <!-- SEO & Open Graph Meta Tags --> and the LAST </head> tag,
    # wait, no, just remove all blocks.
    
    # regex to match: <!-- SEO & Open Graph Meta Tags -->  to </script> (and maybe whitespace)
    cleaned = re.sub(r'<!-- SEO & Open Graph Meta Tags -->.*?</script>\s*', '', html, flags=re.IGNORECASE | re.DOTALL)
    
    # Now we need to inject the block again properly.
    # I'll just use the logic from update_seo_tags_v2.py to regenerate it.
    return cleaned

def fix_all():
    pass
