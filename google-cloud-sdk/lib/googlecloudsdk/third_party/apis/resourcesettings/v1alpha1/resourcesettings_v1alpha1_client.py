"""Generated client library for resourcesettings version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.resourcesettings.v1alpha1 import resourcesettings_v1alpha1_messages as messages


class ResourcesettingsV1alpha1(base_api.BaseApiClient):
  """Generated client library for service resourcesettings version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://resourcesettings.googleapis.com/'
  MTLS_BASE_URL = u'https://resourcesettings.mtls.googleapis.com/'

  _PACKAGE = u'resourcesettings'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = u'google-cloud-sdk'
  _CLIENT_CLASS_NAME = u'ResourcesettingsV1alpha1'
  _URL_VERSION = u'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new resourcesettings handle."""
    url = url or self.BASE_URL
    super(ResourcesettingsV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.folders_settings_value = self.FoldersSettingsValueService(self)
    self.folders_settings = self.FoldersSettingsService(self)
    self.folders = self.FoldersService(self)
    self.organizations_settings_value = self.OrganizationsSettingsValueService(self)
    self.organizations_settings = self.OrganizationsSettingsService(self)
    self.organizations = self.OrganizationsService(self)
    self.projects_settings_value = self.ProjectsSettingsValueService(self)
    self.projects_settings = self.ProjectsSettingsService(self)
    self.projects = self.ProjectsService(self)

  class FoldersSettingsValueService(base_api.BaseApiService):
    """Service class for the folders_settings_value resource."""

    _NAME = u'folders_settings_value'

    def __init__(self, client):
      super(ResourcesettingsV1alpha1.FoldersSettingsValueService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a setting value.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting does not exist.
Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the
setting value already exists on the given Cloud resource.
Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if
the setting is flagged as read only.

      Args:
        request: (GoogleCloudResourcesettingsV1alpha1SettingValue) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SettingValue) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/folders/{foldersId}/settings/{settingsId}/value',
        http_method=u'POST',
        method_id=u'resourcesettings.folders.settings.value.create',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='<request>',
        request_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        supports_download=False,
    )

  class FoldersSettingsService(base_api.BaseApiService):
    """Service class for the folders_settings resource."""

    _NAME = u'folders_settings'

    def __init__(self, client):
      super(ResourcesettingsV1alpha1.FoldersSettingsService, self).__init__(client)
      self._upload_configs = {
          }

    def DeleteValue(self, request, global_params=None):
      r"""Deletes a setting value. If the setting value does not exist, the operation.
is a no-op.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting or the setting value does not exist. The setting value will not
exist if a prior call to `DeleteSetting` for the setting value already
returned a success code.
Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if
the setting is flagged as read only.

      Args:
        request: (ResourcesettingsFoldersSettingsDeleteValueRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('DeleteValue')
      return self._RunMethod(
          config, request, global_params=global_params)

    DeleteValue.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/folders/{foldersId}/settings/{settingsId}/value',
        http_method=u'DELETE',
        method_id=u'resourcesettings.folders.settings.deleteValue',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'ignoreReadOnly'],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'ResourcesettingsFoldersSettingsDeleteValueRequest',
        response_type_name=u'GoogleProtobufEmpty',
        supports_download=False,
    )

    def GetValue(self, request, global_params=None):
      r"""Gets a setting value.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting value does not exist.

      Args:
        request: (ResourcesettingsFoldersSettingsGetValueRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SettingValue) The response message.
      """
      config = self.GetMethodConfig('GetValue')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetValue.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/folders/{foldersId}/settings/{settingsId}/value',
        http_method=u'GET',
        method_id=u'resourcesettings.folders.settings.getValue',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'ResourcesettingsFoldersSettingsGetValueRequest',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all the settings that are available on the Cloud resource `parent`.

      Args:
        request: (ResourcesettingsFoldersSettingsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1ListSettingsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/folders/{foldersId}/settings',
        http_method=u'GET',
        method_id=u'resourcesettings.folders.settings.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/settings',
        request_field='',
        request_type_name=u'ResourcesettingsFoldersSettingsListRequest',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1ListSettingsResponse',
        supports_download=False,
    )

    def LookupEffectiveValue(self, request, global_params=None):
      r"""Computes the effective setting value of a setting at the Cloud resource.
`parent`. The effective setting value is the calculated setting value at a
Cloud resource and evaluates to one of the following options in the given
order (the next option is used if the previous one does not exist):

