import csv
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/inventory.csv")


class Videos:
    def __init__(self, id, title, rating, release_year, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = int(copies_available)

    def __repr__(self):
        return f"""{self.title}"""

    def __str__(self):
        return f"""
            Video ID: {self.id}
            Title: {self.title}
            Rating: {self.rating}
            Release Year: {self.release_year}
            Copies Available: {self.copies_available}
        """

    @classmethod
    def get_all_videos(cls):
        all_videos = []
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                video_instance = Videos(**row)
                all_videos.append(video_instance)
        return all_videos