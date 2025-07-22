import re

def strip_markdown(text):
    text = re.sub(r'\*\*(.*?)\*\*', lambda m: m.group(1).upper(), text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    return text
