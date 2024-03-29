"""Generated message classes for billingbudgets version v1alpha1.

The Cloud Billing Budget API stores Cloud Billing budgets, which define a
budget plan and the rules to execute as spend is tracked against that plan.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'billingbudgets'


class BillingbudgetsBillingAccountsBudgetsCreateRequest(_messages.Message):
  r"""A BillingbudgetsBillingAccountsBudgetsCreateRequest object.

  Fields:
    googleCloudBillingBudgetsV1alpha1CreateBudgetRequest: A
      GoogleCloudBillingBudgetsV1alpha1CreateBudgetRequest resource to be
      passed as the request body.
    parent: Required. The name of the billing account to create the budget in.
      Values are of the form `billingAccounts/{billingAccountId}`.
  """

  googleCloudBillingBudgetsV1alpha1CreateBudgetRequest = _messages.MessageField('GoogleCloudBillingBudgetsV1alpha1CreateBudgetRequest', 1)
  parent = _messages.StringField(2, required=True)


class BillingbudgetsBillingAccountsBudgetsDeleteRequest(_messages.Message):
  r"""A BillingbudgetsBillingAccountsBudgetsDeleteRequest object.

  Fields:
    name: Required. Name of the budget to delete. Values are of the form
      `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
  """

  name = _messages.StringField(1, required=True)


class BillingbudgetsBillingAccountsBudgetsGetRequest(_messages.Message):
  r"""A BillingbudgetsBillingAccountsBudgetsGetRequest object.

  Fields:
    name: Required. Name of budget to get. Values are of the form
      `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
  """

  name = _messages.StringField(1, required=True)


class BillingbudgetsBillingAccountsBudgetsListRequest(_messages.Message):
  r"""A BillingbudgetsBillingAccountsBudgetsListRequest object.

  Fields:
    pageSize: Optional. The maximum number of budgets to return per page. The
      default and maximum value are 100.
    pageToken: Optional. The value returned by the last `ListBudgetsResponse`
      which indicates that this is a continuation of a prior `ListBudgets`
      call, and that the system should return the next page of data.
    parent: Required. Name of billing account to list budgets under. Values
      are of the form `billingAccounts/{billingAccountId}`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class BillingbudgetsBillingAccountsBudgetsPatchRequest(_messages.Message):
  r"""A BillingbudgetsBillingAccountsBudgetsPatchRequest object.

  Fields:
    googleCloudBillingBudgetsV1alpha1UpdateBudgetRequest: A
      GoogleCloudBillingBudgetsV1alpha1UpdateBudgetRequest resource to be
      passed as the request body.
    name: Output only. Resource name of the budget. The resource name implies
      the scope of a budget. Values are of the form
      `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
  """

  googleCloudBillingBudgetsV1alpha1UpdateBudgetRequest = _messages.MessageField('GoogleCloudBillingBudgetsV1alpha1UpdateBudgetRequest', 1)
  name = _messages.StringField(2, required=True)


class GoogleCloudBillingBudgetsV1alpha1AllUpdatesRule(_messages.Message):
  r"""AllUpdatesRule defines notifications that are sent on every update to
  the billing account's spend, regardless of the thresholds defined using
  threshold rules.

  Fields:
    pubsubTopic: Required. The name of the Cloud Pub/Sub topic where budget
      related messages will be published, in the form
      `projects/{project_id}/topics/{topic_id}`. Updates are sent at regular
      intervals to the topic. The topic needs to be created before the budget
      is created; see https://cloud.google.com/billing/docs/how-to/budgets
      #manage-notifications for more details. Caller is expected to have
      `pubsub.topics.setIamPolicy` permission on the topic when it's set for a
      budget, otherwise, the API call will fail with PERMISSION_DENIED. See
      https://cloud.google.com/pubsub/docs/access-control for more details on
      Pub/Sub roles and permissions.
    schemaVersion: Required. The schema version of the notification. Only
      "1.0" is accepted. It represents the JSON schema as defined in
      https://cloud.google.com/billing/docs/how-to/budgets#notification_format
  """

  pubsubTopic = _messages.StringField(1)
  schemaVersion = _messages.StringField(2)


