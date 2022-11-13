import re

def count_pattern(s: str, counts, exemplars):
    """Increment the count for the pattern of s"""

    # Replace strings of digits and month abbreviations with placeholder values
    s = re.sub(r'\d+', 'x', s.strip())
    s = re.sub('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec', 'm', s)
    
    # Count the pattern ns
    if s in counts:
        counts[s] += 1
    else:
        counts[s] = 1
        exemplars[s] = s


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('logfile', type=argparse.FileType('r'))
    args = parser.parse_args()

    counts = {}
    exemplars = {}
    for line in args.logfile:
        count_pattern(line, counts, exemplars)


    for k in sorted(counts, key=counts.get, reverse=True):
        print(f"{counts[k]:10}: {exemplars[k]}")
