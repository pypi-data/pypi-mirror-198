# Cascade CMS 8 REST API Python Driver

This is a module for simplifying interaction with [Hannon Hill's Cascade CMS 8 REST API](https://www.hannonhill.com/cascadecms/latest/developing-in-cascade/rest-api/index.html). This was built to handle some day-to-day task automation with Cascade CMS 8, e.g., access control management, workflow management, file naming rule enforcement, and more.

## How it Works

The driver class [CascadeCMSRestDriver](py-cascade-cms/driver.py) constructor accepts either a username and password combination or a user-specific API key (i.e., for a service account in Cascade CMS) in addition to an organization name, e.g. "cofc". From there, it uses these values to create some headers that are used in combination with the [requests](https://pypi.org/project/requests/) library to wrap requests against the Cascade CMS REST API in simple methods, like **list_sites**. The methods are based on [the API's WSDL description](https://my-org.cascadecms.com/ws/services/AssetOperationService?wsdl). (Replace my-org in the previous link with your own organization).

## Installation

To install the package, simply run:

```
pip install py-cascade-cms-api
```

## Usage

```
# import
from cascadecmsdriver.driver import CascadeCMSRestDriver

# you can provide a username and password or alternatively an api key
# verbose boolean indicates whether to use verbose logging
driver = CascadeCMSRestDriver(
    organization_name="my-org", api_key='my-api-key', verbose=True)
## driver = CascadeCMSRestDriver(
##    organization_name="my-org", username='my-username', password='my-password',
##    verbose=True)
##
sites = driver.list_sites()['sites']
for s in sites:
    asset = driver.read_asset(asset_type='site', asset_identifier=s['id'])
    driver.debug(asset)

```
