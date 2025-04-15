with open("1_2_漢字.md", "r") as f:
    vocab = [line for line in f if line.strip() != ""][2:]
with open("anki_kanji.txt", "w") as o:
    print("#separator:pipe\n#html:false\n#deck:JLPT N1 漢字\n#notetype:Ikoma Kanji", file=o)
    for w in vocab:
        b = [a.strip() for a in w.split("|")[1:-1]]
        b[3] = b[3].replace(b[0], "{{c1::"+b[0]+"}}")
        print('|'.join(b), file=o)
