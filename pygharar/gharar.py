from typing import List

from .http_base import HttpProxy
from .adaptors import Room, User


class Gharar(HttpProxy):
    def create_room(self, name, is_private: bool = True, *args, **kwargs) -> Room:
        response = self.post(
            path="/api/v1/service/rooms/",
            data=dict(name=name, is_private=is_private, *args, **kwargs),
        ).json()
        return Room(response)

    def get_rooms_list(self) -> List[Room]:
        response = self.get(path="/api/v1/service/rooms/").json()
        return [Room(room) for room in response]

    def update_room(self, room_address, name: str, is_private, *args, **kwargs) -> Room:
        response = self.put(
            path=f"/api/v1/service/rooms/{room_address}/",
            data=dict(name=name, is_private=is_private, *args, **kwargs),
        ).json()
        return Room(response)

    def get_room(self, room_address) -> Room:
        response = self.get(path=f"/api/v1/service/rooms/{room_address}/").json()
        return Room(response)

    def delete_room(self, room_address) -> bool:
        return self.delete(path=f"/api/v1/service/rooms/{room_address}/").ok

    def get_room_users(self, room_address) -> List[User]:
        response = self.get(path=f"/api/v1/service/rooms/{room_address}/users/").json()
        return [User(user) for user in response]

    def add_user_to_room(self, room_address, phone_number, is_admin: bool = False) -> User:
        response = self.post(
            path=f"/api/v1/service/rooms/{room_address}/users/",
            data=dict(phone=phone_number, is_admin=is_admin),
        ).json()
        return User(response)

    def get_room_user_details(self, room_address, phone_number) -> User:
        response = self.get(
            path=f"/api/v1/service/rooms/{room_address}/users/{phone_number}/"
        ).json()
        return User(response)

    def update_room_user(self, room_address, phone_number, is_admin, *args, **kwargs) -> User:
        response = self.put(
            path=f"/api/v1/service/rooms/{room_address}/users/{phone_number}/",
            data=dict(phone=phone_number, is_admin=is_admin, *args, **kwargs),
        ).json()
        return User(response)

    def delete_user_from_room(self, room_address, phone_number) -> bool:
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
