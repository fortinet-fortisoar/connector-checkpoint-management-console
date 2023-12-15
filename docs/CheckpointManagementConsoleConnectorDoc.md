## About the connector
CheckPoint Management Console helps you to configure and view the security policy and objects in a Security Management Server or Multi Domain Server using CLI tools and web-services.
<p>This document provides information about the CheckPoint Management Console Connector, which facilitates automated interactions, with a CheckPoint Management Console server using FortiSOAR&trade; playbooks. Add the CheckPoint Management Console Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with CheckPoint Management Console.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-checkpoint-management-console</pre>

## Prerequisites to configuring the connector
- You must have the credentials of CheckPoint Management Console server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the CheckPoint Management Console server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>CheckPoint Management Console</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the server URL of the CheckPoint Management Console server to connect and perform the automated operations.
</td>
</tr><tr><td>Credentials</td><td>Select the type of credentials that you want to provide.
<br><strong>If you choose 'Username and Password'</strong><ul><li>Username: Specify the Username to access the CheckPoint Management Console server to connect and perform the automated operations.</li><li>Password: Specify the Password to access the CheckPoint Management Console server to connect and perform the automated operations.</li></ul><strong>If you choose 'API Key'</strong><ul><li>API Key: Specify the API Key to access the CheckPoint Management Console server to connect and perform the automated operations.</li></ul></td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Create Host</td><td>Creates a host based on the parameters that you have specified.</td><td>add_host <br/>Investigation</td></tr>
<tr><td>Update Host</td><td>Updates a host based on the parameters that you have specified.</td><td>update_host <br/>Investigation</td></tr>
<tr><td>Get Hosts List</td><td>Retrieves a detailed list of hosts based on the parameters that you have specified.</td><td>get_hosts_list <br/>Investigation</td></tr>
<tr><td>Get Host Details</td><td>Retrieves the host details based on the uid or name that you have specified.</td><td>get_host_details <br/>Investigation</td></tr>
<tr><td>Delete Host</td><td>Deletes an existing host object based on the name or uid that you have specified.</td><td>delete_host <br/>Investigation</td></tr>
</tbody></table>

