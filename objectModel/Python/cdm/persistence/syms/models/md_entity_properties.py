# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MDEntityProperties(Model):
    """Defines the artifact entity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param origin_object_id: Entity object id maintained by the caller.
    :type origin_object_id: str
    :ivar object_id: Entity object id maintained by SyMS.
    :vartype object_id: str
    :ivar object_version: Entity object version maintained by SyMS.
    :vartype object_version: long
    :param publish_status: Possible values include: 'PUBLISHED'
    :type publish_status: str or :class:`PublishStatus
     <Microsoft.ADF.SyMSAPIClient.models.PublishStatus>`
    :param properties: Property bag
    :type properties: dict
    """ 

    _validation = {
        'object_id': {'readonly': True},
        'object_version': {'readonly': True},
    }

    _attribute_map = {
        'origin_object_id': {'key': 'OriginObjectId', 'type': 'str'},
        'object_id': {'key': 'ObjectId', 'type': 'str'},
        'object_version': {'key': 'ObjectVersion', 'type': 'long'},
        'publish_status': {'key': 'PublishStatus', 'type': 'PublishStatus'},
        'properties': {'key': 'Properties', 'type': '{object}'},
    }

    def __init__(self, origin_object_id=None, publish_status=None, properties=None):
        self.origin_object_id = origin_object_id
        self.object_id = None
        self.object_version = None
        self.publish_status = publish_status
        self.properties = properties