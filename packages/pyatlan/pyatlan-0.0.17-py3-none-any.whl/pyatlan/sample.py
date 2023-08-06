from pyatlan.client.atlan import AtlanClient
from pyatlan.cache.custom_metadata_cache import CustomMetadataCache
from pyatlan.model.assets import Table

client = AtlanClient()
# table = client.get_asset_by_guid(asset_type=Table, guid="ed16927a-35e6-4f47-b9d6-1652f7252970")
table = Table.create_for_modification(  # (1)
    qualified_name="default/snowflake/1652725837/ATLAN_SAMPLE_DATA/FOOD_BEVERAGE/SALES_MKT_EXPENSES",
    name="SALES_MKT_EXPENSES",
)
monte_carlo = table.get_business_attributes("Monte Carlo")
monte_carlo.freshness_date = 1679518800000
table.set_business_attribute(monte_carlo)
# table.description = None # (2)
response = client.upsert(table, replace_custom_metadata=True)  # (3)
assert 1 == len(response.assets_updated(asset_type=Table))  # (4)
name = "Monte Carlo"
ba_id = CustomMetadataCache.get_id_for_name(name)
type_name = "Table"
for a_type in CustomMetadataCache.types_by_asset[type_name]:
    if hasattr(a_type, "_meta_data_type_name") and a_type._meta_data_type_name == name:
        break
else:
    raise ValueError(f"Business attributes {name} are not applicable to {type_name}")
ba_type = CustomMetadataCache.get_type_for_id(ba_id)
if not ba_type:
    raise ValueError(f"Business attributes {name} are not applicable to {type_name}")
m = ba_type()
pass
