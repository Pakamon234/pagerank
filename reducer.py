import sys

d = 0.85
source = "A"

current_node = None
sum_rank = 0.0
structure = ""

def emit_result(node, sum_rank, structure):
    teleport = 1.0 if node == source else 0.0
    rank = (1 - d) * teleport + d * sum_rank
    print(f"{node}\t{rank:.5f}\t{structure}")

for line in sys.stdin:
    key, value = line.strip().split('\t')

    if current_node and key != current_node:
        emit_result(current_node, sum_rank, structure)
        sum_rank = 0.0
        structure = ""

    current_node = key
    if value.startswith("STRUCT:"):
        structure = value[7:]
    else:
        sum_rank += float(value)

if current_node:
    emit_result(current_node, sum_rank, structure)
