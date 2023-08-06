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

r"""This module's functions, generate PleskRequestPackets using the 'extension' Operator
to make calls to the Git Extension.

Notes: 

    This is not core functionality. Git is available as an extension.

    * Supported Opreations: 
        * GET retrieves information about the Git repositories on a domain or on all domains
        * CREATE adds new Git repository
        * UPDATE updates a Git repository settings
        * REMOVE removes a Git repository        
        * DEPLOY deploys changes from a Git repository to a target directory
        * FETCH fetches the remote repository for a Git repository of the Using remote Git hosting type
    
    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-git-repositories.75959/
"""
from pypleski.core import PleskRequestPacket

def get_git_repositories(domain:str="") -> PleskRequestPacket:
    """This Packet retrieves information about the present Git Repositories.

    Args:
        domain (str, optional): Only show results for this domain. Gets All if set to None. Defaults to None.

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    if domain:
        return PleskRequestPacket("extension", "call", git={'get':{'domain':domain}})
    return PleskRequestPacket("extension", "call", git={'get':''})

def create_git_repository(
        domain:str,
        name:str, 
        deployment_path:str="", 
        deployment_mode:str="", 
        remote_url:str="", 
        skip_ssl:bool=False, 
        actions:str=""
    ) -> PleskRequestPacket:
    """ 
    This Packet adds new Git repository

    Args:
        domain (str): _description_
        name (str): _description_
        deployment_path (str, optional): _description_. Defaults to None.
        deployment_mode (str, optional): _description_. Allowed Values: auto | manual | none Defaults to None.
        remote_url (str, optional): _description_. Defaults to None.
        skip_ssl (bool, optional): _description_. Defaults to False. ( remote hosts only)
        actions (str, optional): actions are shell commands delimited by “;” symbol that should be used with an escape character: “&gt;”. Defaults to None.

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    
    request = {"domain":domain, "name": name}
    if deployment_path:
        request["deployment-path"] = deployment_path
    if deployment_mode:
        request["deployment-mode"] = deployment_mode    
    if remote_url:
        request["remote-url"] = remote_url
        if skip_ssl:
            request["skip-ssl-verification"] = "true"    
    if actions:
        request["actions"] = actions

    return PleskRequestPacket("extension", "call", git={"create":request})



def update_git_repository(
        domain:str,
        name:str, 
        new_name:str="",
        deployment_path:str="", 
        deployment_mode:str="", 
        remote_url:str="", 
        skip_ssl:bool=False, 
        active_branch:str="",
        actions:str=""
    ) -> PleskRequestPacket:
    """ This Packet sets a Git repository's settings.

    Args:
        domain (str): _description_
        name (str): _description_
        new_name (str, optional): _description_. Defaults to None.
        deployment_path (str, optional): _description_. Defaults to None.
        deployment_mode (str, optional): _description_. Allowed Values: auto | manual | none Defaults to None.
        remote_url (str, optional): _description_. Defaults to None.
        skip_ssl (bool, optional): _description_. Defaults to False. ( remote url only)
        active_branch (str, optional): _description_. Defaults to None.
        actions (str, optional): _description_. Defaults to None.

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    request = {"domain":domain, "name": name}

    if new_name:
        request["new_name"] = new_name
    if deployment_path:
        request["deployment-path"] = deployment_path
    if deployment_mode:
        request["deployment-mode"] = deployment_mode    
    if remote_url:
        request["remote-url"] = remote_url
        if skip_ssl:
            request["skip-ssl-verification"] = "true"    
    if active_branch:
        request[active_branch] = active_branch
    if actions:
        request["actions"] = actions

    return PleskRequestPacket("extension", "call", git={"update":request})

def delete_git_repository(domain:str, name:str) -> PleskRequestPacket:
    """ This Packet delets the specified Git repository.

    Args:
        domain (str): _description_
        name (str): _description_

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("extension", "call", git={'remove':{'domain':domain, 'name': name}})

def deploy_git_repository(domain:str, name:str):
    """ This Packet deploys the Git repository to it's defined deploy path.

    Args:
        domain (str): _description_
        name (str): _description_

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("extension", "call", git={'deploy':{'domain':domain, 'name': name}})

def fetch_git_repository(domain:str, name:str):
    """ This Packet fetches the changes from a remote repository to a Git repository. 

    Args:
        domain (str): _description_
        name (str): _description_

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("extension", "call", git={'fetch':{'domain':domain, 'name': name}})