1. the setting value on the given resource
2. the setting value on the given resource's nearest ancestor
3. the setting's default value
4. an empty setting value, defined as a `SettingValue` with all fields
unset

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting does not exist.

      Args:
        request: (ResourcesettingsFoldersSettingsLookupEffectiveValueRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SettingValue) The response message.
      """
      config = self.GetMethodConfig('LookupEffectiveValue')
      return self._RunMethod(
          config, request, global_params=global_params)

    LookupEffectiveValue.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/folders/{foldersId}/settings/{settingsId}:lookupEffectiveValue',
        http_method=u'GET',
        method_id=u'resourcesettings.folders.settings.lookupEffectiveValue',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha1/{+parent}:lookupEffectiveValue',
        request_field='',
        request_type_name=u'ResourcesettingsFoldersSettingsLookupEffectiveValueRequest',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        supports_download=False,
    )

    def Search(self, request, global_params=None):
      r"""Searches for all setting values that exist on the resource `parent`. The.
setting values are not limited to those of a particular setting.

      Args:
        request: (ResourcesettingsFoldersSettingsSearchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SearchSettingValuesResponse) The response message.
      """
      config = self.GetMethodConfig('Search')
      return self._RunMethod(
          config, request, global_params=global_params)

    Search.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/folders/{foldersId}/settings:search',
        http_method=u'GET',
        method_id=u'resourcesettings.folders.settings.search',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/settings:search',
        request_field='',
        request_type_name=u'ResourcesettingsFoldersSettingsSearchRequest',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SearchSettingValuesResponse',
        supports_download=False,
    )

    def UpdateValue(self, request, global_params=None):
      r"""Updates a setting value.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting or the setting value does not exist.
Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if
the setting is flagged as read only.
Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag
supplied in the request does not match the persisted etag of the setting
value.

Note: the supplied setting value will perform a full overwrite of all
fields.

      Args:
        request: (GoogleCloudResourcesettingsV1alpha1SettingValue) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SettingValue) The response message.
      """
      config = self.GetMethodConfig('UpdateValue')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateValue.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/folders/{foldersId}/settings/{settingsId}/value',
        http_method=u'PATCH',
        method_id=u'resourcesettings.folders.settings.updateValue',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='<request>',
        request_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        supports_download=False,
    )

  class FoldersService(base_api.BaseApiService):
    """Service class for the folders resource."""

    _NAME = u'folders'

    def __init__(self, client):
      super(ResourcesettingsV1alpha1.FoldersService, self).__init__(client)
      self._upload_configs = {
          }

  class OrganizationsSettingsValueService(base_api.BaseApiService):
    """Service class for the organizations_settings_value resource."""

    _NAME = u'organizations_settings_value'

    def __init__(self, client):
      super(ResourcesettingsV1alpha1.OrganizationsSettingsValueService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a setting value.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting does not exist.
Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the
setting value already exists on the given Cloud resource.
Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if
the setting is flagged as read only.

      Args:
        request: (GoogleCloudResourcesettingsV1alpha1SettingValue) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SettingValue) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/organizations/{organizationsId}/settings/{settingsId}/value',
        http_method=u'POST',
        method_id=u'resourcesettings.organizations.settings.value.create',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='<request>',
        request_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        supports_download=False,
    )

  class OrganizationsSettingsService(base_api.BaseApiService):
    """Service class for the organizations_settings resource."""

    _NAME = u'organizations_settings'

    def __init__(self, client):
      super(ResourcesettingsV1alpha1.OrganizationsSettingsService, self).__init__(client)
      self._upload_configs = {
          }

    def DeleteValue(self, request, global_params=None):
      r"""Deletes a setting value. If the setting value does not exist, the operation.
