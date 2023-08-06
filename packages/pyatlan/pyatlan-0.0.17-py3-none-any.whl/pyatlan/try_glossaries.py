from pyatlan.client.atlan import AtlanClient
from pyatlan.model.gen.assets import (
    AtlasGlossary,
    AtlasGlossaryCategory,
    AtlasGlossaryTerm,
)

client = AtlanClient()
for asset in client.purge_entity_by_guid("0ad65626-4f1c-4836-b964-0268c9dae3f0").assets_deleted(AtlasGlossary):
    print("Deleted: ", asset.guid)
glossary = AtlasGlossary.create("Ernest Test")
glossary.attributes.user_description("This is a description of the glossary")
glossary = client.upsert(glossary).assets_created(AtlasGlossary)[0]
category_1 = AtlasGlossaryCategory.create("Ernest Category 1", anchor=glossary)
category_1 = client.upsert(category_1).assets_created(AtlasGlossaryCategory)[0]
category_2 = AtlasGlossaryCategory.create(name="Ernest Category 2", anchor=glossary, parent_category=category_1)
category_2 = client.upsert(category_2).assets_created(AtlasGlossaryCategory)[0]
term = AtlasGlossaryTerm.create("Ernest Term", anchor=glossary, categories=[category_1, category_2])
response = client.upsert(term)
term = response.assets_created(AtlasGlossaryTerm)[0]
for category in response.assets_updated(AtlasGlossaryCategory):
    if category.guid == category_1.guid:
        category_1 = category
    elif category.guid == category_2.guid:
        category_2 = category
