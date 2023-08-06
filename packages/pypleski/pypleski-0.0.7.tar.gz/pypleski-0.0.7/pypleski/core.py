# Copyright (C) 2023  Uli Toll
# 
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.


r"""The Core Module contains the Base Classes for all Modules and Plesk Packets as well as the API Client Classes.

Notes:
    * Changes 0.0.7: 
        * PyPleskiApiClient was merged with PleskApiClient
        * Added some basic logging to PleskApiClient


Examples::

    from pypleski.core import PleskApiClient, PleskRequestPacket

    # Setup the PleskApiClient
    client = PleskApiClient('localhost')
    client.set_credentials("alvin","super_secret_password")
    
    # Prepare a Request Packet with PleskRequestPacket 
    request = PleskRequestPacket(
        "server", 
        "create_session", 
        login='alvin',
        data={
            'user_ip':127.0.0.1,
             'source_server':'',
             })

    # Make the Request and retrive it as PleskResponsPacket
    response = api.request(request)    

    # Print out your access token
    print(response.to_dict()['packet']['server']['create_session']['result']['id'])    


    # You will not have to write as much when you use the other fun modules in this package.
    from pypleski.core import PleskApiClient
    from pypleski.server import get_session_token

    # Setup the PleskApiClient
    client = PleskApiClient('localhost')
    client.set_credentials("alvin","super_secret_password")

    # Make the Request and retrieve it as PleskResponsPacket
    response = client.request(get_session_token("alvin", '127.0.0.1'))

    print(response.to_dict()['packet']['server']['create_session']['result']['id'])    

"""

import http.client
import ssl
from contextlib import contextmanager
from typing import Protocol
import xml.etree.ElementTree as ET
import json
import xmltodict
import logging

### Since Python would recognise '-' in a variable name as an operator between two vars we need a way to allow for conversion from 
### keyword variables like ip_address to the actual tag name ip-address. Some tags use _ instead of - and we don't want to correct those
### there are more tagse using - as tags using _ in their names, we catalouged the ones using _ to check if the _ can should be replaced with - or not (PleskRequestPacket).

#TODO# There might still be a trap as we don't know yet, is some tags are with both - and _ in their names. 
# Also the reference documents on plesks website seem to have spark confusion over the use of - and _ in some examples

