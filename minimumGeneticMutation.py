from collections import deque

startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]

bank = set(bank)
        
seen = set()
queue = deque()
        
seen.add(startGene)
queue.append(startGene)
steps = 0
        
while queue:
    for i in range(len(queue)):
        curr_gene = queue.popleft()
        if curr_gene == endGene:
            print(steps)
        for mutation in ["A", "C", "G", "T"]:
            for j in range(len(startGene)): 
                mut_gene = curr_gene[:j] + mutation + curr_gene[j + 1:]
                if (mut_gene not in seen) and (mut_gene in bank):
                    seen.add(mut_gene)
                    queue.append(mut_gene)
    steps += 1
print(-1)