### operation: Create Host
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Specify the host name that you want to create. The host name must be unique in the domain.
</td></tr><tr><td>IP Address</td><td>Specify the IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly.
</td></tr><tr><td>IPv4 Address</td><td>Specify the IPv4 address.
</td></tr><tr><td>IPv6 Address</td><td>Specify the IPv6 address.
</td></tr><tr><td>Interfaces</td><td>Specify the host interfaces.
</td></tr><tr><td>NAT Settings</td><td>Specify the NAT settings for the host object.
</td></tr><tr><td>Tags</td><td>Specify comma separated tags for the host object.
</td></tr><tr><td>Host Servers</td><td>Specify the host servers configuration.
</td></tr><tr><td>Set If Exists</td><td>If another object with the same identifier already exists, it will be updated. The command behaviour will be the same as if originally a set command was called. Pay attention that original object's fields will be overwritten by the fields provided in the request payload.
</td></tr><tr><td>Color</td><td>Specify the color for the host object.
</td></tr><tr><td>Comments</td><td>Specify the comments for the host object.
</td></tr><tr><td>Details Level</td><td>Specify the details level. The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.
</td></tr><tr><td>Groups</td><td>Specify the collection of group identifiers.
</td></tr><tr><td>Ignore Warnings</td><td>Specify whether to apply changes ignoring warnings.
</td></tr><tr><td>Ignore Errors</td><td>Specify whether to apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "uid": "",
    "name": "",
    "type": "",
    "groups": [],
    "interfaces": [],
    "ipv4-address": "",
    "ipv6-address": "",
    "nat-settings": "",
    "tags": [],
    "host-servers": "",
    "color": "",
    "comments": "",
    "domain": {
        "uid": "",
        "name": "",
        "domain-type": ""
    },
    "icon": "",
    "meta-info": "",
    "read-only": "",
    "available-actions": ""
}</pre>
### operation: Update Host
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Based On</td><td>Select the type of parameter that you want to provide.
<br><strong>If you choose 'UID'</strong><ul><li>UID: Specify the host UID to update the host.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the host name to update the host.</li></ul></td></tr><tr><td>Interfaces</td><td>Specify the host interfaces.
</td></tr><tr><td>IP Address</td><td>Specify the IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly.
</td></tr><tr><td>IPv4 Address</td><td>Specify the IPv4 address.
</td></tr><tr><td>IPv6 Address</td><td>Specify the IPv6 address.
</td></tr><tr><td>NAT Settings</td><td>Specify the NAT settings for the host object.
</td></tr><tr><td>New Name</td><td>Specify the new name for the host object.
</td></tr><tr><td>Tags</td><td>Specify comma separated tags for the host object.
</td></tr><tr><td>Host Servers</td><td>Specify the host servers configuration.
</td></tr><tr><td>Color</td><td>Specify the color for the host object.
</td></tr><tr><td>Comments</td><td>Specify the comments for the host object.
</td></tr><tr><td>Details Level</td><td>Specify the details level. The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.
</td></tr><tr><td>Groups</td><td>Specify the collection of group identifiers.
</td></tr><tr><td>Ignore Warnings</td><td>Specify whether to apply changes ignoring warnings.
</td></tr><tr><td>Ignore Errors</td><td>Specify whether to apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "uid": "",
    "name": "",
    "type": "",
    "groups": [],
    "interfaces": [],
    "ipv4-address": "",
    "ipv6-address": "",
    "nat-settings": "",
    "tags": [],
    "host-servers": "",
    "color": "",
    "comments": "",
    "domain": {
        "uid": "",
        "name": "",
        "domain-type": ""
    },
    "icon": "",
    "meta-info": "",
    "read-only": "",
    "available-actions": ""
}</pre>
### operation: Get Hosts List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter</td><td>Specify the search expression to filter objects. The provided text should be exactly the same as it would be given in SmartConsole Object Explorer. The logical operators in the expression ('AND', 'OR') should be provided in capital letters. The search involves both a IP search and a textual search in name, comment, tags etc.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of objects that should be returned. The value should be between 1 to 500. Default value is 50.
</td></tr><tr><td>Offset</td><td>Specify the offset, i.e. the number of results to skip initially. Default value is 0.
</td></tr><tr><td>Order</td><td>Specify the order, it sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order.
</td></tr><tr><td>Show Membership</td><td>Indicates whether to calculate and show 'groups' field for every object in reply.
</td></tr><tr><td>Details Level</td><td>Specify the details level. The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.
<br><strong>If you choose 'UID'</strong><ul><li>Domains To Process: Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true.</li></ul><strong>If you choose 'Standard'</strong><ul><li>Domains To Process: Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "from": "",
    "to": "",
    "total": "",
    "objects": [
        {
            "uid": "",
            "name": "",
            "type": "",
            "domain": {
                "uid": "",
                "name": "",
                "domain-type": ""
            },
            "icon": "",
            "color": "",
            "ipv4-address": "",
            "ipv6-address": ""
        }
    ]
}</pre>
### operation: Get Host Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Based On</td><td>Select the type of parameter that you want to provide.
<br><strong>If you choose 'UID'</strong><ul><li>UID: Specify the host UID to retrieve the host's details.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the host name to retrieve the host's details.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "uid": "",
    "name": "",
    "type": "",
    "groups": [],
    "interfaces": [],
    "ipv4-address": "",
    "ipv6-address": "",
    "nat-settings": "",
    "tags": [],
    "host-servers": "",
    "color": "",
    "comments": "",
    "domain": {
        "uid": "",
        "name": "",
        "domain-type": ""
    },
    "icon": "",
    "meta-info": "",
    "read-only": "",
    "available-actions": ""
}</pre>
### operation: Delete Host
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Based On</td><td>Select the type of parameter that you want to provide.
<br><strong>If you choose 'UID'</strong><ul><li>UID: Specify the host UID to delete the host.</li></ul><strong>If you choose 'Name'</strong><ul><li>Name: Specify the host name to delete the host.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "message": "",
    "warnings": [],
    "errors": [],
    "blocking-errors": [],
    "code": ""
}</pre>
## Included playbooks
The `Sample - checkpoint-management-console - 1.0.0` playbook collection comes bundled with the CheckPoint Management Console connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the CheckPoint Management Console connector.

- Create Host
- Update Host
- Get Hosts List
- Get Host Details
- Delete Host

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