UNDERSCORED_TAGS = {
    "1.6.9.1": ['admin_locale', 'trial_license', 'add_master_server', 'max_button_length', 'admin_phone', 'admin_pcode', 'include_remote_databases', 'admin_cname', 'outgoing_email_mode_explicit_ipv6', 'services_state', 'pop3_imap_out', 'additional_key', 'smtp_out', 'admin_state', 'get_events', 'initial_setup', 'admin_city', 'gen_info', 'max_connections_per_ip', 'remove_from_acl', 'smtp_use_default_settings', 'outgoing_messages_mbox_limit', 'smtp_allow_users', 'get_additional_key', 'get_prefs', 'add_rec', 'admin_email', 'is_visible', 'outgoing_messages_subscription_limit', 'traffic_accounting', 'set_misc', 'logo_img_ref', 'vrt_hst', 'smtp_login', 'get_protos', 'get_traffic', 'frm_fwd', 'login_timeout', 'new_name', 'mail_notifications', 'smtp_password', 'admin_pname', 'c_phone', 'back_url', 'std_fwd', 'smtp_host', 'get_info', 'lic_get_info', 'get_rec', 'notification_period', 'certificate_name', 'outgoing_email_mode', 'renew_additional_key', 'srv_man', 'user_ip', 'since_date', 'cform_buttons_list', 'secret_key', 'lic_install', 'zone_type', 'outgoing_antispam', 'starting_url', 'smtp_in', 'global_settings_not_set', 'dns_zone_type', 'admin_country', 'gen_setup', 'dom_name', 'get_acl', 'public_ip_address', 'add_to_acl', 'del_rec', 'dest_url', 'session_setup', 'event_log', 'restart_apache_interval', 'ip_address', 'content_type', 'dom_id', 'outgoing_email_mode_explicit_ipv4', 'smtp_port', 'get_misc', 'create_session', 'report_period', 'admin_multiple_sessions', 'set_traffic', 'del_master_server', 'cl_id', 'del_misc', 'locale_id', 'pop3_imap_in', 'server_name', 'admin_address', 'stat_ttl', 'disable_lock_screen', 'max_connections', 'ftp_over_ssl', 'ftp_pass', 'domain_name', 'is_uploaded', 'aps_force_updates', 'source_server', 'c_email', 'preview_protection', 'sort_key', 'aps_suggest_updates', 'to_date', 'end_date', 'disk_usage', 'send_announce', 'get_master_server', 'db_server', 'outgoing_messages_domain_limit', 'flush_selected_range', 'enable_sendmail', 'lic_update', 'ftp_user', 'logo_img_url', 'set_prefs', 'remove_additional_key', 'http_code', 'admin_fax', 'smtp_tls', 'apache_pipelog'], 
    "1.6.9.0": ['get_additional_key', 'remove_from_acl', 'set_traffic', 'get_events', 'disk_usage', 'content_type', 'enable_sendmail', 'cl_id', 'starting_url', 'migration_id', 'certificate_name', 'pop3_imap_in', 'outgoing_messages_domain_limit', 'lic_update', 'std_fwd', 'dom_name', 'smtp_host', 'smtp_port', 'get_misc', 'apache_pipelog', 'set_prefs', 'logo_img_ref', 'smtp_login', 'dest_url', 'admin_cname', 'admin_pcode', 'create_session', 'since_date', 'preview_protection', 'get_info', 'ip_address', 'aps_force_updates', 'zone_type', 'get_master_server', 'vrt_hst', 'admin_multiple_sessions', 'get_fs', 'login_timeout', 'restart_apache_interval', 'server_name', 'admin_locale', 'max_connections_per_ip', 'outgoing_antispam', 'event_log', 'db_server', 'admin_state', 'del_master_server', 'http_code', 'dns_zone_type', 'outgoing_messages_subscription_limit', 'admin_fax', 'add_master_server', 'secret_key', 'smtp_allow_users', 'admin_city', 'smtp_use_default_settings', 'lic_get_info', 'smtp_out', 'max_button_length', 'add_to_acl', 'source_server', 'get_protos', 'admin_phone', 'end_date', 'sort_key', 'gen_info', 'get_rec', 'flush_selected_range', 'logo_img_url', 'disable_lock_screen', 'ftp_pass', 'frm_fwd', 'aps_suggest_updates', 'services_state', 'public_ip_address', 'smtp_in', 'renew_additional_key', 'cform_buttons_list', 'add_rec', 'outgoing_email_mode_explicit_ipv4', 'get_acl', 'additional_key', 'domain_name', 'del_rec', 'is_visible', 'report_period', 'dom_id', 'outgoing_email_mode', 'del_misc', 'admin_country', 'stat_ttl', 'admin_address', 'srv_man', 'back_url', 'ftp_user', 'admin_email', 'send_announce', 'user_ip', 'notification_period', 'set_misc', 'c_email', 'session_setup', 'max_connections', 'get_prefs', 'to_date', 'get_status', 'new_name', 'smtp_tls', 'remove_additional_key', 'is_uploaded', 'gen_setup', 'get_traffic', 'ftp_over_ssl', 'pop3_imap_out', 'initial_setup', 'smtp_password', 'include_remote_databases', 'locale_id', 'global_settings_not_set', 'traffic_accounting', 'mail_notifications', 'admin_pname', 'lic_install', 'c_phone', 'outgoing_messages_mbox_limit', 'outgoing_email_mode_explicit_ipv6'], 
    "1.6.8.0": ['get_protos', 'max_button_length', 'smtp_login', 'get_rec', 'pop3_imap_out', 'ftp_pass', 'srv_man', 'flush_selected_range', 'global_settings_not_set', 'get_additional_key', 'disk_usage', 'smtp_tls', 'add_rec', 'smtp_in', 'back_url', 'zone_type', 'initial_setup', 'mail_notifications', 'ip_address', 'restart_apache_interval', 'create_session', 'outgoing_email_mode_explicit_ipv6', 'cl_id', 'get_prefs', 'frm_fwd', 'logo_img_ref', 'get_fs', 'smtp_use_default_settings', 'ftp_user', 'content_type', 'outgoing_email_mode_explicit_ipv4', 'admin_locale', 'admin_address', 'get_info', 'smtp_out', 'admin_fax', 'certificate_name', 'del_misc', 'to_date', 'max_connections_per_ip', 'admin_state', 'traffic_accounting', 'del_master_server', 'remove_additional_key', 'del_rec', 'admin_email', 'disable_lock_screen', 'lic_update', 'set_traffic', 'dest_url', 'smtp_password', 'ftp_over_ssl', 'include_remote_databases', 'get_misc', 'admin_pcode', 'domain_name', 'aps_force_updates', 'new_name', 'http_code', 'smtp_host', 'std_fwd', 'public_ip_address', 'set_prefs', 'c_phone', 'admin_city', 'enable_sendmail', 'pop3_imap_in', 'dom_name', 'smtp_port', 'report_period', 'vrt_hst', 'admin_country', 'gen_info', 'outgoing_antispam', 'outgoing_messages_mbox_limit', 'remove_from_acl', 'migration_id', 'dns_zone_type', 'gen_setup', 'admin_pname', 'add_master_server', 'event_log', 'outgoing_messages_domain_limit', 'sort_key', 'smtp_allow_users', 'source_server', 'max_connections', 'user_ip', 'lic_install', 'stat_ttl', 'apache_pipelog', 'set_misc', 'outgoing_email_mode', 'locale_id', 'services_state', 'login_timeout', 'aps_suggest_updates', 'is_visible', 'lic_get_info', 'outgoing_messages_subscription_limit', 'get_status', 'get_acl', 'dom_id', 'logo_img_url', 'get_traffic', 'secret_key', 'end_date', 'notification_period', 'admin_cname', 'server_name', 'get_events', 'session_setup', 'admin_phone', 'send_announce', 'starting_url', 'add_to_acl', 'c_email', 'admin_multiple_sessions', 'preview_protection', 'additional_key', 'cform_buttons_list', 'is_uploaded', 'get_master_server', 'since_date', 'db_server', 'renew_additional_key'],
    "1.6.7.0": ['logo_img_url', 'get_status', 'c_email', 'set_prefs', 'back_url', 'dns_zone_type', 'max_button_length', 'ftp_over_ssl', 'admin_state', 'lic_install', 'restart_apache_interval', 'enable_sendmail', 'del_rec', 'admin_address', 'disable_lock_screen', 'is_visible', 'admin_email', 'ip_address', 'dom_id', 'add_to_acl', 'session_setup', 'global_settings_not_set', 'outgoing_email_mode_explicit_ipv4', 'logo_img_ref', 'db_server', 'preview_protection', 'login_timeout', 'cl_id', 'outgoing_messages_domain_limit', 'get_events', 'ftp_pass', 'smtp_login', 'outgoing_email_mode', 'get_additional_key', 'smtp_host', 'lic_get_info', 'lic_update', 'zone_type', 'admin_city', 'admin_cname', 'create_session', 'frm_fwd', 'aps_suggest_updates', 'smtp_use_default_settings', 'gen_info', 'content_type', 'smtp_password', 'apache_pipelog', 'smtp_in', 'to_date', 'srv_man', 'add_rec', 'aps_force_updates', 'get_protos', 'certificate_name', 'c_phone', 'secret_key', 'std_fwd', 'additional_key', 'remove_additional_key', 'send_announce', 'ftp_user', 'get_traffic', 'del_misc', 'get_acl', 'domain_name', 'include_remote_databases', 'dom_name', 'smtp_allow_users', 'traffic_accounting', 'new_name', 'notification_period', 'get_info', 'mail_notifications', 'smtp_port', 'get_fs', 'set_misc', 'since_date', 'dest_url', 'services_state', 'is_uploaded', 'migration_id', 'cform_buttons_list', 'starting_url', 'remove_from_acl', 'smtp_tls', 'get_master_server', 'get_rec', 'outgoing_messages_subscription_limit', 'report_period', 'disk_usage', 'http_code', 'set_traffic', 'source_server', 'vrt_hst', 'smtp_out', 'admin_phone', 'add_master_server', 'outgoing_messages_mbox_limit', 'get_misc', 'locale_id', 'pop3_imap_in', 'admin_pcode', 'event_log', 'outgoing_email_mode_explicit_ipv6', 'end_date', 'admin_fax', 'admin_country', 'admin_pname', 'server_name', 'max_connections_per_ip', 'outgoing_antispam', 'user_ip', 'sort_key', 'del_master_server', 'get_prefs', 'pop3_imap_out', 'renew_additional_key', 'initial_setup', 'public_ip_address', 'flush_selected_range', 'stat_ttl', 'gen_setup', 'max_connections']
    }

