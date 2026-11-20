"""
Written by Zixuan Huang (zixuanhu@ug.kth.se), No use of AI
Created 2026-11-20
"""
from heapQueue import PriorityQueue
from book import Book
import csv, timeit, tracemalloc

def createMinHeap(datafile, k):
    minHeap = PriorityQueue("min")
    with open(datafile, "r", encoding="utf-8") as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for row in csvFile:
            title, surname, firstname, downloads = row
            book = Book(title, surname, firstname, downloads)
            if minHeap.size() >= k: # Is queue full
                if minHeap.peek() < book: # Insert or not
                    minHeap.dequeue()
                    minHeap.enqueue(book)
            else:
                minHeap.enqueue(book)
    return minHeap

def createMaxHeap(datafile):
    maxHeap = PriorityQueue("max")
    with open(datafile, "r", encoding="utf-8") as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for row in csvFile:
            title, surname, firstname, downloads = row
            book = Book(title, surname, firstname, downloads)
            maxHeap.enqueue(book)
    return maxHeap

def displayMax(heap, k):
    print(f"Leaderboard of Top {k} Books(Max Heap)")
    for i in range(k):
        book = heap.dequeue()
        # print(book)
    print("==================================================")
    
def displayMin(heap):
    print(f"Leaderboard of Top {heap.size()} Books(Min Heap)")
    for i in range(heap.size()):
        book = heap.dequeue()
        # print(book)

def main():
    k = 10000

    print("Insertion in MaxHeap")
    tracemalloc.start() 
    maxHeap = createMaxHeap("data1000.csv")
    print(f"Max Heap Current Memory Usage: {tracemalloc.get_traced_memory()[0]}")
    print(f"Max Heap Peak Memory Usage: {tracemalloc.get_traced_memory()[1]}")
    tracemalloc.stop()
    print("======================================================")

    print("Insertion in MinHeap")
    tracemalloc.start()
    minHeap = createMinHeap("data1000.csv", k)
    print(f"Min Heap Current Memory Usage: {tracemalloc.get_traced_memory()[0]}")
    print(f"Min Heap Peak Memory Usage: {tracemalloc.get_traced_memory()[1]}")
    tracemalloc.stop()    
    print("======================================================")


main()