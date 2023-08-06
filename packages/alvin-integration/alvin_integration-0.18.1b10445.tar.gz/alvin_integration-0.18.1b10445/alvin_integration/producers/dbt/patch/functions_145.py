# overrides dbt/adapters/spark/connections.py#get_response#305
def get_response(cls, cursor):
    from alvin_integration.producers.dbt.lineage.extractors.databricks import (
        AlvinDatabricksAdapterResponse,
    )

    # https://github.com/dbt-labs/dbt-spark/issues/142
    message = "OK"

    # [TODO] safety checks
    guid_bytes = cursor._cursor.active_result_set.command_id.operationId.guid
    import uuid

    parsed_uuid = uuid.UUID(bytes=guid_bytes)
    parsed_uuid_as_str = str(parsed_uuid)

    return AlvinDatabricksAdapterResponse(_message=message, job_id=parsed_uuid_as_str)