class PleskResponsePacket():
    """ PleskResponsePacket(response_xml) 
    
Stores Response Packets and converts them into different formats

Args:
    response_xml (string): Takes the response string from PleskClient.request()

Methods: 
    to_dict() : Returns the Response as a dictionary
    to_JSON() : Returns the Response as JSON formatted string
    to_list() : Returns the Response as a list
    to_string() : Returns the Response as XML string
    as_xml_etree_element() : Returns the Response as XML tree element        
    is_error() : Returns True if the ResponsePacket contains an Error Response 
    
    """
    _is_error = True
    _errcode = []

    def __init__(self, response_xml:str) -> None:
        """ PleskResponsePacket(response_xml) 
    
Stores Response Packets and converts them into different formats

Args:
    response_xml (string): Takes the response string from PleskClient.request()

Methods: 
    to_dict() : Returns the Response as a dictionary
    to_JSON() : Returns the Response as JSON formatted string
    to_list() : Returns the Response as a list
    to_string() : Returns the Response as XML string
    as_xml_etree_element() : Returns the Response as XML tree element        
    is_error() : Returns True if the ResponsePacket contains an Error Response     
    """
        self.packet = ET.fromstring(response_xml)

        self._is_error = bool(self.packet.find('.//errcode'))
        
        if self.is_error():
            self._errcode = [int(x) for x in (self.packet.find('.//errcode'))] #type: ignore

    def __str__(self) -> str:
        """Dunder Method - alias for to_JSON()

        Returns:
            str: ResponsePacket as JSON String 

        """
        return self.to_JSON()
    
    def __dict__(self)-> dict:
        """Dunder Method - alias for to_dict() method

        Returns:
            dict: ResponsePacket as dictionary

        """
        return self.to_dict()
    
    def __eq__(self, o: object):
        """Dunder Method to support the == operator

        Returns:
            bool: Returns True if o.__str__ is equal to self.__str__

        """
        if type(object) is not PleskResponsePacket:
            return False
        return o.__str__() == self.__str__()


    def to_JSON(self) -> str:    ### easy to use with a JSON string        
        """ 
        Returns:
            str: Response as JSON string
        """
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:    ### easy to use as dictionary
        """ 
        Returns:
            dict: Response as dict
        """
        return xmltodict.parse(self.to_string())

    def to_list(self) -> list :    ### only usefull for few responses due to its structure
        """ 
        Returns:
            list: Response as string list
        """
        return ET.tostringlist(self.packet, encoding="UTF-8")

    
    def to_string(self) -> str:    ### get the plain XML String
        """ 
        Returns:
            str: Response as XML string
        """
        return ET.tostring(self.packet, encoding="UTF-8")

    def as_xml_etree_element(self) -> ET.Element:
        """
        Returns:
            xml.etree.ElementTree.Element: The response as xml.etree.ElementTree.Element object
        """
        return self.packet
        
    def is_error(self) -> bool:    ### see if it is an error before parsing any output
        """
        Returns:
            bool: True if response contains an error
        """                              
        return self._is_error

    def get_errcode(self) -> list:
        """
        Returns:
            list(int): Returns a list of errcodes found in the response. Empty list if no errcode was found.
        """         
        return self._errcode



