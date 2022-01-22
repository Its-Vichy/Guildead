import requests, uuid, random, string

class Exploit:
    def blank_message():
        return [random.choice(string.ascii_letters + string.ascii_uppercase + string.digits) for _ in range(random.randint(1000, 1000))]

class Guilded:
    def __init__(self, proxy: str= None):
        self.base_url = "https://www.guilded.gg/api"
        self.session = requests.Session()
        self.session.proxies = {"http": proxy, "https": proxy} if proxy else None

    def login(self, email: str, password: str):
        r = self.session.post(f'{self.base_url}/login', json={'email': email, 'password': password})
        return (False, {'error': 'Email or password is incorrect.'}) if 'Email or password is incorrect.' in r.text in r.text else (True, {'mid': r.cookies.get('guilded_mid'), 'hmac_signed_session': r.cookies.get('hmac_signed_session')})
    
    def send_message(self, channel_id: str, message: str, confirmed: bool= False, isSilent: bool= False, isPrivate: bool= False, repliesTo: list= []):
        r = self.session.post(f'{self.base_url}/channels/{channel_id}/messages', json={
            "messageId": str(uuid.uuid1()),
            "content": {
                "object": "value",
                "document": {
                    "object": "document",
                    "data": {},
                    "nodes": [
                        {
                            "object": "block",
                            "type": "paragraph",
                            "data": {},
                            "nodes": [
                                {
                                    "object": "text",
                                    "leaves": [
                                        {
                                            "object": "leaf",
                                            "text": message,
                                            "marks": []
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            },
            "repliesToIds": repliesTo,
            "confirmed": confirmed,
            "isSilent": isSilent,
            "isPrivate": isPrivate
        })
        return r.json()
    
    def edit_message(self, channel_id: str, message_id: str, message: str, confirmed: bool= False, isSilent: bool= False, isPrivate: bool= False, repliesTo: list= []):
        r = self.session.put(f'{self.base_url}/channels/{channel_id}/messages/{message_id}', json={
            "messageId": message_id,
            "content": {
                "object": "value",
                "document": {
                    "object": "document",
                    "data": {},
                    "nodes": [
                        {
                            "object": "block",
                            "type": "paragraph",
                            "data": {},
                            "nodes": [
                                {
                                    "object": "text",
                                    "leaves": [
                                        {
                                            "object": "leaf",
                                            "text": message,
                                            "marks": []
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            },
            "repliesToIds": repliesTo,
            "confirmed": confirmed,
            "isSilent": isSilent,
            "isPrivate": isPrivate
        })
        return r.json()
    
    def delete_message(self, channel_id: str, message_id: str):
        r = self.session.delete(f'{self.base_url}/channels/{channel_id}/messages/{message_id}')
        return r.json()
