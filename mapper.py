import sys

d = 0.85
source = "A"

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) == 3:
        node, rank, outlinks = parts
        outlinks_list = outlinks.split(',') if outlinks else []

        if outlinks_list:
            contribution = float(rank) / len(outlinks_list)
            for neighbor in outlinks_list:
                print(f"{neighbor}\t{contribution}")

        print(f"{node}\tLINKS:{outlinks}")
    elif len(parts) == 2 and parts[0] == source:
        print(f"{source}\tTELEPORT")