# Gharar Python Client

This is a python adaptor for interact with 
[Gharar](https://http://gharar.ir) service.

# Installation

You can easily install the package via command line below:

```commandline
pip install pygharar
```

# Usage

```python
In[1]: from pygharar import Gharar

In[2]: my_gharar = Gharar(
    service_url="https://gharar.ir/",
    authorization_token="PUT YOUR OWN TOKEN HERE", 
    max_retry=3
)

In[3]: my_gharar.create_room(name="yazdan", is_private=True)
Out[3]:
{'name': 'yazdan',
 'address': '6bedda4b-80ce-4f17-bec9-204709964161',
 'is_private': True,
 'has_live': False,
 'live_address': None,
 'is_beta_enabled': False,
 'live_stream_url': None,
 'is_active': True,
 'record_enabled': False,
 'transcription_enabled': False,
 'auto_record': False,
 'incoming_call_enabled': False,
 'call_pin': '74761137'}

In[4]: my_gharar.create_room(name="sobhan", is_private=False)
Out[4]:
{'name': 'sobhan',
 'address': '8f297726-fa6c-4246-a1de-8a96b3cf589d',
 'is_private': False,
 'has_live': False,
 'live_address': None,
 'is_beta_enabled': False,
 'live_stream_url': None,
 'is_active': True,
 'record_enabled': False,
 'transcription_enabled': False,
 'auto_record': False,
 'incoming_call_enabled': False,
 'call_pin': '56177610'}

In[5]: my_gharar.get_rooms_list()
Out[5]:
[{'name': 'yazdan',
  'address': '6bedda4b-80ce-4f17-bec9-204709964161',
  'is_private': True,
  'has_live': False,
  'live_address': None,
  'is_beta_enabled': False,
  'live_stream_url': None,
  'is_active': True,
  'record_enabled': False,
  'transcription_enabled': False,
  'auto_record': False,
  'incoming_call_enabled': False,
  'call_pin': '74761137'},
 {'name': 'sobhan',
  'address': '8f297726-fa6c-4246-a1de-8a96b3cf589d',
  'is_private': False,
  'has_live': False,
  'live_address': None,
  'is_beta_enabled': False,
  'live_stream_url': None,
  'is_active': True,
  'record_enabled': False,
  'transcription_enabled': False,
  'auto_record': False,
  'incoming_call_enabled': False,
  'call_pin': '56177610'}]

In[6]: my_gharar.update_room(
    room_address="6bedda4b-80ce-4f17-bec9-204709964161",
    name="yazdan-edited", 
    is_private=False, 
    is_active=False
)
Out[6]:
{'name': 'yazdan-edited',
 'address': '6bedda4b-80ce-4f17-bec9-204709964161',
 'is_private': False,
 'has_live': False,
 'live_address': None,
 'is_beta_enabled': False,
 'live_stream_url': None,
 'is_active': False,
 'record_enabled': False,
 'transcription_enabled': False,
 'auto_record': False,
 'incoming_call_enabled': False,
 'call_pin': '74761137'}

In[7]: my_gharar.update_room(
    room_address="6bedda4b-80ce-4f17-bec9-204709964161",
    name="yazdan", 
    is_private=True, 
    is_active=True,
    record_enabled=True
)
Out[7]:
{'name': 'yazdan',
 'address': '6bedda4b-80ce-4f17-bec9-204709964161',
 'is_private': True,
 'has_live': False,
 'live_address': None,
 'is_beta_enabled': False,
 'live_stream_url': None,
 'is_active': True,
 'record_enabled': True,
 'transcription_enabled': False,
 'auto_record': False,
 'incoming_call_enabled': False,
 'call_pin': '74761137'}

In[8]: my_gharar.get_room(room_address="8f297726-fa6c-4246-a1de-8a96b3cf589d")
Out[8]:
{'name': 'sobhan',
 'address': '8f297726-fa6c-4246-a1de-8a96b3cf589d',
 'is_private': False,
 'has_live': False,
 'live_address': None,
 'is_beta_enabled': False,
 'live_stream_url': None,
 'is_active': True,
 'record_enabled': False,
 'transcription_enabled': False,
 'auto_record': False,
 'incoming_call_enabled': False,
 'call_pin': '56177610'}

In[9]: my_gharar.delete_room(room_address="8f297726-fa6c-4246-a1de-8a96b3cf589d")
Out[9]: True

In[10]: my_gharar.get_rooms_list()
Out[10]:
[{'name': 'yazdan',
  'address': '6bedda4b-80ce-4f17-bec9-204709964161',
  'is_private': True,
  'has_live': False,
  'live_address': None,
  'is_beta_enabled': False,
  'live_stream_url': None,
  'is_active': True,
  'record_enabled': True,
  'transcription_enabled': False,
  'auto_record': False,
  'incoming_call_enabled': False,
  'call_pin': '74761137'}]

In[11]: my_gharar.get_room_users(room_address="6bedda4b-80ce-4f17-bec9-204709964161")
Out[11]: []

In[12]: my_gharar.add_user_to_room(
    room_address="6bedda4b-80ce-4f17-bec9-204709964161",
    phone_number="09355070766", 
    is_admin=True
)
Out[12]: {'phone': '09355070766', 'is_admin': True}

In[13]: my_gharar.add_user_to_room(
    room_address="6bedda4b-80ce-4f17-bec9-204709964161",
    phone_number="09373985131", 
    is_admin=False
)
Out[13]: {'phone': '09373985131', 'is_admin': False}

In[14]: my_gharar.get_room_users(room_address="6bedda4b-80ce-4f17-bec9-204709964161")
Out[14]:
[{'phone': '09355070766', 'name': '', 'is_admin': True},
 {'phone': '09373985131', 'name': '', 'is_admin': False}]

In[15]: my_gharar.get_room_user_details(
    room_address="6bedda4b-80ce-4f17-bec9-204709964161",
    phone_number="09355070766"
)
Out[15]: {'phone': '09355070766', 'name': '', 'is_admin': True}

In[16]: my_gharar.update_room_user(
    room_address="6bedda4b-80ce-4f17-bec9-204709964161",
    phone_number="09373985131", 
    is_admin=True
)
Out[16]: {'phone': '09373985131', 'is_admin': True}

In[17]: my_gharar.delete_user_from_room(
    room_address="6bedda4b-80ce-4f17-bec9-204709964161",
    phone_number="09355070766"
)
Out[17]: True
```
