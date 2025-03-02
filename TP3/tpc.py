import re

def convert_inline(text):
    # Imagem
    text = re.sub(r'\!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', text)
    # Link
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    # Negrito
    text = re.sub(r'\*\*([^\*]+)\*\*', r'<b>\1</b>', text)
    # Itálico
    text = re.sub(r'\*([^\*]+)\*', r'<i>\1</i>', text)
    return text

def convert_markdown_to_html(markdown_text):
    html_lines = []
    lines = markdown_text.splitlines()
    in_list = False

    for line in lines:
        header_match = re.match(r'^(#{1,3})\s+(.*)$', line)
        if header_match:
            header_level = len(header_match.group(1))
            content = convert_inline(header_match.group(2))
            html_lines.append(f'<h{header_level}>{content}</h{header_level}>')
            continue
        
        list_match = re.match(r'^\s*\d+\.\s+(.*)$', line)
        if list_match:
            if not in_list:
                in_list = True
                html_lines.append('<ol>')
            content = convert_inline(list_match.group(1))
            html_lines.append(f'  <li>{content}</li>')
            continue
        else:
            if in_list:
                html_lines.append('</ol>')
                in_list = False

        if line.strip():
            content = convert_inline(line)
            html_lines.append(f'<p>{content}</p>')
        else:
            html_lines.append('')
    
    if in_list:
        html_lines.append('</ol>')
    
    return "\n".join(html_lines)

def main():
    input_filename = 'input.md'
    output_filename = 'output.html'
    
    with open(input_filename, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    
    html_text = convert_markdown_to_html(markdown_text)
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_text)
    

if __name__ == '__main__':
    main()
