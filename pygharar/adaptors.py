class Room(object):
    def __init__(self, response):
        self.response = response

    def name(self):
        return self.response["name"]

    def address(self):
        return self.response["address"]

    def is_private(self):
        return self.response["is_private"]

    def has_live(self):
        return self.response["has_live"]

    def live_address(self):
        return self.response["live_address"]

    def is_beta_enabled(self):
        return self.response["is_beta_enabled"]

    def live_stream_url(self):
        return self.response["live_stream_url"]

    def is_active(self):
        return self.response["is_active"]

    def record_enabled(self):
        return self.response["record_enabled"]

    def transcription_enabled(self):
        return self.response["transcription_enabled"]

    def auto_record(self):
        return self.response["auto_record"]

    def incoming_call_enabled(self):
        return self.response["incoming_call_enabled"]

    def call_pin(self):
        return self.response["call_pin"]

    def link(self):
        return f"https://room.gharar.ir/{self.address()}"


class User(object):
    def __init__(self, response):
        self.response = response

    def phone(self):
        return self.response["phone"]

    def name(self):
        return self.response["name"]

    def is_admin(self):
        return self.response["is_admin"]
