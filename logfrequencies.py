import re

strip_digits = str.maketrans("","","0123456789")

all_pattern_counts = {}
all_pattern_exemplars = {}

def clear_patterns():
    global all_pattern_counts, all_pattern_exemplars
    all_pattern_counts = {}
    all_pattern_exemplars = {}

def add_pattern(s: str):
    # Quick and dirty normalization:
    # To make log strings comparable to one another, delete the digits.  This will take care of dates, times, pids, etc.
    # It won't get month names if they are spelled out.  And of course some log messages may have other differing parts like usernames, etc.
    ns = s.translate(strip_digits)
    if ns in all_pattern_counts:
        all_pattern_counts[ns] += 1
    else:
        all_pattern_counts[ns] = 1
        # the exemplar is a string we will show to users.  we still want to remove
        # digits to help with stability across runs, but we want there to be a placeholder 
        # for them so the exemplar looks more like the string it is replacing.
        all_pattern_exemplars[ns] = re.sub(r'\d+','x', s.strip())

def process_file(fp):
    for line in fp:
        add_pattern(line)

if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('logfile', type=argparse.FileType('r'))
    args = parser.parse_args()

    process_file(args.logfile)

    for k in sorted(all_pattern_exemplars.keys()):
        count = all_pattern_counts[k]
        name = all_pattern_exemplars[k]
        print(f"{count:10}: {name}")
