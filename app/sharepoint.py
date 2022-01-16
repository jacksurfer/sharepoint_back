from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext
from .config import client_id, client_secret, site_url


client_credentials = ClientCredential(client_id, client_secret)
ctx = ClientContext(site_url).with_credentials(client_credentials)


def get_items():
    target_list = ctx.web.lists.get_by_title("requestEquipment")
    list_items = target_list.items.paged(True).top(10).get().execute_query()
    fields = list_items[0].properties.keys()
    data_list = list()
    for item in list_items:
        data_list.append(item.properties)
    dict_returned = dict()
    dict_returned['data'] = data_list
    dict_returned['keys'] = fields
    return dict_returned


def add_equipment_request(email, equip_type, equip, count, waytoship):
    target_list = ctx.web.lists.get_by_title("requestEquipment")
    target_list.add_item({
        "Title": "New Task",
        "type": equip_type,
        "equip": equip,
        "count": count,
        "wayToShip": waytoship,
        "email": email
    }).execute_query()