---
layout: topics-index
title: Learn Reference Guide
stylesheet: /assets/css/topics-index.css
---

# From Original Repo:

A comparative guide to data structures and algorithms.

## Backtracking
* [Hamiltonean Cycles](computer-science/algorithms/Backtracking/Hamiltonean%20Cycles/)
* [Knight's Tour Problem](computer-science/algorithms/Backtracking/Knight's%20Tour%20Problem/)
* [N-Queens Problem](computer-science/algorithms/Backtracking/N-Queens%20Problem/)
* [Sum of subsets](computer-science/algorithms/Backtracking/Sum%20of%20subsets/)

## Branch and Bound
* [Binary Search](./Branch%20and%20Bound/Binary%20Search/)
* [Binary Search Tree](./Branch%20and%20Bound/Binary%20Search%20Tree/)
* [Depth-Limited Search](./Branch%20and%20Bound/Depth-Limited%20Search/)
* [Topological Sort](./Branch%20and%20Bound/Topological%20Sort/)

## Brute Force
* [Binary Tree Traversal](./Brute%20Force/Binary%20Tree%20Traversal/)
* [Bipartiteness Test](./Brute%20Force/Bipartiteness%20Test/)
* [Breadth-First Search](./Brute%20Force/Breadth-First%20Search/)
* [Bridge Finding](./Brute%20Force/Bridge%20Finding/)
* [Bubble Sort](./Brute%20Force/Bubble%20Sort/)
* [Comb Sort](./Brute%20Force/Comb%20Sort/)
* [Cycle Sort](./Brute%20Force/Cycle%20Sort/)
* [Depth-First Search](./Brute%20Force/Depth-First%20Search/)
* [Flood Fill](./Brute%20Force/Flood%20Fill/)
* [Heapsort](./Brute%20Force/Heapsort/)
* [Insertion Sort](./Brute%20Force/Insertion%20Sort/)
* [Lowest Common Ancestor](./Brute%20Force/Lowest%20Common%20Ancestor/)
* [PageRank](./Brute%20Force/PageRank/)
* [Pancake Sort](./Brute%20Force/Pancake%20Sort/)
* [Rabin-Karp's String Search](./Brute%20Force/Rabin-Karp's%20String%20Search/)
* [Selection Sort](./Brute%20Force/Selection%20Sort/)
* [Shellsort](./Brute%20Force/Shellsort/)
* [Tarjan's Strongly Connected Components](./Brute%20Force/Tarjan's%20Strongly%20Connected%20Components/)

## Divide and Conquer
* [Bucket Sort](./Divide%20and%20Conquer/Bucket%20Sort/)
* [Counting Sort](./Divide%20and%20Conquer/Counting%20Sort/)
* [Merge Sort](./Divide%20and%20Conquer/Merge%20Sort/)
* [Pigeonhole Sort](./Divide%20and%20Conquer/Pigeonhole%20Sort/)
* [Quicksort](./Divide%20and%20Conquer/Quicksort/)
* [Radix Sort](./Divide%20and%20Conquer/Radix%20Sort/)

## Dynamic Programming
* [Bellman-Ford's Shortest Path](./Dynamic%20Programming/Bellman-Ford's%20Shortest%20Path/)
* [Catalan Number](./Dynamic%20Programming/Catalan%20Number/)
* [Fibonacci Sequence](./Dynamic%20Programming/Fibonacci%20Sequence/)
* [Floyd-Warshall's Shortest Path](./Dynamic%20Programming/Floyd-Warshall's%20Shortest%20Path/)
* [Integer Partition](./Dynamic%20Programming/Integer%20Partition/)
* [Knapsack Problem](./Dynamic%20Programming/Knapsack%20Problem/)
* [Knuth-Morris-Pratt's String Search](./Dynamic%20Programming/Knuth-Morris-Pratt's%20String%20Search/)
* [Levenshtein's Edit Distance](./Dynamic%20Programming/Levenshtein's%20Edit%20Distance/)
* [Longest Common Subsequence](./Dynamic%20Programming/Longest%20Common%20Subsequence/)
* [Longest Increasing Subsequence](./Dynamic%20Programming/Longest%20Increasing%20Subsequence/)
* [Longest Palindromic Subsequence](./Dynamic%20Programming/Longest%20Palindromic%20Subsequence/)
* [Maximum Subarray](./Dynamic%20Programming/Maximum%20Subarray/)
* [Maximum Sum Path](./Dynamic%20Programming/Maximum%20Sum%20Path/)
* [Nth Factorial](./Dynamic%20Programming/Nth%20Factorial/)
* [Pascal's Triangle](./Dynamic%20Programming/Pascal's%20Triangle/)
* [Shortest Common Supersequence](./Dynamic%20Programming/Shortest%20Common%20Supersequence/)
* [Sieve of Eratosthenes](./Dynamic%20Programming/Sieve%20of%20Eratosthenes/)
* [Sliding Window](./Dynamic%20Programming/Sliding%20Window/)
* [Ugly Numbers](./Dynamic%20Programming/Ugly%20Numbers/)
* [Z String Search](./Dynamic%20Programming/Z%20String%20Search/)

