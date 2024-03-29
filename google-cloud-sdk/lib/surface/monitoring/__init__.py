# -*- coding: utf-8 -*- #
# Copyright 2018 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command group for Stackdriver Monitoring."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


@base.ReleaseTracks(base.ReleaseTrack.GA)
class MonitoringGA(base.Group):
  # pylint: disable=line-too-long
  """Manage Stackdriver Monitoring dashboards."""
  category = base.MONITORING_CATEGORY

  detailed_help = {
      'DESCRIPTION':
          """\
          Manage Stackdriver Monitoring dashboards.

          More information can be found here:
              * https://cloud.google.com/monitoring/dashboards/api-dashboard
      """
  }


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class MonitoringBeta(base.Group):
  # pylint: disable=line-too-long
  """Manage Stackdriver Monitoring dashboards and notification channels."""
  category = base.MONITORING_CATEGORY

  detailed_help = {
      'DESCRIPTION':
          """\
          Manage Stackdriver Monitoring dashboards and notification
          channels.

          More information can be found here:
              * https://cloud.google.com/monitoring/api/v3/
              * https://cloud.google.com/monitoring/alerts/using-channels-api
              * https://cloud.google.com/monitoring/dashboards/api-dashboard
      """
  }


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class MonitoringAlpha(base.Group):
  # pylint: disable=line-too-long
  """Manage Stackdriver Monitoring alerting policies, dashboards, and notification channels."""
  category = base.MONITORING_CATEGORY

  detailed_help = {
      'DESCRIPTION':
          """\
          Manage Stackdriver Monitoring alerting policies, dashboards, and notification
          channels.

          More information can be found here:
              * https://cloud.google.com/monitoring/api/v3/
              * https://cloud.google.com/monitoring/alerts/using-alerting-api
              * https://cloud.google.com/monitoring/alerts/using-channels-api
              * https://cloud.google.com/monitoring/dashboards/api-dashboard
      """
  }
