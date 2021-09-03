import datetime
from typing import Iterable, List


_user_counter = 0


class User(dict):
    def __init__(self, **kwargs):
        global _user_counter
        _user_counter += 1
        uid = _user_counter
        kwargs.update(**{'uid': uid})
        assert kwargs.get('name'), 'Name must be provided'
        assert kwargs.get('family_name'), 'family_name must be provided'
        assert kwargs.get('start_date'), 'start_date must be provided'
        kwargs.update(**{'start_date': datetime.datetime.strptime(kwargs.get('start_date'), '%d/%m/%Y')})
        assert kwargs.get('mail'), 'mail must be provided'
        is_verified = bool(kwargs.get('is_verified', True))
        kwargs.update(**{'is_verified': is_verified})
        super().__init__(**kwargs)

    def __str__(self):
        return ', '.join(f"{k}: {v}" for k, v in self.items())


class TimeAttendance:
    def __init__(self, **kwargs):
        self.uid = kwargs.get('uid')
        self.did = kwargs.get('did')
        self.date = datetime.datetime.now()
        self.start = datetime.datetime.strptime(kwargs.get('start'), '%H:%M')
        self._end = kwargs.get('end')

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        date_value = datetime.datetime.strptime(value, '%d/%m/%Y')
        self._end = date_value


class Test:
    def __init__(self, **kwargs):
        self.uid = kwargs.get('uid')
        self.did = kwargs.get('did')
        self.type = kwargs.get('type')
        self.place = kwargs.get('place')


class AttendanceData(dict):
    tables = ['users', 'attendances', 'tests']

    def __init__(self):
        super().__init__()
        for name in self.tables:
            self.setdefault(name, [])

    @property
    def users(self) -> List[User]:
        return self['users']

    @property
    def attendances(self) -> List[TimeAttendance]:
        return self['attendances']

    @property
    def tests(self) -> Iterable[Test]:
        return self['tests']

    def __str__(self):
        return '\n'.join(f"{i}" for i in self.users)


if __name__ == '__main__':

    data = AttendanceData()
    data.users.append(User(name='Rony', family_name='Oguz', start_date='03/09/2021', mail='d@d.com'))
    roni_uid = [u for u in data.users if u.name == 'Rony'][0]
    data.users.append(User(name='Dima', family_name='Oguz', start_date='03/09/2021', mail='a@d.com'))
    print(f"{data}")
    roni_uid = [u for u in data.users if u.name == 'Rony'][0]
    data.attendances.append(TimeAttendance(uid=roni_uid, start='12:34'))
