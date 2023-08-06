# pypleski 0.0.7 - under development

Pypleski (Pythonic Plesk Interface) is a collection of functions and classes that aim to ease the use of the Plesk XML API. The most important classes being PleskRequestPacket and PleskResponsePacket which are designed to represent the Request and Response Packets defined by Plesk.


### Bugfixes:
* Fixed the Filter bug in get and delete related functions
    of the database and the customer module
    

### Changes:
* Merged PyPleskiApiClient with PleskApiClient.
* New Documentation is online: https://pypleski.codingcow.de
* Removed the Managers entirely
* Removed the 'Meta' classes from all modules.
* PleskApiClient


### Added Modules
* Webhosting
* Mail


# TODO
### Core Imporvements:
* Implement Logging in Api Client Classes
* Clean up Api Client Classes
* Review all Modules
* Improve the Docs

### Planned Modules:
* reseller
* reseller_plan
* webspace
* service_plan
* service_plan_addon

#  Managers module deprecated.

The managers module was removed with version 0.0.5.

Use the PleskApiClient Class's request method to retrieve in conjunction with the several plypleski modules functions.

We moved away from building ManagerClasses and instead provide a functions based approach

this allows usage like this and makes managers obsolete
```
python
from pypleski.core import PleskApiClient
from pypleski.datbase import get_database

#create client object
client = PleskApiClient("localhost") 

#add your token or use set_credentials method
client.set_access_token("IamAValidTokenLOL") 

#make your request
datbase_info = client.request(get_database("webspace-name", "domain.name"))

#print out the response
print(database_info)
```

See https://pypleski.codingcow.de to read the docs.
