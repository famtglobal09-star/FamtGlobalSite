import glob, os, codecs

root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
pattern = os.path.join(root, 'templates', '**', '*.html')
files = glob.glob(pattern, recursive=True)
missing = []
for f in files:
    content = codecs.open(f, 'r', 'utf-8').read()
    if '{% static' in content and '{% load static' not in content:
        missing.append(os.path.relpath(f, root))

print('Templates using {% static %} without {% load static %}:')
for m in missing:
    print(' -', m)
