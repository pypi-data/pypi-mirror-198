from kabaret import flow
from kabaret.flow_entities.entities import Entity, Property

from .maputils import SimpleCreateAction
from ..utils.kabaret.flow_entities.entities import EntityView


class Asset(Entity):
    """
    Defines a asset.

    Instances provide the `asset` key in their contextual
    dictionary (`settings` context).
    """

    ICON = ('icons.flow', 'asset')

    code = Property().ui(hidden=True)

    @classmethod
    def get_source_display(cls, oid):
        split = oid.split('/')
        indices = list(range(len(split) - 1, 2, -2))
        return ' · '.join([split[i] for i in reversed(indices)])
    
    def get_code(self):
        return self.code.get() or self.name()

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(
                asset=self.name(),
                asset_code=self.get_code()
            )


class AssetCollection(EntityView):
    """
    Defines a collection of assets.
    """

    ICON = ('icons.flow', 'asset')

    add_asset = flow.Child(SimpleCreateAction)
    
    @classmethod
    def mapped_type(cls):
        return flow.injection.injectable(Asset)
    
    def collection_name(self):
        mgr = self.root().project().get_entity_manager()
        return mgr.get_asset_collection().collection_name()


class AssetFamily(Entity):
    """
    Defines a asset family containing a list of assets.

    Instances provide the `asset_family` key in their contextual
    dictionary (`settings` context).
    """

    ICON = ('icons.flow', 'asset_family')

    assets = flow.Child(AssetCollection).injectable().ui(
        expanded=True
    )

    @classmethod
    def get_source_display(cls, oid):
        split = oid.split('/')
        indices = list(range(len(split) - 1, 2, -2))
        return ' · '.join([split[i] for i in reversed(indices)])

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(asset_family=self.name())


class AssetFamilyCollection(EntityView):
    """
    Defines a collection of asset families.
    """

    ICON = ('icons.flow', 'asset_family')

    add_asset_family = flow.Child(SimpleCreateAction)
    
    @classmethod
    def mapped_type(cls):
        return flow.injection.injectable(AssetFamily)
    
    def collection_name(self):
        mgr = self.root().project().get_entity_manager()
        return mgr.get_asset_family_collection().collection_name()


class AssetType(Entity):
    """
    Defines a asset type containing a list of asset families.

    Instances provide the `asset_type` key in their contextual
    dictionary (`settings` context).
    """

    ICON = ('icons.flow', 'asset_family')

    asset_families = flow.Child(AssetFamilyCollection).injectable()

    @classmethod
    def get_source_display(cls, oid):
        split = oid.split('/')
        indices = list(range(len(split) - 1, 2, -2))
        return ' · '.join([split[i] for i in reversed(indices)])

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(asset_type=self.name())


class AssetTypeCollection(EntityView):
    """
    Defines a collection of asset types.
    """

    ICON = ('icons.flow', 'bank')

    add_asset_type = flow.Child(SimpleCreateAction)
    
    @classmethod
    def mapped_type(cls):
        return flow.injection.injectable(AssetType)
    
    def collection_name(self):
        mgr = self.root().project().get_entity_manager()
        return mgr.get_asset_type_collection().collection_name()
