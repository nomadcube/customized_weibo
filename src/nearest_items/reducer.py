#! /usr/bin/env python
import sys

nearest_post = None
largest_similarity = 0.0

for line in sys.stdin:
    similarity, post = line.strip().split(",", 1)
    similarity = float(similarity)
    if similarity > largest_similarity:
        largest_similarity = similarity
        nearest_post = post

print nearest_post
