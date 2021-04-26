from .http_base import HttpProxy


class Gharar(HttpProxy):
    def create_room(self, name, is_private: bool = True, *args, **kwargs):
        return self.post(
            path="/api/v1/service/rooms/",
            data=dict(name=name, is_private=is_private, *args, **kwargs),
        ).json()

    def get_rooms_list(self):
        return self.get(path="/api/v1/service/rooms/").json()

    def update_room(self, room_address, name: str, is_private, *args, **kwargs):
        return self.put(
            path=f"/api/v1/service/rooms/{room_address}/",
            data=dict(name=name, is_private=is_private, *args, **kwargs),
        ).json()

    def get_room(self, room_address):
        return self.get(path=f"/api/v1/service/rooms/{room_address}/").json()

    def delete_room(self, room_address):
        return self.delete(path=f"/api/v1/service/rooms/{room_address}/").ok

    def get_room_users(self, room_address):
        return self.get(path=f"/api/v1/service/rooms/{room_address}/users/").json()

    def add_user_to_room(self, room_address, phone_number, is_admin: bool = False):
        return self.post(
            path=f"/api/v1/service/rooms/{room_address}/users/",
            data=dict(phone=phone_number, is_admin=is_admin),
        ).json()

    def get_room_user_details(self, room_address, phone_number):
        return self.get(
            path=f"/api/v1/service/rooms/{room_address}/users/{phone_number}/"
        ).json()

    def update_room_user(self, room_address, phone_number, is_admin: bool, *args, **kwargs):
        return self.put(
            path=f"/api/v1/service/rooms/{room_address}/users/{phone_number}/",
            data=dict(phone=phone_number, is_admin=is_admin, *args, **kwargs),
        ).json()

    def delete_user_from_room(self, room_address, phone_number):
        return self.delete(
            path=f"/api/v1/service/rooms/{room_address}/users/{phone_number}/"
        ).ok

    def get_room_status(self, room_address):
        return self.get(path=f"/api/v1/service/rooms/{room_address}/usage-stats/").json()

    def get_room_records(self, room_address):
        return self.get(path=f"/api/v1/service/rooms/{room_address}/recordings/").json()

    def remove_record(self, room_address, record_name):
        return self.delete(
            path=f"/api/v1/service/rooms/{room_address}/recordings/{record_name}/"
        ).ok