### TODO validation for Request Packets
### TODO update function - adapt after failed validation - to update requestpackage after version change get dict from package and rebuild it -
### TODO add support for lists i.e. ip_adresses = ['10.22.0.1', '10.20.0.1']
### TODO implement __add__ method to support + operator for adding PleskRequestPackets in a useful way (merge packet nodes)


class PleskRequestPacket():  
    """PleskRequestPacket(module:str ="webspace", operation:str = "get", **data) 

Used to craft PLESK XML API requests

Args:
    module (str, optional): _description_. Defaults to "webspace".
    operation (str, optional): _description_. Defaults to "get".
    **data: further keyword arguments

Keyword args:
    filter (dict): Example: filter = {'id':23}
    version (str): Example: version = "1.6.9.1"
    __data__ (dict): Example __data__ = {'id':23,'subscription-id':2}

    further keywords are available depending on the module and operation selected

Tipp: Use the new __data__ keyword to provide a prepared dict the __data__ keyword must be provided with an 
dict and will replace the **data (kwargs) dict after the filter keyword was processed            
    """
      
    
    def __init__(self, module:str ="webspace", operation:str = "get", **data) -> None:
        """PleskRequestPacket(module:str ="webspace", operation:str = "get", **data) 

Used to craft PLESK XML API requests

Args:
    module (str, optional): _description_. Defaults to "webspace".
    operation (str, optional): _description_. Defaults to "get".
    **data: further keyword arguments

Keyword args:
    filter (dict): Example: filter = {'id':23}
    version (str): Example: version = "1.6.9.1"
    __data__ (dict): Example __data__ = {'id':23,'subscription-id':2}

    further keywords are available depending on the module and operation selected

Tipp: Use the new __data__ keyword to provide a prepared dict the __data__ keyword must be provided with an 
dict and will replace the **data (kwargs) dict after the filter keyword was processed
    """                 
        self.packet = ET.Element('packet') # The Packet (Root) Node          
        self.module = ET.SubElement(self.packet,module) # The Module Node
        self.operation = ET.SubElement(self.module,operation) # The Operation Node                              
        self.set_packet_version()
        if ("version" in data):            
            self.packet.set("version", data["version"])  
            del data['version']          
        self._setup(**data)

    def __str__(self) -> str:
        """Dunder Method 

        Returns:
            str: The RequestPacket as XML string
        """
        return f"{self.to_string()}"
    
    def __add__(self, o:object) :
        """ NOT YET FUNCTIONAL Dunder Method to Support + Operator

        Returns:
            str: The sum of the added PleskRequestPackets as XML string
        """
        print("Operator + not yet supported by PleskRequestPacket")
        

    
    def __dict__(self) -> dict:
        """Dunder Method

        Returns:
            dict: The RequestPacket as Dictionary
        """
        return xmltodict.parse(self.to_string())

    def __eq__(self, o: object):
        if type(o) is not PleskRequestPacket:
            return False
        return o.__str__() == self.__str__()

    def _setup(self, **data):
        """ _setup function - Checks if there if the operation tag implies the use of a filter and adds it if needed 
        before adding the provided data to the operation node
            Should only be Called by __init__ 
        
        TODO: Merge with __init__
        """             
        ## This option and the __data__ keyword is used and actually contains a dict it will replace the current data object
        ## This is a weird patch that should be reviewed      
        if "__data__" in data:     
            data=data["__data__"]
        self.add_data_to_node(self.operation, **data)         

    def set_packet_version(self, version:str="1.6.7.0") -> None:
        """Sets the packet version for the request

Args:
    version (str, optional): Defaults to "1.6.7.0".
        """        
        self.packet.set("version", version)

    def add_data_to_node(self, parent, **data) -> None:           
        """Adds all data sets to the given parent Element                 

Args:
    parent (xml.etree.ElementTree.Element): The parent node to which you want to add **data. 
    **data (Any): Keywords or Dictionary containing more keywords      
        
        """
    

        
        for key, value in data.items():             
            # if key contains substring "_" replace but is not in HYPHONED_TAGS[packet version] replace it with "-"
            
            if key not in UNDERSCORED_TAGS[self.packet.get("version")]: #type: ignore
            # type: ignore                
                key = key.replace("_","-")                                            
            
            node = ET.SubElement(parent, key)           

            #recursion if we have another dict
            if type(value) == dict:
                self.add_data_to_node(node,**value) 
            else:
                node.text = f"{value}"       

    def to_string(self, encoding="unicode") -> str:
        """to_string function - returns the packet XML as a string
        Args:
            encoding (string): Set string encoding - defaults to: UTF-8
        Returns:
            str: The Plesk Response XML as string
        
        """
        return ET.tostring(self.packet,encoding=encoding, method='xml')
    


