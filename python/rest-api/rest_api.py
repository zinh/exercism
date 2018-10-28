import json

class RestAPI(object):
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == '/users':
            return self.get_users(payload)
        return json.dumps({})

    def post(self, url, payload=None):
        if url == '/add':
            return self.add_user(json.loads(payload)['user'])
        if url == '/iou':
            return self.iou(payload)
        return json.dumps({})

    def add_user(self, user_name):
        user_info = {
                'name': user_name,
                'owes': {},
                'owed_by': {},
                'balance': 0
        }
        self.database['users'].append(user_info)
        return json.dumps(user_info)

    def get_users(self, payload):
        if payload is None:
            return json.dumps({'users': self.database['users']})
        users = json.loads(payload)['users']
        response = {'users': list(map(lambda name: self.get_user_by_name(name), users))}
        return json.dumps(response)

    def iou(self, payload):
        request = json.loads(payload)
        lender = self.get_user_by_name(request['lender'])
        lender_name = lender['name']
        borrower = self.get_user_by_name(request['borrower'])
        borrower_name = borrower['name']
        amount = request['amount']
        if borrower_name in lender['owed_by']:
            lender['owed_by'][borrower_name] += amount
        else:
            lender['owed_by'][borrower_name] = amount
        lender['balance'] += amount
        if lender_name in borrower['owes']:
            borrower['owes'][lender_name] += amount
        else:
            borrower['owes'][lender_name] = amount
        borrower['balance'] -= amount
        return json.dumps({'users': sorted([RestAPI.recalculate(lender), RestAPI.recalculate(borrower)], key=lambda user: user['name'])}, indent=4)

    def get_user_by_name(self, name):
        return next(user for user in self.database['users'] if user['name'] == name)

    @staticmethod
    def recalculate(user):
        names = list(user['owes'].keys())
        for name in names:
            if name in user['owed_by']:
                owes = user['owes'][name]
                owned = user['owed_by'][name]
                if owes > owned:
                    user['owes'][name] -= owned
                    del user['owed_by'][name]
                elif owes < owned:
                    user['owed_by'][name] -= owes
                    del user['owes'][name] 
                else:
                    del user['owes'][name]
                    del user['owed_by'][name]
        return user
