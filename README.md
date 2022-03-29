# Processing BED files (Part 2)

If our BED files are sorted, we should be able to extract regions in logarithmic time instead of linear time, if we use binary search instead of linear search.

## Sorting BED files

In the file `src/sort_bed.py` there is a function

```python
def sort_file(table: Table) -> None
```

that almost sorts a BED file. I is just lacking the sorting part. The function runs through all the chromosomes in the input, and you get them as a list for each chromosome. Sort that list according to the start position. Then the rest of the program should work.

## Merging sorted BED files

If you have two sorted BED files and you want a single sorted BED file with the features from them, it is more efficient to merge them than to concatenate them and then sort them. **FIXME**

## Querying BED files with binary search


## Report

*Answer the questions below and then push this file to GitHub.*



*Would anything be more difficult if the features covered ranges instead of single nucleotides (like real BED files)? What could go wrong, if anything?*

*We wrote a tool for merging two BED files, but what if we had a bunch of them? What would the complexity be if we merged them in, one at a time? What would the complexity be if we merged all of the files at the same time?*

