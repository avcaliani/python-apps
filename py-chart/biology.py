"""
Further Information
- https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
- https://www.ncbi.nlm.nih.gov/nuccore/M10098.1?report=fasta
- https://www.ncbi.nlm.nih.gov/nuccore/NR_024570.1?report=fasta
"""
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'


red = lambda value: f'\033[1;31;40m{value}\033[0m'
green = lambda value: f'\033[1;32;40m{value}\033[0m'
number_format = lambda value: red(f'- { -1 * value }') if value < 0 else f'+ {value}'


def get_nucleotides():
    nucleotides, letters = {}, ['A', 'T', 'C', 'G', 'N']
    for x in letters:
        for y in letters:
            nucleotides[ x + y ] = 0
    return nucleotides


def process(file):
    nucleotides = get_nucleotides()
    data = open(file).read().replace('\n', '')
    for i in range(len(data) - 1):
        key = data[i] + data[i + 1]
        nucleotides[key] += 1
    return nucleotides


bacterium = process('data/biology.escherichia.fasta')
human = process('data/biology.human.fasta')

# ---------------------------------
#  OUTPUT
# -----------------------------
print("\n# SUBTITLE")
print("NC   : Nucleotides")
print("DIFF : Human Nucleotides - Escherichia Bacterium Nucleotides\n")

print('+---------------------------------------+')
print('| NC | \tHUMAN\tBACTERIUM\tDIFF\t|')
print('+----+----------------------------------+')

subtitle = get_nucleotides()
for key in subtitle:
    h, b = human[key], bacterium[key]
    diff = h-b
    if diff == 0:
        print(f'| {key} |\t{h}\t{b}\t\t{number_format(diff)}\t|')
    else:
        print(f'| {key} |\t{green(h) if h > b else h}\t{green(b) if b > h else b}\t\t{number_format(diff)}\t|')
print('+---------------------------------------+\n')
