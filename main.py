from heapQueue import PriorityQueue
from book import Book
import csv

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

    return

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
        print(heap.dequeue())

def main():
    k = 10
    maxHeap = createMaxHeap("data1000.csv")
    minHeap = createMinHeap("data1000.csv")
    displayMax(maxHeap, k)
    # displayMin(minHeap)

main()