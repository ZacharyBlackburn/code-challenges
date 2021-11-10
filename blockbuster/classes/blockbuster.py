from classes.customer import Customer
from classes.videos import Videos
import os
import csv

my_path = os.path.abspath(os.path.dirname(__file__))
customer_path = os.path.join(my_path, "../data/customers.csv")
video_path = os.path.join(my_path, "../data/inventory.csv")


class Blockbuster:
    def __init__(self, name):
        self.name = name
        self.all_customers = Customer.get_all_customers()
        self.all_videos = Videos.get_all_videos()
        self.selected_customer = None

    def print_all_customers(self):
        self.all_customers = Customer.get_all_customers()
        return self.all_customers

    def view_inventory(self):
        print('\n')
        for i, videos in enumerate(self.all_videos):
            print(
                f'\n{i + 1}: {videos.title}, Rated {videos.rating}\nReleased:{videos.release_year}\nCopies Available: {videos.copies_available}\n'
            )

    def add_customer(self, customer_info):
        self.all_customers.append(Customer(**customer_info))
        print(self.all_customers)
        self.update_new_customer()
        self.save_customers()

    def add_video(self, video_info):
        self.all_videos.append(Videos(**video_info))
        self.save_videos()

    #customer_id is input on interface
    def find_customer_rentals(self, customer_id):
        self.selected_customer = None
        for customer in self.all_customers:
            if customer.id == customer_id:
                self.selected_customer = customer
                print(
                    f"\n{customer.first_name} {customer.last_name}'s current rentals:\n"
                )
                current_video_str = str(customer.current_video_rentals)
                print(current_video_str[1:-1])

    def get_customer_video_length(self, customer_id):
        self.selected_customer = None
        for customer in self.all_customers:
            if customer.id == customer_id:
                self.selected_customer = customer
                video_length = len(customer.current_video_rentals)
                return video_length

    def get_customer_account_type(self, customer_id):
        self.selected_customer = None
        for customer in self.all_customers:
            if customer.id == customer_id:
                self.selected_customer = customer
                current_account_str = str(customer.account_type)
                return current_account_str

    # Customer instance
    def get_customer(self, customer_id):
        self.selected_customer = None
        for customer in self.all_customers:
            if customer_id == customer.id:
                self.selected_customer = customer
        return self.selected_customer

    #input video title
    def remove_current_video_rental(self, video_title):
        selected_video = None
        for video in self.selected_customer.current_video_rentals:
            if video_title == video.title:
                selected_video = video
        self.selected_customer.remove_video_instance(selected_video)
        self.add_video_back(selected_video)
        self.update_all_customers()
        self.save_videos()
        return None

    def add_current_video_rental(self, video_title):
        selected_video = None
        for video in self.all_videos:
            if video_title == video.title:
                selected_video = video
        self.selected_customer.add_video_instance(selected_video)
        self.take_video_away(selected_video)
        self.update_all_customers()
        self.save_videos()
        return None

    def update_all_customers(self):
        for customer in self.all_customers:
            if customer.id == self.selected_customer.id:
                customer = self.selected_customer
        self.save_customers()
        return self.all_customers

    def update_new_customer(self):
        self.save_customers()
        return self.all_customers

    # method to add back to copies available in inventory.csv
    def add_video_back(self, video_instance):
        for video in self.all_videos:
            if video_instance.title == video.title:
                video.copies_available += 1
        return video

    # method to subtract from copies available in inventory.csv
    def take_video_away(self, video_instance):
        for video in self.all_videos:
            if video_instance.title == video.title:
                video.copies_available -= 1
        return video

    def save_customers(self):
        with open(customer_path, 'w') as csv_file:
            fieldnames = [
                'id', 'account_type', 'first_name', 'last_name',
                'current_video_rentals'
            ]
            customer_csv = csv.DictWriter(csv_file, fieldnames=fieldnames)
            customer_csv.writeheader()
            for customer in self.all_customers:
                customer_csv.writerow({
                    'id':
                    customer.id,
                    'account_type':
                    customer.account_type,
                    'first_name':
                    customer.first_name,
                    'last_name':
                    customer.last_name,
                    'current_video_rentals':
                    "/".join([
                        videos.title
                        for videos in customer.current_video_rentals
                    ])
                })

    def save_videos(self):
        with open(video_path, 'w') as csv_file:
            fieldnames = [
                'id', 'title', 'rating', 'release_year', 'copies_available'
            ]
            video_csv = csv.DictWriter(csv_file, fieldnames=fieldnames)
            video_csv.writeheader()
            for video in self.all_videos:
                video_csv.writerow({
                    'id': video.id,
                    'title': video.title,
                    'rating': video.rating,
                    'release_year': video.release_year,
                    'copies_available': video.copies_available
                })

    # def store_password(self, store_pass):
    #     self.store_pass = store_pass
    #     return store_pass

    # def authenticate_user(self):
    #     count = 3
    #     while count > 0:
    #         print(f"\n\n\nWelcome to {self.name}\n_________________________\n")
    #         self.store_pass = 'password'
    #         password = input("Please enter the store password: \n")
    #         if password == self.store_pass:
    #             return f"Thank you, welcome to the store management console.\n"
    #         if count > 1:
    #             print(
    #                 "\nAre you authorized to enter the management console? If not, stop and walk away. If so, try again.\n"
    #             )
    #         count -= 1
    #     if count == 0:
    #         print("\nYou are not authorized to access this console.\n")
    #     return False