is a no-op.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting or the setting value does not exist. The setting value will not
exist if a prior call to `DeleteSetting` for the setting value already
returned a success code.
Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if
the setting is flagged as read only.

      Args:
        request: (ResourcesettingsOrganizationsSettingsDeleteValueRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('DeleteValue')
      return self._RunMethod(
          config, request, global_params=global_params)

    DeleteValue.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/organizations/{organizationsId}/settings/{settingsId}/value',
        http_method=u'DELETE',
        method_id=u'resourcesettings.organizations.settings.deleteValue',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'ignoreReadOnly'],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'ResourcesettingsOrganizationsSettingsDeleteValueRequest',
        response_type_name=u'GoogleProtobufEmpty',
        supports_download=False,
    )

    def GetValue(self, request, global_params=None):
      r"""Gets a setting value.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting value does not exist.

      Args:
        request: (ResourcesettingsOrganizationsSettingsGetValueRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SettingValue) The response message.
      """
      config = self.GetMethodConfig('GetValue')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetValue.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/organizations/{organizationsId}/settings/{settingsId}/value',
        http_method=u'GET',
        method_id=u'resourcesettings.organizations.settings.getValue',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'ResourcesettingsOrganizationsSettingsGetValueRequest',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all the settings that are available on the Cloud resource `parent`.

      Args:
        request: (ResourcesettingsOrganizationsSettingsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1ListSettingsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/organizations/{organizationsId}/settings',
        http_method=u'GET',
        method_id=u'resourcesettings.organizations.settings.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/settings',
        request_field='',
        request_type_name=u'ResourcesettingsOrganizationsSettingsListRequest',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1ListSettingsResponse',
        supports_download=False,
    )

    def LookupEffectiveValue(self, request, global_params=None):
      r"""Computes the effective setting value of a setting at the Cloud resource.
`parent`. The effective setting value is the calculated setting value at a
Cloud resource and evaluates to one of the following options in the given
order (the next option is used if the previous one does not exist):

1. the setting value on the given resource
2. the setting value on the given resource's nearest ancestor
3. the setting's default value
4. an empty setting value, defined as a `SettingValue` with all fields
unset

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting does not exist.

      Args:
        request: (ResourcesettingsOrganizationsSettingsLookupEffectiveValueRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SettingValue) The response message.
      """
      config = self.GetMethodConfig('LookupEffectiveValue')
      return self._RunMethod(
          config, request, global_params=global_params)

    LookupEffectiveValue.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/organizations/{organizationsId}/settings/{settingsId}:lookupEffectiveValue',
        http_method=u'GET',
        method_id=u'resourcesettings.organizations.settings.lookupEffectiveValue',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha1/{+parent}:lookupEffectiveValue',
        request_field='',
        request_type_name=u'ResourcesettingsOrganizationsSettingsLookupEffectiveValueRequest',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        supports_download=False,
    )

    def Search(self, request, global_params=None):
      r"""Searches for all setting values that exist on the resource `parent`. The.
setting values are not limited to those of a particular setting.

      Args:
        request: (ResourcesettingsOrganizationsSettingsSearchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SearchSettingValuesResponse) The response message.
      """
      config = self.GetMethodConfig('Search')
      return self._RunMethod(
          config, request, global_params=global_params)

    Search.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/organizations/{organizationsId}/settings:search',
        http_method=u'GET',
        method_id=u'resourcesettings.organizations.settings.search',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/settings:search',
        request_field='',
        request_type_name=u'ResourcesettingsOrganizationsSettingsSearchRequest',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SearchSettingValuesResponse',
        supports_download=False,
    )

    def UpdateValue(self, request, global_params=None):
      r"""Updates a setting value.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting or the setting value does not exist.
Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if
the setting is flagged as read only.
Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag
supplied in the request does not match the persisted etag of the setting
value.

Note: the supplied setting value will perform a full overwrite of all
fields.

      Args:
        request: (GoogleCloudResourcesettingsV1alpha1SettingValue) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SettingValue) The response message.
      """
      config = self.GetMethodConfig('UpdateValue')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateValue.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/organizations/{organizationsId}/settings/{settingsId}/value',
        http_method=u'PATCH',
        method_id=u'resourcesettings.organizations.settings.updateValue',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='<request>',
        request_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        supports_download=False,
    )

  class OrganizationsService(base_api.BaseApiService):
    """Service class for the organizations resource."""

    _NAME = u'organizations'

    def __init__(self, client):
      super(ResourcesettingsV1alpha1.OrganizationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsSettingsValueService(base_api.BaseApiService):
    """Service class for the projects_settings_value resource."""

    _NAME = u'projects_settings_value'

    def __init__(self, client):
      super(ResourcesettingsV1alpha1.ProjectsSettingsValueService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a setting value.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting does not exist.
Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the
setting value already exists on the given Cloud resource.
Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if
the setting is flagged as read only.

      Args:
        request: (GoogleCloudResourcesettingsV1alpha1SettingValue) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SettingValue) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/settings/{settingsId}/value',
        http_method=u'POST',
        method_id=u'resourcesettings.projects.settings.value.create',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='<request>',
        request_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        supports_download=False,
    )

  class ProjectsSettingsService(base_api.BaseApiService):
    """Service class for the projects_settings resource."""

    _NAME = u'projects_settings'

    def __init__(self, client):
      super(ResourcesettingsV1alpha1.ProjectsSettingsService, self).__init__(client)
      self._upload_configs = {
          }

    def DeleteValue(self, request, global_params=None):
      r"""Deletes a setting value. If the setting value does not exist, the operation.
is a no-op.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting or the setting value does not exist. The setting value will not
exist if a prior call to `DeleteSetting` for the setting value already
returned a success code.
Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if
the setting is flagged as read only.

      Args:
        request: (ResourcesettingsProjectsSettingsDeleteValueRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('DeleteValue')
      return self._RunMethod(
          config, request, global_params=global_params)

    DeleteValue.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/settings/{settingsId}/value',
        http_method=u'DELETE',
        method_id=u'resourcesettings.projects.settings.deleteValue',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'ignoreReadOnly'],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'ResourcesettingsProjectsSettingsDeleteValueRequest',
        response_type_name=u'GoogleProtobufEmpty',
        supports_download=False,
    )

    def GetValue(self, request, global_params=None):
      r"""Gets a setting value.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting value does not exist.

      Args:
        request: (ResourcesettingsProjectsSettingsGetValueRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SettingValue) The response message.
      """
      config = self.GetMethodConfig('GetValue')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetValue.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/settings/{settingsId}/value',
        http_method=u'GET',
        method_id=u'resourcesettings.projects.settings.getValue',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'ResourcesettingsProjectsSettingsGetValueRequest',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all the settings that are available on the Cloud resource `parent`.

      Args:
        request: (ResourcesettingsProjectsSettingsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1ListSettingsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/settings',
        http_method=u'GET',
        method_id=u'resourcesettings.projects.settings.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/settings',
        request_field='',
        request_type_name=u'ResourcesettingsProjectsSettingsListRequest',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1ListSettingsResponse',
        supports_download=False,
    )

    def LookupEffectiveValue(self, request, global_params=None):
      r"""Computes the effective setting value of a setting at the Cloud resource.
