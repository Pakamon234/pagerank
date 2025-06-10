import sys
for line in sys.stdin:
    parts = line.strip().split('\t')
    node = parts[0]
    rank = float(parts[1])
    outlinks = parts[2].split(',') if len(parts) > 2 else []

    if outlinks:
        pr_share = rank / len(outlinks)
        for out in outlinks:
            print(f"{out}\t{pr_share}")

    print(f"{node}\tSTRUCT:{','.join(outlinks)}")
