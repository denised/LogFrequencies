import re

strip_digits = str.maketrans("","","0123456789")

def count_pattern(s: str, counts, exemplars):
    """Increment the count for the pattern of s"""

    # Generalize s to pattern ns
    # Quick and dirty generalization: delete the digits.  This will take care of dates, times, pids, etc.
    # It won't get month names if they are spelled out.  And of course some log messages may have other differing parts like usernames, etc.
    ns = s.translate(strip_digits)
    
    # Count the pattern ns
    if ns in counts:
        counts[ns] += 1
    else:
        counts[ns] = 1
        # also set the exemplar
        # the exemplar is a string we will show to users.  we still want to remove
        # digits to help with stability across runs, but we want there to be a placeholder 
        # for them so the exemplar looks more like the string it is replacing.
        exemplars[ns] = re.sub(r'\d+','x', s.strip())


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('logfile', type=argparse.FileType('r'))
    args = parser.parse_args()

    counts = {}
    exemplars = {}
    for line in args.logfile:
        count_pattern(line, counts, exemplars)


    for k in sorted(counts.keys()):
        print(f"{counts[k]:10}: {exemplars[k]}")
