import sys
from collections import defaultdict

d = 0.85
source = "A"

current_node = None
links = ""
total = 0.0
teleport = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split("\t")
    if len(parts) != 2:
        continue
    node, value = parts

    if current_node and node != current_node:
        # Tính PageRank mới
        new_rank = (1 - d) * (1.0 if current_node == source else 0.0) + d * total
        print(f"{current_node}\t{new_rank}\t{links}")
        total = 0.0
        links = ""

    current_node = node
    if value.startswith("LINKS:"):
        links = value[6:]
    elif value == "TELEPORT":
        pass  # giữ nguyên, xử lý bằng công thức
    else:
        try:
            total += float(value)
        except:
            pass

# Kết thúc node cuối cùng
if current_node:
    new_rank = (1 - d) * (1.0 if current_node == source else 0.0) + d * total
    print(f"{current_node}\t{new_rank}\t{links}")