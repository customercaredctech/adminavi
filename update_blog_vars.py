import os

files_to_update = ['blog.html', 'blog-sds-visa.html', 'blog-canada-permit.html']

for file in files_to_update:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = {
        'var(--primary)': 'var(--c-navy)',
        'var(--primary-light)': 'var(--c-navy-dark)',
        'var(--secondary)': '#F4F7F6',
        'var(--accent)': 'var(--c-gold)',
        'var(--accent-hover)': '#B8962E',
        'var(--text-dark)': 'var(--c-navy)',
        'var(--text-body)': 'var(--c-text-light)',
        'var(--text-muted)': 'var(--c-text-light)',
        'var(--bg-page)': '#F4F7F6',
        'var(--radius-lg)': 'var(--rad-lg)',
        'var(--radius-md)': 'var(--rad-md)',
        'Outfit': 'Poppins',
        'Inter': 'Inter'
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file} vars")
