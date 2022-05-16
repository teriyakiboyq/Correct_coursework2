import json


class CandidatesDAO:

    def __init__(self, path, com):
        self.path = path
        self.com = com

    def load_data(self):
        with open(self.path, 'r', encoding='utf8') as file:
            data = json.load(file)
        return data

    def get_posts_by_user(self, user_name):
        list_obj = []
        json_load = self.load_data()
        for user in json_load:
            if user_name == user['poster_name']:
                list_obj.append(user)
        return list_obj

    def get_posts_by_comments(self, post_id):
        list_obj = []
        with open(self.com, 'r', encoding='utf8') as file:
            data = json.load(file)
        for comments in data:
            if post_id == comments['post_id']:
                list_obj.append(comments)
        return list_obj

    def get_all(self):
        candidates = self.load_data()
        return candidates

    def get_post_by_pk(self, pk):
        candidates = self.load_data()
        for candidate in candidates:
            if candidate['pk'] == pk:
                return candidate

    def search_for_posts(self, query):
        list_quer = []
        data = self.load_data()
        for i in data:
            if query in i['content']:
                list_quer.append(i)
        return list_quer

