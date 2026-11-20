from heapQueue import PriorityQueue
from book import Book
import csv

def createMinHeap(data):
    return

def createMaxHeap(datafile):
    maxHeap = PriorityQueue("max")
    with open(datafile, "r", encoding="utf-8") as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            title, surname, firstname, downloads = row
            book = Book(title, surname, firstname, downloads)
            maxHeap.enqueue(book)
    return maxHeap

def main():
    return 