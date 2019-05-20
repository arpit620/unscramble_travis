# Changelog
All changes with a new version release should go in detail over here.

## [0.1.0] - 2019-05-16
### Added
- Added actual dictionary for the lookup
- Added tqdm to see the progress bar
- Added ``_get_defaultdict`` which returns dictionary where key represent # of 
  character and value is the list of word with specified length. 
- Added ``print_dict`` method which prints out dictionary in a readable format.
- Sort by keys in decreasing order

### Changed
- Changed all methods to internal except ``find_words()``
- Changed to proper parameter exchange within methods.
  Using self everywhere was creating confusion where the variable is coming from.

### Removed
- Removed ``generate_words()`` method. Moved the method calls to ``find_words()``
  as it was redundant.
- Removed 2

## To Do

- Optimization: Make the process faster by using parallelization.
- Scale up. Currently can't be used for big words.
- Add a functionality to specify range for # of characters in a word.