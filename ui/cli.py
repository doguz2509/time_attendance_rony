
import os
import json


class DataManager:
    def __init__(self, file_path):
        self._file_path = file_path
        self._data = dict()

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self._file_path, 'w+') as sw:
            json.dump(self._data, sw)

    def __enter__(self):
        # Read file, assign data to class
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as sr:
                self._data = json.loads('\n'.join(sr.readlines()))
        return self

    def select_user(self):
        user_list = self._data.get('user_list', [])
        if len(user_list) == 0:
            print('No users defined yet; Please signup')
            return '', 0

        return '\n'.join(user_list) + f'{len(user_list) + 1} Exit', len(user_list) + 1




