from datetime import datetime

class user_information:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class Chats_Message:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = user_information('juhi', 'Ms.', 22, 3.5)

friend_one = user_information('kirti', 'Ms.', 22,4.5)
friend_two = user_information('shubbu', 'Mr.', 22,4.5)
friend_three = user_information('mansi', 'Ms.', 35,4.4)
friend_four=spy('soni','Ms.',27,2.5)
friend_five=spy('kaushal','Mr.',38,3.5)


friends = [friend_one, friend_two, friend_three ,friend_four, friend_five]
