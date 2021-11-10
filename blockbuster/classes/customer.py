import csv
import os.path
from classes.videos import Videos

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/customers.csv")


class Customer:
    def __init__(
        self,
        id,
        account_type,
        first_name,
        last_name,
    ):
        self.id = id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = []

    def __repr__(self):
        return f"""
            ID: {self.id}
            Account Type: {self.account_type}
            First Name: {self.first_name}
            Last Name: {self.last_name}
            Current Rentals: {self.current_video_rentals}
        """

    # Parsing string of videos from CSV
    def parse_customer_videos(self, video_string):
        video_str_array = video_string.split('/')
        return self.create_videos_arr(video_str_array)

    # Creating video instance from parsed video array
    def create_videos_arr(self, video_str_array):
        all_videos = Videos.get_all_videos()
        for video in video_str_array:
            for video_instance in all_videos:
                if video == video_instance.title:
                    self.current_video_rentals.append(video_instance)
        return self.current_video_rentals

    def remove_video_instance(self, video_instance):
        self.current_video_rentals.remove(video_instance)
        return self.current_video_rentals

    def add_video_instance(self, video_instance):
        self.current_video_rentals.append(video_instance)
        return self.current_video_rentals

    @classmethod
    def get_all_customers(cls):
        all_customers = []
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customer_instance = Customer(row['id'], row['account_type'],
                                             row['first_name'],
                                             row['last_name'])
                video_str_array = customer_instance.parse_customer_videos(
                    row['current_video_rentals'])
                customer_instance.create_videos_arr(video_str_array)
                all_customers.append(customer_instance)
        return all_customers
