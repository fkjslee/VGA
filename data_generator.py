import jieba

with open("read.txt", encoding="utf-8") as f:
    content = f.readlines()
    for line in content:
        line = line.strip()
        words = jieba.lcut(line)
        print("-")
        print("  sentence: 添加 句子 {}".format(" ".join(words)))
        print("  intent: modify")
        print("  slot: ")
        print("    - O")
        print("    - O")
        if len(words) == 1:
            print("    - S-sentence")
        else:
            print("    - B-sentence")
            for _ in range(len(words) - 2):
                print("    - M-sentence")
            print("    - E-sentence")
        print()
