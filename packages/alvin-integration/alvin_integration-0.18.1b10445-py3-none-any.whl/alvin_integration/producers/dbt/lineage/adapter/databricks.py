from dbt.adapters.databricks.impl import DatabricksAdapter

from alvin_integration.producers.dbt.installer import AlvinDBTInstaller


class AlvinDatabricksAdapter(DatabricksAdapter):
    def __init__(self, *args, **kwargs):

        alvin_manager = AlvinDBTInstaller()

        alvin_manager.install()

        super(DatabricksAdapter, self).__init__(*args, **kwargs)
