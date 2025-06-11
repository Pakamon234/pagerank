# Personalized PageRank mapper
import sys

d = 0.85  # hệ số nhảy
source = "A"  # ID node nguồn (sẽ được chỉnh sửa tùy theo dữ liệu)

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) == 3:
        node, rank, outlinks = parts
        outlinks_list = outlinks.split(',') if outlinks else []

        # Phân phối rank cho các nút liên kết
        if outlinks_list:
            contribution = float(rank) / len(outlinks_list)
            for neighbor in outlinks_list:
                print(f"{neighbor}\t{contribution}")

        # Giữ lại danh sách outlinks
        print(f"{node}\tLINKS:{outlinks}")
    elif len(parts) == 2 and parts[0] == source:
        # Trường hợp node nguồn: thêm teleport
        print(f"{source}\tTELEPORT")