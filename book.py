class Book():
    def __init__(self, t, sname, fname, dwnlds):
        self.title = t
        self.surname = sname
        self.firstname = fname
        self.downloads = int(dwnlds)

    def __str__(self):
        return f"{self.title}: {self.surname} {self.firstname} (Dwnlds:{self.downloads})"

    def __lt__(self, other):
        return self.downloads < other.downloads