from pandas import read_excel
e = read_excel("1_語彙.xlsx", header=None, engine="calamine").values.tolist()
with open("anki_vocab.txt", "w") as o, open("1_語彙.md", "w") as p:
    print("#separator:pipe\n#html:false\n#deck:JLPT N1 語彙\n#notetype:Two Backs", file=o)
    print("|日|ひ|英|\n|---|---|---|", file=p)
    [print('|'.join(v), file=o) for v in e]
    [print('|'+'|'.join(v)+'|', file=p) for v in e]
