import csv
import collections
import itertools

infile = "Artist_lists_small.txt"
outfile = "Arena_Code_challenge_output.txt"

reader = csv.reader(open(infile, 'rb'), delimiter=',')
all_lines = []
for line in reader:
    all_lines.append(line)

o = open(outfile, "w")

counts = collections.defaultdict(int)
for bandpair in all_lines:
    bandpair.sort()
    for pair in itertools.combinations(bandpair, 2):
        counts[pair] += 1

for pair, total in counts.items():
    if total >= 50:
        printpair = str(pair).strip("(,)")+"\n"
        printpair = printpair.replace("'", "")
        printpair = printpair.replace(", ", ",")
        o.write(printpair)

