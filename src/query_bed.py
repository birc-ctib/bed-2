"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    read_bed_file, print_line, BedLine
)


def lower_bound(features: list[BedLine], start: int) -> int:
    """Return the index of the lower bound of start in features."""
    lo, hi = 0, len(features)
    while lo < hi:
        m = (lo + hi) // 2
        if features[m].chrom_start < start:
            lo = m + 1
        else:
            hi = m
    return lo


def extract_region(features: list[BedLine],
                   start: int, end: int) -> list[BedLine]:
    """Extract region chrom[start:end] and write it to outfile."""
    lb = lower_bound(features, start)
    ub = lower_bound(features, end+1)  # upper bound of end
    return features[lb:ub]


def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',  # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    features = read_bed_file(args.bed)
    for query in args.query:
        chrom, start, end = query.split()
        # Extract the region from the chromosome, using your extract_region()
        # function. If you did your job well, this should give us the features
        # that we want.
        region = extract_region(
            features.get_chrom(chrom), int(start), int(end))
        for line in region:
            print_line(line, args.outfile)


if __name__ == '__main__':
    main()
