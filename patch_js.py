import os
import glob

# Javascript snippet to inject
js_snippet = """
  // Desktop dropdown interactive toggle
  const dropdownParent = document.querySelector('.nav-has-dropdown') || document.querySelector('.nav-dropdown');
  const dropdownToggle = document.querySelector('.nav-dropdown-toggle') || (dropdownParent ? dropdownParent.querySelector('a') : null);
  
  if (dropdownToggle && dropdownParent) {
    dropdownToggle.addEventListener('click', (e) => {
      e.preventDefault();
      dropdownParent.classList.toggle('is-active');
    });
    document.addEventListener('click', (e) => {
      if (!dropdownParent.contains(e.target)) {
        dropdownParent.classList.remove('is-active');
      }
    });
  }
"""

website_dir = r"c:\Users\mark\OneDrive\Grigg Share Drive\RENOVA UK\Website"
html_files = glob.glob(os.path.join(website_dir, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Avoid injecting multiple times
    if "Desktop dropdown interactive toggle" in content:
        continue
    
    # Find "</script>\n\n</body>" or "</script>\n</body>" or just "</script>"
    # Let's cleanly inject it before the last </script> tag
    idx = content.rfind("</script>")
    if idx != -1:
        new_content = content[:idx] + js_snippet + content[idx:]
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Patched {os.path.basename(file_path)}")
    else:
        print(f"Skipped {os.path.basename(file_path)} (no <script> found)")

