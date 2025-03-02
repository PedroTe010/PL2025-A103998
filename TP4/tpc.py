import re

def get_token_patterns():
    patterns = [
        (r"select", "SELECT"),
        (r"where", "WHERE"),
        (r"\?[\w]+", "VARIABLE"),
        (r"[a-zA-Z_]\w*:", "CONNECTION"),
        (r"[a-zA-Z_]\w*", "COMPONENT"),
        (r"[{]", "START"),
        (r"[}]", "END"),
        (r"[.]", "END OF QUERY"),
        (r"@([a-zA-Z\-]+)", "LANGUAGE"),
        (r"\"[^\"]*\"", "STRING"),
        (r"\d+", "NUMBER"),
        (r"LIMIT \d+", "LIMIT"),
        (r"\s+", None), 
    ]
    return [(re.compile(pattern), token_type) for pattern, token_type in patterns]

def tokenize(query, token_patterns):
    tokens = []
    pos = 0

    while pos < len(query):
        for regex, token_type in token_patterns:
            match = regex.match(query, pos)
            if match:
                tokens.append((token_type, match.group()))
                pos = match.end()
                break
        else:
            raise SyntaxError(f"Erro inesperado: {query[pos]}")
    
    return tokens

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def print_tokens(tokens):
    for token_type, value in tokens:
        print(f"[{token_type}] -> {value}")

if __name__ == "__main__":
    token_patterns = get_token_patterns()
    query_text = read_file("query.txt")
    
    try:
        tokens = tokenize(query_text, token_patterns)
        print_tokens(tokens)
    except SyntaxError as e:
        print(e)
