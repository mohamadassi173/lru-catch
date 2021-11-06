# lru_cache Implementation

## about the task
Implementation of "least recently used cache" using dict of keys,
and every key have a list of [value, previous added key, next added key]
which make the dict to act like a linked list and keep the order of inserted 
keys  with O(1) complexity.

## Required
python

## To run
* clone this repository
* import it 
  > import lru_cache
  > 
  > from lru_cache import lru_cache

## example 
* screenshot from terminal 
<img width="667" alt="Screenshot 2021-11-04 010405" src="https://user-images.githubusercontent.com/57872327/140232808-32294084-c51b-44fe-b1a9-447180e98508.png">
