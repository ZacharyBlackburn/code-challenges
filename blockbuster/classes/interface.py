from classes.videos import Videos
from classes.blockbuster import Blockbuster
from classes.customer import Customer


class Interface:
    def __init__(self, name):
        self.store = Blockbuster(name)
        self.all_videos = Videos.get_all_videos()
        self.all_customers = Customer.get_all_customers()

    def run(self):
        while True:
            # check = self.store.authenticate_user()
            # if check == False:
            #     break
            mode = input(self.menu())

            if mode == '1':
                self.store.view_inventory()

            elif mode == '2':
                customer_id = input('Enter customer ID:\n')
                self.store.find_customer_rentals(customer_id)

            elif mode == '3':
                self.store.add_customer(self.mode_3_menu())

            elif mode == '4':
                self.mode_4_menu()

            elif mode == '5':
                customer_id = input('Enter customer ID:\n')
                for customers in self.all_customers:
                    if customer_id == customers.id:
                        self.store.get_customer(customer_id)
                        videos_rented_string = str(
                            self.store.find_customer_rentals(customer_id))
                        videos_rented_list = ''.split(videos_rented_string)
                        print(videos_rented_list.pop())
                        video_title = input(
                            '\nType the title of the video the customer would like to return:'
                        )
                        self.store.remove_current_video_rental(video_title)

            elif mode == '6':
                self.store.add_video(self.mode_6_menu())

            elif mode == '7':
                break

    def menu(self):
        return f"""

         _     _            _    _               _
        | |   | |          | |  | |             | |
        | |__ | | ___   ___| | _| |__  _   _ ___| |_ ___ _ __
        | '_ \| |/ _ \ / __| |/ / '_ \| | | / __| __/ _ \ '__|
        | |_) | | (_) | (__|   <| |_) | |_| \__ \ ||  __/ |
        |_.__/|_|\___/ \___|_|\_\_.__/ \__,_|___/\__\___|_|

                Welcome to the employee rental menu.
                  What would you like to do today?

        1. View store video inventory.
        2. View customer rented videos.
        3. Add new customer.
        4. Rent video.
        5. Return video.
        6. Add new video to inventory.
        7. Exit.

        """

    def mode_3_menu(self):
        customer_info = {}
        account_priv = input(
            'Choose the number associated with new customer account type:\n1: Standard\n2: Premium\n3: Standard Family\n4: Premium Family\n5: Cancel Customer Account Creation\n\n'
        )
        if account_priv != '5':
            if account_priv == '1':
                print(
                    'Customer has a standard account and can rent 1 video at a time. Please continue.'
                )
                customer_info['account_type'] = 'sx'
            elif account_priv == '2':
                print(
                    'Customer has a premium account and can rent 3 videos at a time. Please continue.'
                )
                customer_info['account_type'] = 'px'
            elif account_priv == '3':
                print(
                    'Customer has a standard family account and can rent 1 PG-13 and below rated video at a time. Please continue.'
                )
                customer_info['account_type'] = 'sf'
            elif account_priv == '4':
                print(
                    'Customer has a premium family account and can rent 3 PG-13 and below rated videos at a time. Please continue.'
                )
                customer_info['account_type'] = 'pf'
            elif account_priv != '1' or account_priv != '2' or account_priv != '3' or account_priv != '4' or account_priv != '5':
                print('Invalid Input. Please select a number between 1-5.')
                return self.mode_3_menu()
            account_id = input('Enter the customer ID:\n')
            for accounts in self.all_customers:
                if account_id == accounts.id:
                    print(
                        "This account ID has already been taken. Please type a different ID number.\n\n\n"
                    )
                    return self.mode_3_menu()
            customer_info['id'] = account_id
            customer_info['first_name'] = input('Enter customer first name:\n')
            customer_info['last_name'] = input('Enter customer last name:\n')
            return customer_info

    def mode_4_menu(self):
        customer_id = input('Enter customer ID:\n')
        self.store.get_customer(customer_id)
        self.store.find_customer_rentals(customer_id)
        account_priv = self.store.get_customer_account_type(customer_id)
        current_rentals_num = self.store.get_customer_video_length(customer_id)

        if account_priv == 'sx':
            print(
                '\nCustomer has a standard account and can rent 1 video at a time.'
            )

            if current_rentals_num >= 1:
                print('Customer has reached their max movie rental limit.')
                return Interface(
                    'Bend Blockbuster: The Last Blockbuster').run()
            if current_rentals_num == 0:
                video_title = input(
                    '\nType the title of the video the customer would like to rent:\n'
                )
                for videos in self.store.all_videos:
                    if video_title == videos.title and videos.copies_available > 0:
                        self.store.add_current_video_rental(video_title)
                        print(
                            'Video has been successfully rented. Remind the customer they have 1 week to return it.'
                        )
                    if video_title == videos.title and videos.copies_available < 1:
                        print("Not enough videos available!")

        if account_priv == 'px':
            print(
                '\nCustomer has a premium account and can rent 3 videos at a time.'
            )

            if current_rentals_num > 2:
                print('Customer has reached their max movie rental limit.')
                return Interface(
                    'Bend Blockbuster: The Last Blockbuster').run()
            if current_rentals_num <= 2:
                video_title = input(
                    '\nType the title of the video the customer would like to rent:\n'
                )
                for videos in self.store.all_videos:
                    if (video_title
                            == videos.title) and (videos.copies_available > 0):
                        self.store.add_current_video_rental(video_title)
                        print(
                            'Video has been successfully rented. Remind the customer they have 1 week to return it.'
                        )
                    if video_title == videos.title and videos.copies_available < 1:
                        print("Not enough videos available!")

        if account_priv == 'sf':
            print(
                '\nCustomer has a standard family account and can rent 1 PG-13 or below rated video at a time.'
            )

            if current_rentals_num >= 1:
                print('Customer has reached their max movie rental limit.')
                return Interface(
                    'Bend Blockbuster: The Last Blockbuster').run()
            if current_rentals_num == 0:
                video_title = input(
                    '\nType the title of the video the customer would like to rent:\n'
                )
                for videos in self.store.all_videos:
                    if video_title == videos.title and videos.rating != 'R' and videos.copies_available > 0:
                        self.store.add_current_video_rental(video_title)
                        print(
                            'Video has been successfully rented. Remind the customer they have 1 week to return it.'
                        )
                    if video_title == videos.title and videos.rating == 'R':
                        print("No can do, that's an explicit movie.")
                    if video_title == videos.title and videos.copies_available < 1:
                        print("Not enough videos available!")

        if account_priv == 'pf':
            print(
                '\nCustomer has a standard family account and can rent 3 PG-13 or below rated videos at a time.'
            )

            if current_rentals_num >= 3:
                print('\nCustomer has reached their max movie rental limit.')
                return Interface(
                    'Bend Blockbuster: The Last Blockbuster').run()
            if current_rentals_num <= 2:
                video_title = input(
                    '\nType the title of the video the customer would like to rent:\n'
                )
                for videos in self.store.all_videos:
                    if video_title == videos.title and videos.rating != 'R' and videos.copies_available > 0:
                        self.store.add_current_video_rental(video_title)
                        print(
                            'Video has been successfully rented. Remind the customer they have 1 week to return it.'
                        )
                    if video_title == videos.title and videos.rating == 'R':
                        print("No can do, that's an explicit movie.")
                    if video_title == videos.title and videos.copies_available < 1:
                        print("Not enough videos available!")

    def mode_6_menu(self):
        video_info = {}
        video_id = input('Enter the new video ID:\n')
        for videos in self.all_videos:
            if video_id == videos.id:
                print(
                    "This video ID has already been used. Please type a different ID number.\n\n\n"
                )
                return self.mode_6_menu()
        video_info['id'] = video_id
        video_info['title'] = input('Enter the title of the new video:\n')
        video_info['rating'] = input('Enter the rating of the new video:\n')
        if (video_info['rating'] != 'G') and (
                video_info['rating'] != 'PG'
        ) and (video_info['rating'] != 'PG-13') and (
                video_info['rating'] != 'R') and (video_info['rating'] != 'X'):
            print("Invalid rating, please try again.")
            return self.mode_6_menu()
        video_info['release_year'] = input(
            'Enter the release year of the new video:\n')
        if len(video_info['release_year']) != 4:
            print("Invalid release year, please try again.")
            return self.mode_6_menu()
        video_info['copies_available'] = input(
            'Enter the number of copies available:\n')
        if int(video_info['copies_available']) > 99:
            print("Invalid input, please try again.")
            return self.mode_6_menu()

        return video_info