#### Add a method to check for supported packet versions

class PleskApiClient:
    """PleskApiClient(server:str, port:int=8443, use_ssl:bool = True, unverified_ssl:bool = False) 

A simple http(s) client that uses http.client and ssl           


Args:
    server (_type_): The URL to your PLESK Server
    port (int, optional): The Port PLESK is listening. Defaults to 8443.
    use_ssl (str, optional): Use SSL (https). Defaults to True.
    unverified_ssl (bool, optional): Ignore ssl errors. Defaults to False.

Methods:
    set_credentials() : Set the username and Password to use.
    set_server() : Set the Plesk Server URL.
    set_access_token() : Set the Access token to use instead of credentials. 
    set_use_ssl() : Set to True for secure connection.
    set_allow_unverified_ssl() : Set to True to allow unverfied ssl context. 
    request(request:PleskRequestPacket or str,legacy:bool=False): Returns a PleskResponsePacket 
    """
    _access_token:str = "" # will store the set access token as string
    _credentials:tuple =  ("","")# will store credentials as tuple("username","password")
    server:str = "localhost"
    port:int = 8443
    use_ssl:bool = True
    unverified_ssl:bool=False


    def __init__(self, server:str, port:int=8443, use_ssl:bool = True, unverified_ssl:bool = False):
        """PleskApiClient(server:str, port:int=8443, use_ssl:bool = True, unverified_ssl:bool = False) 

A simple http(s) client that uses http.client and ssl           


Args:
    server (_type_): The URL to your PLESK Server
    port (int, optional): The Port PLESK is listening. Defaults to 8443.
    use_ssl (str, optional): Use SSL (https). Defaults to True.
    unverified_ssl (bool, optional): Ignore ssl errors. Defaults to False.

Methods:
    set_credentials() : Set the username and Password to use.
    set_server() : Set the Plesk Server URL.
    set_access_token() : Set the Access token to use instead of credentials. 
    set_use_ssl() : Set to True for secure connection.
    set_allow_unverified_ssl() : Set to True to allow unverfied ssl context. 
    request(request:PleskRequestPacket): Returns a PleskResponsePacket 
    """
       
        self.server = server
        self.port = port
        self.use_ssl = use_ssl
        self.unverified_ssl = unverified_ssl        
    
    def __str__(self) -> str:
        """Dunder Method

        Returns:
            str: String Repre
        """
        return f"PleskApiClient@{self.server}:{self.port}"

    def set_server(self, url:str)-> None:
        """Sets the Plesk server base URL

        Args:
            url (str): The URL to your Plesk Instance
        """
        self.server = url                
        

    def set_port(self, port:int)-> None:
        """Sets the port your Plesk is listening. Default is 8443.

        Args:
            port (int): The port your Plesk is listening
        
        """
        self.port = port

    def set_use_ssl(self, use_ssl:bool) -> None:
        """Turn SSL on (True) or off (False). You want to use SSL.

        Args:
            use_ssl (bool): True turns SSL on | False turns ssl off
        """
        self.use_ssl = use_ssl

    def set_allow_unverified_ssl(self, unverified_ssl:bool) -> None:
        """Set if unverified ssl context is allowed. 

        Args:
            unverified_ssl (bool): True turns ON | False turns OFF
        """
        self.unverified_ssl = unverified_ssl    
        
    def set_credentials(self, user:str, pswd:str ) -> None:        
        """Set the credentials for PLESK

        Args:
            user (str): Your PLESK username
            pswd (str): Your PLESK password
        """
        self._credentials = (user,pswd)
        logging.info(f"Credentials for {self} changed!")

    def set_access_token(self, token:str) -> None:
        """Set an access token to use instead of your credentials

        Args:
            token (str): Your PLESK access token        
        """
        if not token:
            return
        self._access_token = token
        logging.info("Deleting credentials and using Token.")
        del self._credentials # No need to keep them in memory as we are using the token
    
    @contextmanager
    def _create_connection(self):
        """ Create a Connection to the PLESK Server                  

        Yields:
            http.client.HTTPSConnection or http.client.HTTPConnection: Returns a Connection Object
        """
        try:
            if not self.use_ssl:
                connection = http.client.HTTPConnection(self.server, self.port) # implement log warning 
                logging.warning(f"Connection to {self.server}:{self.port} not secured! All data amd credential will be send in plain text!")

            if self.unverified_ssl:
                connection = http.client.HTTPSConnection(self.server, self.port, context=ssl._create_unverified_context())
                logging.warning(f"Connection to {self.server}:{self.port} using unverified SSL context! Only use unverified_ssl = False if you trust the connection!")
            else:
                logging.info(f"Connecting to {self.server}:{self.port} using SSL.")
                connection = http.client.HTTPSConnection(self.server, self.port)  
                
            yield connection

        except Exception as e:
            logging.error(f"An Error occured while trying to connect to {self.server}:{self.port} Exception: {e}")
        finally: 
            logging.info(f"Closing Connection to {self.server}:{self.port}")
            connection.close()  #type: ignore

    
    def _header(self) -> dict:
        """ Prepares the header for the Request        

        Returns:
            dict: A dictionary containing the headers for use with the http.client's request method
        """
        header = {"Content-Type": "TEXT/XML", "HTTP_PRETTY_PRINT": "TRUE"}        
        if self._access_token: # use access token     
            header["KEY"] = self._access_token           
        else: # unpack the credentials from tuple into header dict
            header["HTTP_AUTH_LOGIN"], header["HTTP_AUTH_PASSWD"]  = self._credentials         
        return header

    def request(self, request:PleskRequestPacket) -> PleskResponsePacket:
        """ Send a Request to the set PLESK Server
        Args:
            request (PleskRequestPacket): The Request to the PLESK API as PleskRequestPacket Object

        Returns:
            PleskResponsePacket: The Response Packet as PleskResponsePacket Object
        """       
        xml = request.to_string()      
        logging.info(f"Sending request to {self} with payload: {xml}")
        with (self._create_connection()) as connection:
            data = self._get_result(connection, xml)            
            return PleskResponsePacket(data.decode("utf-8"))        

    def request_from_string(self, request:str) -> str:
        """ Send a Request to the set PLESK Server
        Args:
            request (str): The Request to the PLESK API as XML String.

        Returns:
            str: The Response as XML string
        """       

        with (self._create_connection()) as connection:
            data = self._get_result(connection, request)
            return data.decode("utf-8") #type: ignore

    def _get_result(self, connection, request) -> str:
        """Gets the result for the request on the given connection

        Args:
            connection (_type_): The connection to make the request
            request (_type_): The request.

        Returns:
            str: The result as string.
        """
        connection.request("POST", "/enterprise/control/agent.php", request, self._header())
        response = connection.getresponse()
        result = response.read()
        return result
           

class PleskApiClientDummy(PleskApiClient):
    """ PleskApiClientDummy     

        This class acts as placeholder for testing

    """
    ### Just for testing purpose
    # no real connection 

    
    def request(self, request:PleskRequestPacket, error:bool = False, **data) -> str:
        """ simulates a request and returns a positive add user operation or an webspace error

        Args:
            request (any): the Request XML When using the dummy this does nothing.
            error (bool, optional): If you need an error set to True. Defaults to False.

        Returns:
            str: An XML Response String        
        
        """
        return """<packet>
                        <webspace>
                            <get>
                                <result>
                                    <status>error</status>
                                    <errcode>1013</errcode>
                                    <errtext>Object not found.</errtext>
                                    <id>1234</id>
                                </result>
                            </get>
                        </webspace>
                    </packet>""" if error else """
                        <packet version="1.6.7.0">
                            <customer>
                                <add>
                                    <result>
                                        <status>ok</status>
                                        <id>3</id>
                                        <guid>d7914f79-d089-4db1-b506-4fac617ebd60</guid>
                                    </result>
                                </add>
                            </customer>
                        </packet>"""

# Alias PyPleskiApiClient
PyPleskiApiClient = PleskApiClient


    