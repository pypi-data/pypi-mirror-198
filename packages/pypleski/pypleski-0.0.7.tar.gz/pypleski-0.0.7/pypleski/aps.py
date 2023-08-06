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

r"""The aps endpoint is no longer supported in Plesk Obsidian and later. Since pypleski does currently support Plesk Obsidian only this is not considered supported.
We may implement older Packet Versions in future versions of pypleski. 

Warning: This is only a template and their is no functionality in this Module. 

Notes:
    * Not yet Supported:
        * DOWNLOAD-PACKAGE downloads an application package from the APS Catalog
        * GET-DOWNLOAD-STATUS retrieves the status of a package download task
        * IMPORT-PACKAGE imports to Plesk an application package uploaded to the server
        * GET-PACKAGES-LIST retrieves information on application packages available for installation on subscription’s main domain or subdomains
        * INSTALL installs an application on a subscription’s main domain or subdomains
        * IMPORT-CONFIG imports a custom list (configuration file) of APS Catalogs to Plesk
        * SET-PACKAGE-PROPERTIES displays or hides the package from customers and resellers when they view Applications Catalog
        * GET-PACKAGES-LIST-BY-RESELLER retrieves information on application packages installed on a reseller account
        * GET-PACKAGES-LIST-BY-WEBSPACE retrieves information on application packages installed under a subscription
    
    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-aps-catalog-and-applications.64489/
"""

from pypleski.core import PleskRequestPacket