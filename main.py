from heapQueue import PriorityQueue
from book import Book
import csv

def createMinHeap(data):
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
    maxHeap = createMaxHeap("data1000.csv")
    displayMax(maxHeap, 10)

main()