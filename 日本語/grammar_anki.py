def get_data(start, end, lines):
    d = []
    f = False
    for line in lines[start:end]:
        line = line.replace('- ', '')
        if '：' in line:
            h, c = line.split('：')
            if c.strip() != '':
                d.append([h, [c.strip()]])
            else:
                f = True
                d.append([h, []])
        elif f == True:
            d[-1][1].append(line.strip())
    return d

def to_html(string: str):
    return "".join ( [["</strong>","<strong>",""][i&1 if i else 2]+l for i, l in enumerate(string.split('**'))] )

with open("2_2_文法出題基準外項目.md", "r") as f:
    lines = list(f)

headers = [(i,h[3:].strip()) for i,h in enumerate(lines) if h.startswith('##')]
l = len(headers)

with open("extra_grammar_anki.txt","w") as o:
    print("#separator:pipe\n#html:true\n#deck:JLPT N1 文法\n#notetype:Grammar Point", file=o)
    for j in range(l):
        s = headers[j][0]
        if (j < l-1):
            e = headers[j+1][0]
        else:
            e = -1
        h = headers[j][1]
        f, m, e = [to_html( "<div>"+('</div><div>'.join(a[1]))+"</div>" ) for a in get_data(s, e, lines)[:3]]
        print('|'.join((h,f,m,e)), file=o)