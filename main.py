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

def createMaxHeap(datafile, k):
    topK = []
    maxHeap = PriorityQueue("max")
    with open(datafile, "r", encoding="utf-8") as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for row in csvFile:
            title, surname, firstname, downloads = row
            book = Book(title, surname, firstname, downloads)
            maxHeap.enqueue(book)
    for i in range(k):
        topK.append(maxHeap.dequeue())
    return topK

def mallocTest(heapType, amountOfData):
    print("======================================================")      
    print(f"MallocTest: {heapType}-heap (k={amountOfData})")
    tracemalloc.start() 
    if heapType == "min":
        result = createMinHeap("data75000.csv", amountOfData)
    else:
        result = createMaxHeap("data75000.csv", amountOfData)
    print(f"{heapType}-heap Current Memory Usage: {tracemalloc.get_traced_memory()[0]}")
    print(f"{heapType}-heap Peak Memory Usage: {tracemalloc.get_traced_memory()[1]}")
    tracemalloc.stop()
    print("======================================================")


def main():
    k = int(input("Data amount (k):"))
    mallocTest("max", k)
    mallocTest("min", k)

main()