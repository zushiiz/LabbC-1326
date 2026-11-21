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

def enqueueMallocTest(heapType, amountOfData):
    print("======================================================")      
    print(f"MallocTest: {heapType}-heap")
    tracemalloc.start() 
    if heapType == "min":
        heap = createMinHeap("data1000.csv", amountOfData)
    else:
        heap = createMaxHeap("data1000.csv")
    print(f"{heapType}-heap Current Memory Usage: {tracemalloc.get_traced_memory()[0]}")
    print(f"{heapType}-heap Peak Memory Usage: {tracemalloc.get_traced_memory()[1]}")
    tracemalloc.stop()
    print("======================================================")    
    return heap

def main():
    k = 10

    maxHeap = enqueueMallocTest("max", k)
    minHeap = enqueueMallocTest("min", k)

main()