`parent`. The effective setting value is the calculated setting value at a
Cloud resource and evaluates to one of the following options in the given
order (the next option is used if the previous one does not exist):

1. the setting value on the given resource
2. the setting value on the given resource's nearest ancestor
3. the setting's default value
4. an empty setting value, defined as a `SettingValue` with all fields
unset

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting does not exist.

      Args:
        request: (ResourcesettingsProjectsSettingsLookupEffectiveValueRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SettingValue) The response message.
      """
      config = self.GetMethodConfig('LookupEffectiveValue')
      return self._RunMethod(
          config, request, global_params=global_params)

    LookupEffectiveValue.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/settings/{settingsId}:lookupEffectiveValue',
        http_method=u'GET',
        method_id=u'resourcesettings.projects.settings.lookupEffectiveValue',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha1/{+parent}:lookupEffectiveValue',
        request_field='',
        request_type_name=u'ResourcesettingsProjectsSettingsLookupEffectiveValueRequest',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        supports_download=False,
    )

    def Search(self, request, global_params=None):
      r"""Searches for all setting values that exist on the resource `parent`. The.
setting values are not limited to those of a particular setting.

      Args:
        request: (ResourcesettingsProjectsSettingsSearchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SearchSettingValuesResponse) The response message.
      """
      config = self.GetMethodConfig('Search')
      return self._RunMethod(
          config, request, global_params=global_params)

    Search.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/settings:search',
        http_method=u'GET',
        method_id=u'resourcesettings.projects.settings.search',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/settings:search',
        request_field='',
        request_type_name=u'ResourcesettingsProjectsSettingsSearchRequest',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SearchSettingValuesResponse',
        supports_download=False,
    )

    def UpdateValue(self, request, global_params=None):
      r"""Updates a setting value.

Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the
setting or the setting value does not exist.
Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if
the setting is flagged as read only.
Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag
supplied in the request does not match the persisted etag of the setting
value.

Note: the supplied setting value will perform a full overwrite of all
fields.

      Args:
        request: (GoogleCloudResourcesettingsV1alpha1SettingValue) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudResourcesettingsV1alpha1SettingValue) The response message.
      """
      config = self.GetMethodConfig('UpdateValue')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateValue.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/settings/{settingsId}/value',
        http_method=u'PATCH',
        method_id=u'resourcesettings.projects.settings.updateValue',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='<request>',
        request_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        response_type_name=u'GoogleCloudResourcesettingsV1alpha1SettingValue',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(ResourcesettingsV1alpha1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
