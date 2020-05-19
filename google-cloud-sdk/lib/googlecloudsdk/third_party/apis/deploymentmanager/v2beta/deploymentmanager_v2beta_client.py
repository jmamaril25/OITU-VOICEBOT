"""Generated client library for deploymentmanager version v2beta."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.deploymentmanager.v2beta import deploymentmanager_v2beta_messages as messages


class DeploymentmanagerV2beta(base_api.BaseApiClient):
  """Generated client library for service deploymentmanager version v2beta."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://www.googleapis.com/deploymentmanager/v2beta/'
  MTLS_BASE_URL = u''

  _PACKAGE = u'deploymentmanager'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-platform.read-only', u'https://www.googleapis.com/auth/ndev.cloudman', u'https://www.googleapis.com/auth/ndev.cloudman.readonly']
  _VERSION = u'v2beta'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = u'google-cloud-sdk'
  _CLIENT_CLASS_NAME = u'DeploymentmanagerV2beta'
  _URL_VERSION = u'v2beta'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new deploymentmanager handle."""
    url = url or self.BASE_URL
    super(DeploymentmanagerV2beta, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.compositeTypes = self.CompositeTypesService(self)
    self.deployments = self.DeploymentsService(self)
    self.manifests = self.ManifestsService(self)
    self.operations = self.OperationsService(self)
    self.resources = self.ResourcesService(self)
    self.typeProviders = self.TypeProvidersService(self)
    self.types = self.TypesService(self)

  class CompositeTypesService(base_api.BaseApiService):
    """Service class for the compositeTypes resource."""

    _NAME = u'compositeTypes'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.CompositeTypesService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      r"""Deletes a composite type.

      Args:
        request: (DeploymentmanagerCompositeTypesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'deploymentmanager.compositeTypes.delete',
        ordered_params=[u'project', u'compositeType'],
        path_params=[u'compositeType', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/compositeTypes/{compositeType}',
        request_field='',
        request_type_name=u'DeploymentmanagerCompositeTypesDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets information about a specific composite type.

      Args:
        request: (DeploymentmanagerCompositeTypesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CompositeType) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.compositeTypes.get',
        ordered_params=[u'project', u'compositeType'],
        path_params=[u'compositeType', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/compositeTypes/{compositeType}',
        request_field='',
        request_type_name=u'DeploymentmanagerCompositeTypesGetRequest',
        response_type_name=u'CompositeType',
        supports_download=False,
    )

    def Insert(self, request, global_params=None):
      r"""Creates a composite type.

      Args:
        request: (DeploymentmanagerCompositeTypesInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    Insert.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'deploymentmanager.compositeTypes.insert',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/compositeTypes',
        request_field=u'compositeType',
        request_type_name=u'DeploymentmanagerCompositeTypesInsertRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all composite types for Deployment Manager.

      Args:
        request: (DeploymentmanagerCompositeTypesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CompositeTypesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.compositeTypes.list',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[u'filter', u'maxResults', u'orderBy', u'pageToken'],
        relative_path=u'projects/{project}/global/compositeTypes',
        request_field='',
        request_type_name=u'DeploymentmanagerCompositeTypesListRequest',
        response_type_name=u'CompositeTypesListResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Patches a composite type.

      Args:
        request: (DeploymentmanagerCompositeTypesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PATCH',
        method_id=u'deploymentmanager.compositeTypes.patch',
        ordered_params=[u'project', u'compositeType'],
        path_params=[u'compositeType', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/compositeTypes/{compositeType}',
        request_field=u'compositeTypeResource',
        request_type_name=u'DeploymentmanagerCompositeTypesPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates a composite type.

      Args:
        request: (DeploymentmanagerCompositeTypesUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'deploymentmanager.compositeTypes.update',
        ordered_params=[u'project', u'compositeType'],
        path_params=[u'compositeType', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/compositeTypes/{compositeType}',
        request_field=u'compositeTypeResource',
        request_type_name=u'DeploymentmanagerCompositeTypesUpdateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class DeploymentsService(base_api.BaseApiService):
    """Service class for the deployments resource."""

    _NAME = u'deployments'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.DeploymentsService, self).__init__(client)
      self._upload_configs = {
          }

    def CancelPreview(self, request, global_params=None):
      r"""Cancels and removes the preview currently associated with the deployment.

      Args:
        request: (DeploymentmanagerDeploymentsCancelPreviewRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('CancelPreview')
      return self._RunMethod(
          config, request, global_params=global_params)

    CancelPreview.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'deploymentmanager.deployments.cancelPreview',
        ordered_params=[u'project', u'deployment'],
        path_params=[u'deployment', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/deployments/{deployment}/cancelPreview',
        request_field=u'deploymentsCancelPreviewRequest',
        request_type_name=u'DeploymentmanagerDeploymentsCancelPreviewRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a deployment and all of the resources in the deployment.

      Args:
        request: (DeploymentmanagerDeploymentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'deploymentmanager.deployments.delete',
        ordered_params=[u'project', u'deployment'],
        path_params=[u'deployment', u'project'],
        query_params=[u'deletePolicy'],
        relative_path=u'projects/{project}/global/deployments/{deployment}',
        request_field='',
        request_type_name=u'DeploymentmanagerDeploymentsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets information about a specific deployment.

      Args:
        request: (DeploymentmanagerDeploymentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Deployment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.deployments.get',
        ordered_params=[u'project', u'deployment'],
        path_params=[u'deployment', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/deployments/{deployment}',
        request_field='',
        request_type_name=u'DeploymentmanagerDeploymentsGetRequest',
        response_type_name=u'Deployment',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource. May be empty if no such policy or resource exists.

      Args:
        request: (DeploymentmanagerDeploymentsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.deployments.getIamPolicy',
        ordered_params=[u'project', u'resource'],
        path_params=[u'project', u'resource'],
        query_params=[],
        relative_path=u'projects/{project}/global/deployments/{resource}/getIamPolicy',
        request_field='',
        request_type_name=u'DeploymentmanagerDeploymentsGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def Insert(self, request, global_params=None):
      r"""Creates a deployment and all of the resources described by the deployment manifest.

      Args:
        request: (DeploymentmanagerDeploymentsInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    Insert.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'deploymentmanager.deployments.insert',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[u'createPolicy', u'preview'],
        relative_path=u'projects/{project}/global/deployments',
        request_field=u'deployment',
        request_type_name=u'DeploymentmanagerDeploymentsInsertRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all deployments for a given project.

      Args:
        request: (DeploymentmanagerDeploymentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeploymentsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.deployments.list',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[u'filter', u'maxResults', u'orderBy', u'pageToken'],
        relative_path=u'projects/{project}/global/deployments',
        request_field='',
        request_type_name=u'DeploymentmanagerDeploymentsListRequest',
        response_type_name=u'DeploymentsListResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Patches a deployment and all of the resources described by the deployment manifest.

      Args:
        request: (DeploymentmanagerDeploymentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PATCH',
        method_id=u'deploymentmanager.deployments.patch',
        ordered_params=[u'project', u'deployment'],
        path_params=[u'deployment', u'project'],
        query_params=[u'createPolicy', u'deletePolicy', u'preview'],
        relative_path=u'projects/{project}/global/deployments/{deployment}',
        request_field=u'deploymentResource',
        request_type_name=u'DeploymentmanagerDeploymentsPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any existing policy.

      Args:
        request: (DeploymentmanagerDeploymentsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'deploymentmanager.deployments.setIamPolicy',
        ordered_params=[u'project', u'resource'],
        path_params=[u'project', u'resource'],
        query_params=[],
        relative_path=u'projects/{project}/global/deployments/{resource}/setIamPolicy',
        request_field=u'globalSetPolicyRequest',
        request_type_name=u'DeploymentmanagerDeploymentsSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def Stop(self, request, global_params=None):
      r"""Stops an ongoing operation. This does not roll back any work that has already been completed, but prevents any new work from being started.

      Args:
        request: (DeploymentmanagerDeploymentsStopRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Stop')
      return self._RunMethod(
          config, request, global_params=global_params)

    Stop.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'deploymentmanager.deployments.stop',
        ordered_params=[u'project', u'deployment'],
        path_params=[u'deployment', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/deployments/{deployment}/stop',
        request_field=u'deploymentsStopRequest',
        request_type_name=u'DeploymentmanagerDeploymentsStopRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.

      Args:
        request: (DeploymentmanagerDeploymentsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'deploymentmanager.deployments.testIamPermissions',
        ordered_params=[u'project', u'resource'],
        path_params=[u'project', u'resource'],
        query_params=[],
        relative_path=u'projects/{project}/global/deployments/{resource}/testIamPermissions',
        request_field=u'testPermissionsRequest',
        request_type_name=u'DeploymentmanagerDeploymentsTestIamPermissionsRequest',
        response_type_name=u'TestPermissionsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates a deployment and all of the resources described by the deployment manifest.

      Args:
        request: (DeploymentmanagerDeploymentsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'deploymentmanager.deployments.update',
        ordered_params=[u'project', u'deployment'],
        path_params=[u'deployment', u'project'],
        query_params=[u'createPolicy', u'deletePolicy', u'preview'],
        relative_path=u'projects/{project}/global/deployments/{deployment}',
        request_field=u'deploymentResource',
        request_type_name=u'DeploymentmanagerDeploymentsUpdateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ManifestsService(base_api.BaseApiService):
    """Service class for the manifests resource."""

    _NAME = u'manifests'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.ManifestsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a specific manifest.

      Args:
        request: (DeploymentmanagerManifestsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Manifest) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.manifests.get',
        ordered_params=[u'project', u'deployment', u'manifest'],
        path_params=[u'deployment', u'manifest', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/deployments/{deployment}/manifests/{manifest}',
        request_field='',
        request_type_name=u'DeploymentmanagerManifestsGetRequest',
        response_type_name=u'Manifest',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all manifests for a given deployment.

      Args:
        request: (DeploymentmanagerManifestsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManifestsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.manifests.list',
        ordered_params=[u'project', u'deployment'],
        path_params=[u'deployment', u'project'],
        query_params=[u'filter', u'maxResults', u'orderBy', u'pageToken'],
        relative_path=u'projects/{project}/global/deployments/{deployment}/manifests',
        request_field='',
        request_type_name=u'DeploymentmanagerManifestsListRequest',
        response_type_name=u'ManifestsListResponse',
        supports_download=False,
    )

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a specific operation.

      Args:
        request: (DeploymentmanagerOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.operations.get',
        ordered_params=[u'project', u'operation'],
        path_params=[u'operation', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/operations/{operation}',
        request_field='',
        request_type_name=u'DeploymentmanagerOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all operations for a project.

      Args:
        request: (DeploymentmanagerOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (OperationsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.operations.list',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[u'filter', u'maxResults', u'orderBy', u'pageToken'],
        relative_path=u'projects/{project}/global/operations',
        request_field='',
        request_type_name=u'DeploymentmanagerOperationsListRequest',
        response_type_name=u'OperationsListResponse',
        supports_download=False,
    )

  class ResourcesService(base_api.BaseApiService):
    """Service class for the resources resource."""

    _NAME = u'resources'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.ResourcesService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a single resource.

      Args:
        request: (DeploymentmanagerResourcesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Resource) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.resources.get',
        ordered_params=[u'project', u'deployment', u'resource'],
        path_params=[u'deployment', u'project', u'resource'],
        query_params=[],
        relative_path=u'projects/{project}/global/deployments/{deployment}/resources/{resource}',
        request_field='',
        request_type_name=u'DeploymentmanagerResourcesGetRequest',
        response_type_name=u'Resource',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all resources in a given deployment.

      Args:
        request: (DeploymentmanagerResourcesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ResourcesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.resources.list',
        ordered_params=[u'project', u'deployment'],
        path_params=[u'deployment', u'project'],
        query_params=[u'filter', u'maxResults', u'orderBy', u'pageToken'],
        relative_path=u'projects/{project}/global/deployments/{deployment}/resources',
        request_field='',
        request_type_name=u'DeploymentmanagerResourcesListRequest',
        response_type_name=u'ResourcesListResponse',
        supports_download=False,
    )

  class TypeProvidersService(base_api.BaseApiService):
    """Service class for the typeProviders resource."""

    _NAME = u'typeProviders'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.TypeProvidersService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      r"""Deletes a type provider.

      Args:
        request: (DeploymentmanagerTypeProvidersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'deploymentmanager.typeProviders.delete',
        ordered_params=[u'project', u'typeProvider'],
        path_params=[u'project', u'typeProvider'],
        query_params=[],
        relative_path=u'projects/{project}/global/typeProviders/{typeProvider}',
        request_field='',
        request_type_name=u'DeploymentmanagerTypeProvidersDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets information about a specific type provider.

      Args:
        request: (DeploymentmanagerTypeProvidersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TypeProvider) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.typeProviders.get',
        ordered_params=[u'project', u'typeProvider'],
        path_params=[u'project', u'typeProvider'],
        query_params=[],
        relative_path=u'projects/{project}/global/typeProviders/{typeProvider}',
        request_field='',
        request_type_name=u'DeploymentmanagerTypeProvidersGetRequest',
        response_type_name=u'TypeProvider',
        supports_download=False,
    )

    def GetType(self, request, global_params=None):
      r"""Gets a type info for a type provided by a TypeProvider.

      Args:
        request: (DeploymentmanagerTypeProvidersGetTypeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TypeInfo) The response message.
      """
      config = self.GetMethodConfig('GetType')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetType.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.typeProviders.getType',
        ordered_params=[u'project', u'typeProvider', u'type'],
        path_params=[u'project', u'type', u'typeProvider'],
        query_params=[],
        relative_path=u'projects/{project}/global/typeProviders/{typeProvider}/types/{type}',
        request_field='',
        request_type_name=u'DeploymentmanagerTypeProvidersGetTypeRequest',
        response_type_name=u'TypeInfo',
        supports_download=False,
    )

    def Insert(self, request, global_params=None):
      r"""Creates a type provider.

      Args:
        request: (DeploymentmanagerTypeProvidersInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    Insert.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'deploymentmanager.typeProviders.insert',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/typeProviders',
        request_field=u'typeProvider',
        request_type_name=u'DeploymentmanagerTypeProvidersInsertRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all resource type providers for Deployment Manager.

      Args:
        request: (DeploymentmanagerTypeProvidersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TypeProvidersListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.typeProviders.list',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[u'filter', u'maxResults', u'orderBy', u'pageToken'],
        relative_path=u'projects/{project}/global/typeProviders',
        request_field='',
        request_type_name=u'DeploymentmanagerTypeProvidersListRequest',
        response_type_name=u'TypeProvidersListResponse',
        supports_download=False,
    )

    def ListTypes(self, request, global_params=None):
      r"""Lists all the type info for a TypeProvider.

      Args:
        request: (DeploymentmanagerTypeProvidersListTypesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TypeProvidersListTypesResponse) The response message.
      """
      config = self.GetMethodConfig('ListTypes')
      return self._RunMethod(
          config, request, global_params=global_params)

    ListTypes.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.typeProviders.listTypes',
        ordered_params=[u'project', u'typeProvider'],
        path_params=[u'project', u'typeProvider'],
        query_params=[u'filter', u'maxResults', u'orderBy', u'pageToken'],
        relative_path=u'projects/{project}/global/typeProviders/{typeProvider}/types',
        request_field='',
        request_type_name=u'DeploymentmanagerTypeProvidersListTypesRequest',
        response_type_name=u'TypeProvidersListTypesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Patches a type provider.

      Args:
        request: (DeploymentmanagerTypeProvidersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PATCH',
        method_id=u'deploymentmanager.typeProviders.patch',
        ordered_params=[u'project', u'typeProvider'],
        path_params=[u'project', u'typeProvider'],
        query_params=[],
        relative_path=u'projects/{project}/global/typeProviders/{typeProvider}',
        request_field=u'typeProviderResource',
        request_type_name=u'DeploymentmanagerTypeProvidersPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates a type provider.

      Args:
        request: (DeploymentmanagerTypeProvidersUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'deploymentmanager.typeProviders.update',
        ordered_params=[u'project', u'typeProvider'],
        path_params=[u'project', u'typeProvider'],
        query_params=[],
        relative_path=u'projects/{project}/global/typeProviders/{typeProvider}',
        request_field=u'typeProviderResource',
        request_type_name=u'DeploymentmanagerTypeProvidersUpdateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class TypesService(base_api.BaseApiService):
    """Service class for the types resource."""

    _NAME = u'types'

    def __init__(self, client):
      super(DeploymentmanagerV2beta.TypesService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists all resource types for Deployment Manager.

      Args:
        request: (DeploymentmanagerTypesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TypesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'deploymentmanager.types.list',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[u'filter', u'maxResults', u'orderBy', u'pageToken'],
        relative_path=u'projects/{project}/global/types',
        request_field='',
        request_type_name=u'DeploymentmanagerTypesListRequest',
        response_type_name=u'TypesListResponse',
        supports_download=False,
    )