class GoogleCloudBillingBudgetsV1alpha1Budget(_messages.Message):
  r"""A budget is a plan that describes what you expect to spend on Cloud
  projects, plus the rules to execute as spend is tracked against that plan,
  (for example, send an alert when 90% of the target spend is met). Currently
  all plans are monthly budgets so the usage period(s) tracked are implied
  (calendar months of usage back-to-back).

  Fields:
    allUpdatesRule: Optional. Rules to apply to all updates to the actual
      spend, regardless of the thresholds set in `threshold_rules`.
    amount: Required. Budgeted amount.
    budgetFilter: Optional. Filters that define which resources are used to
      compute the actual spend against the budget.
    displayName: User data for display name in UI. Validation: <= 60 chars.
    etag: Optional. Etag to validate that the object is unchanged for a read-
      modify-write operation. An empty etag will cause an update to overwrite
      other changes.
    name: Output only. Resource name of the budget. The resource name implies
      the scope of a budget. Values are of the form
      `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
    thresholdRules: Optional. Rules that trigger alerts (notifications of
      thresholds being crossed) when spend exceeds the specified percentages
      of the budget.
  """

  allUpdatesRule = _messages.MessageField('GoogleCloudBillingBudgetsV1alpha1AllUpdatesRule', 1)
  amount = _messages.MessageField('GoogleCloudBillingBudgetsV1alpha1BudgetAmount', 2)
  budgetFilter = _messages.MessageField('GoogleCloudBillingBudgetsV1alpha1Filter', 3)
  displayName = _messages.StringField(4)
  etag = _messages.StringField(5)
  name = _messages.StringField(6)
  thresholdRules = _messages.MessageField('GoogleCloudBillingBudgetsV1alpha1ThresholdRule', 7, repeated=True)


class GoogleCloudBillingBudgetsV1alpha1BudgetAmount(_messages.Message):
  r"""The budgeted amount for each usage period.

  Fields:
    lastPeriodAmount: Use the last period's actual spend as the budget for the
      present period.
    specifiedAmount: A specified amount to use as the budget. `currency_code`
      is optional. If specified, it must match the currency of the billing
      account. The `currency_code` is provided on output.
  """

  lastPeriodAmount = _messages.MessageField('GoogleCloudBillingBudgetsV1alpha1LastPeriodAmount', 1)
  specifiedAmount = _messages.MessageField('GoogleTypeMoney', 2)


class GoogleCloudBillingBudgetsV1alpha1CreateBudgetRequest(_messages.Message):
  r"""Request for CreateBudget

  Fields:
    budget: Required. Budget to create.
  """

  budget = _messages.MessageField('GoogleCloudBillingBudgetsV1alpha1Budget', 1)


class GoogleCloudBillingBudgetsV1alpha1Filter(_messages.Message):
  r"""A filter for a budget, limiting the scope of the cost to calculate.

  Enums:
    CreditTypesTreatmentValueValuesEnum: Optional. If not set, default
      behavior is `INCLUDE_ALL_CREDITS`.

  Fields:
    creditTypesTreatment: Optional. If not set, default behavior is
      `INCLUDE_ALL_CREDITS`.
    projects: Optional. A set of projects of the form `projects/{project}`,
      specifying that usage from only this set of projects should be included
      in the budget. If omitted, the report will include all usage for the
      billing account, regardless of which project the usage occurred on. Only
      zero or one project can be specified currently.
    services: Optional. A set of services of the form `services/{service_id}`,
      specifying that usage from only this set of services should be included
      in the budget. If omitted, the report will include usage for all the
      services. The service names are available through the Catalog API:
      https://cloud.google.com/billing/v1/how-tos/catalog-api.
  """

  class CreditTypesTreatmentValueValuesEnum(_messages.Enum):
    r"""Optional. If not set, default behavior is `INCLUDE_ALL_CREDITS`.

    Values:
      CREDIT_TYPES_TREATMENT_UNSPECIFIED: <no description>
      INCLUDE_ALL_CREDITS: All types of credit are subtracted from the gross
        cost to determine the spend for threshold calculations.
      EXCLUDE_ALL_CREDITS: All types of credit are added to the net cost to
        determine the spend for threshold calculations.
    """
    CREDIT_TYPES_TREATMENT_UNSPECIFIED = 0
    INCLUDE_ALL_CREDITS = 1
    EXCLUDE_ALL_CREDITS = 2

  creditTypesTreatment = _messages.EnumField('CreditTypesTreatmentValueValuesEnum', 1)
  projects = _messages.StringField(2, repeated=True)
  services = _messages.StringField(3, repeated=True)