## Greedy
* [Boyer–Moore's Majority Vote](computer-science/algorithms/Greedy/Boyer–Moore's%20Majority%20Vote/)
* [Dijkstra's Shortest Path](computer-science/algorithms/Greedy/Dijkstra's%20Shortest%20Path/)
* [Job Scheduling Problem](computer-science/algorithms/Greedy/Job%20Scheduling%20Problem/)
* [Kruskal's Minimum Spanning Tree](computer-science/algorithms/Greedy/Kruskal's%20Minimum%20Spanning%20Tree/)
* [Prim's Minimum Spanning Tree](computer-science/algorithms/Greedy/Prim's%20Minimum%20Spanning%20Tree/)
* [Stable Matching](computer-science/algorithms/Greedy/Stable%20Matching/)

## Simple Recursive
* [Cellular Automata](./Simple%20Recursive/Cellular%20Automata/)
* [Cycle Detection](./Simple%20Recursive/Cycle%20Detection/)
* [Euclidean Greatest Common Divisor](./Simple%20Recursive/Euclidean%20Greatest%20Common%20Divisor/)
* [Nth Factorial](./Simple%20Recursive/Nth%20Factorial/)
* [Suffix Array](./Simple%20Recursive/Suffix%20Array/)

## Uncategorized
* [Affine Cipher](computer-science/algorithms/Uncategorized/Affine%20Cipher/)
* [Caesar Cipher](computer-science/algorithms/Uncategorized/Caesar%20Cipher/)
* [Freivalds' Matrix-Multiplication Verification](computer-science/algorithms/Uncategorized/Freivalds'%20Matrix-Multiplication%20Verification/)
* [K-Means Clustering](computer-science/algorithms/Uncategorized/K-Means%20Clustering/)
* [Magic Square](computer-science/algorithms/Uncategorized/Magic%20Square/)
* [Maze Generation](computer-science/algorithms/Uncategorized/Maze%20Generation/)
* [Miller-Rabin's Primality Test](computer-science/algorithms/Uncategorized/Miller-Rabin's%20Primality%20Test/)
* [Shortest Unsorted Continuous Subarray](computer-science/algorithms/Uncategorized/Shortest%20Unsorted%20Continuous%20Subarray/)

---


# Learn Reference Guide

A multi-disciplinary learning reference guide.

{% for discipline in site.data.curriculum %}
<h2>{{ discipline.discipline }}</h2>

{% for subject in discipline.subjects %}
<!-- Link to the subject's main index page -->
<h3>
<a href="{{ site.baseurl }}/{{ discipline.folder | uri_escape }}/{{ subject.folder | uri_escape }}/">
{{ subject.name }}
</a>
</h3>

<ul>
{% for category in subject.categories %}
<!-- Link to the specific category index page -->
<li>
<a href="{{ site.baseurl }}/{{ discipline.folder | uri_escape }}/{{ subject.folder | uri_escape }}/{{ category.folder | uri_escape }}/">
{{ category.name }}</a>
</li>
{% endfor %}
</ul>
{% endfor %}
<hr>
{% endfor %}