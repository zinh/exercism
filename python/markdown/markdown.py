import re

def parse_markdown(markdown):
    lines = markdown.split('\n')
    res = []
    state = None
    for line in lines:
        tag, text = parse_line(line)
        if tag == 'list' and state != 'list':
            state = 'list'
            text = '<ul>' + text
        if tag != 'list' and state == 'list':
            state = None
            text = '</ul>' + text 
        res.append(text)
    if state == 'list':
        res.append('</ul>')
    return ''.join(res)

def parse_line(line):
    header = re.match(r'^(#{1,6}) (.*)', line)
    paragraph = True
    if header is not None:
        count = len(header.group(1))
        text = header.group(2)
        return ('header', f'<h{count}>{text}</h{count}>')
    for bold in re.finditer(r'__([^_])+__', line):
        text = bold.group()[2:-2]
        line = line.replace(bold.group(), f'<strong>{text}</strong>')
    for italic in re.finditer(r'_([^_]+)_', line):
        text = italic.group()[1:-1]
        line = line.replace(italic.group(), f'<em>{text}</em>')
    for li in re.finditer(r'^\* (.+)', line):
        paragraph = False
        text = li.group()[2:]
        line = line.replace(li.group(), f'<li>{text}</li>')
    if paragraph:
        return ('paragraph', f'<p>{line}</p>')
    else:
        return ('list', line)