class GoogleCloudBillingBudgetsV1alpha1LastPeriodAmount(_messages.Message):
  r"""Describes a budget amount targeted to last period's spend. At this time,
  the amount is automatically 100% of last period's spend; that is, there are
  no other options yet. Future configuration will be described here (for
  example, configuring a percentage of last period's spend).
  """



class GoogleCloudBillingBudgetsV1alpha1ListBudgetsResponse(_messages.Message):
  r"""Response for ListBudgets

  Fields:
    budgets: List of the budgets owned by the requested billing account.
    nextPageToken: If not empty, indicates that there may be more budgets that
      match the request; this value should be passed in a new
      `ListBudgetsRequest`.
  """

  budgets = _messages.MessageField('GoogleCloudBillingBudgetsV1alpha1Budget', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudBillingBudgetsV1alpha1ThresholdRule(_messages.Message):
  r"""ThresholdRule contains a definition of a threshold which triggers an
  alert (a notification of a threshold being crossed) to be sent when spend
  goes above the specified amount. Alerts are automatically e-mailed to users
  with the Billing Account Administrator role or the Billing Account User
  role. The thresholds here have no effect on notifications sent to anything
  configured under `Budget.all_updates_rule`.

  Enums:
    SpendBasisValueValuesEnum: Optional. The type of basis used to determine
      if spend has passed the threshold. Behavior defaults to CURRENT_SPEND if
      not set.

  Fields:
    spendBasis: Optional. The type of basis used to determine if spend has
      passed the threshold. Behavior defaults to CURRENT_SPEND if not set.
    thresholdPercent: Required. Send an alert when this threshold is exceeded.
      This is a 1.0-based percentage, so 0.5 = 50%. Validation: non-negative
      number.
  """

  class SpendBasisValueValuesEnum(_messages.Enum):
    r"""Optional. The type of basis used to determine if spend has passed the
    threshold. Behavior defaults to CURRENT_SPEND if not set.

    Values:
      BASIS_UNSPECIFIED: Unspecified threshold basis.
      CURRENT_SPEND: Use current spend as the basis for comparison against the
        threshold.
      FORECASTED_SPEND: Use forecasted spend for the period as the basis for
        comparison against the threshold.
    """
    BASIS_UNSPECIFIED = 0
    CURRENT_SPEND = 1
    FORECASTED_SPEND = 2

  spendBasis = _messages.EnumField('SpendBasisValueValuesEnum', 1)
  thresholdPercent = _messages.FloatField(2)


class GoogleCloudBillingBudgetsV1alpha1UpdateBudgetRequest(_messages.Message):
  r"""Request for UpdateBudget

  Fields:
    budget: Required. The updated budget object. The budget to update is
      specified by the budget name in the budget.
    updateMask: Optional. Indicates which fields in the provided budget to
      update. Read-only fields (such as `name`) cannot be changed. If this is
      not provided, then only fields with non-default values from the request
      are updated. See https://developers.google.com/protocol-
      buffers/docs/proto3#default for more details about default values.
  """

  budget = _messages.MessageField('GoogleCloudBillingBudgetsV1alpha1Budget', 1)
  updateMask = _messages.StringField(2)


class GoogleProtobufEmpty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class GoogleTypeMoney(_messages.Message):
  r"""Represents an amount of money with its currency type.

  Fields:
    currencyCode: The 3-letter currency code defined in ISO 4217.
    nanos: Number of nano (10^-9) units of the amount. The value must be
      between -999,999,999 and +999,999,999 inclusive. If `units` is positive,
      `nanos` must be positive or zero. If `units` is zero, `nanos` can be
      positive, zero, or negative. If `units` is negative, `nanos` must be
      negative or zero. For example $-1.75 is represented as `units`=-1 and
      `nanos`=-750,000,000.
    units: The whole units of the amount. For example if `currencyCode` is
      `"USD"`, then 1 unit is one US dollar.
  """

  currencyCode = _messages.StringField(1)
  nanos = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  units = _messages.IntegerField(3)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
