# coding: utf-8

# flake8: noqa

"""
    Determined API (Beta)

    Determined helps deep learning teams train models more quickly, easily share GPU resources, and effectively collaborate. Determined allows deep learning engineers to focus on building and training models at scale, without needing to worry about DevOps or writing custom code for common tasks like fault tolerance or experiment tracking.  You can think of Determined as a platform that bridges the gap between tools like TensorFlow and PyTorch --- which work great for a single researcher with a single GPU --- to the challenges that arise when doing deep learning at scale, as teams, clusters, and data sets all increase in size.  # noqa: E501

    OpenAPI spec version: 0.1
    Contact: community@determined.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from determined._swagger.client.api.authentication_api import AuthenticationApi
from determined._swagger.client.api.checkpoints_api import CheckpointsApi
from determined._swagger.client.api.cluster_api import ClusterApi
from determined._swagger.client.api.commands_api import CommandsApi
from determined._swagger.client.api.experiments_api import ExperimentsApi
from determined._swagger.client.api.internal_api import InternalApi
from determined._swagger.client.api.models_api import ModelsApi
from determined._swagger.client.api.notebooks_api import NotebooksApi
from determined._swagger.client.api.shells_api import ShellsApi
from determined._swagger.client.api.templates_api import TemplatesApi
from determined._swagger.client.api.tensorboards_api import TensorboardsApi
from determined._swagger.client.api.trials_api import TrialsApi
from determined._swagger.client.api.unimplemented_api import UnimplementedApi
from determined._swagger.client.api.users_api import UsersApi

# import ApiClient
from determined._swagger.client.api_client import ApiClient
from determined._swagger.client.configuration import Configuration
# import models into sdk package
from determined._swagger.client.models.determinedcheckpointv1_state import Determinedcheckpointv1State
from determined._swagger.client.models.determinedcontainerv1_state import Determinedcontainerv1State
from determined._swagger.client.models.determinedexperimentv1_state import Determinedexperimentv1State
from determined._swagger.client.models.determinedtaskv1_state import Determinedtaskv1State
from determined._swagger.client.models.devicev1_type import Devicev1Type
from determined._swagger.client.models.get_hp_importance_response_metric_hp_importance import GetHPImportanceResponseMetricHPImportance
from determined._swagger.client.models.get_trial_response_workload_container import GetTrialResponseWorkloadContainer
from determined._swagger.client.models.protobuf_any import ProtobufAny
from determined._swagger.client.models.protobuf_field_mask import ProtobufFieldMask
from determined._swagger.client.models.protobuf_null_value import ProtobufNullValue
from determined._swagger.client.models.runtime_error import RuntimeError
from determined._swagger.client.models.runtime_stream_error import RuntimeStreamError
from determined._swagger.client.models.stream_result_of_v1_get_hp_importance_response import StreamResultOfV1GetHPImportanceResponse
from determined._swagger.client.models.stream_result_of_v1_get_trial_profiler_available_series_response import StreamResultOfV1GetTrialProfilerAvailableSeriesResponse
from determined._swagger.client.models.stream_result_of_v1_get_trial_profiler_metrics_response import StreamResultOfV1GetTrialProfilerMetricsResponse
from determined._swagger.client.models.stream_result_of_v1_master_logs_response import StreamResultOfV1MasterLogsResponse
from determined._swagger.client.models.stream_result_of_v1_metric_batches_response import StreamResultOfV1MetricBatchesResponse
from determined._swagger.client.models.stream_result_of_v1_metric_names_response import StreamResultOfV1MetricNamesResponse
from determined._swagger.client.models.stream_result_of_v1_notebook_logs_response import StreamResultOfV1NotebookLogsResponse
from determined._swagger.client.models.stream_result_of_v1_trial_logs_fields_response import StreamResultOfV1TrialLogsFieldsResponse
from determined._swagger.client.models.stream_result_of_v1_trial_logs_response import StreamResultOfV1TrialLogsResponse
from determined._swagger.client.models.stream_result_of_v1_trial_preemption_signal_response import StreamResultOfV1TrialPreemptionSignalResponse
from determined._swagger.client.models.stream_result_of_v1_trials_sample_response import StreamResultOfV1TrialsSampleResponse
from determined._swagger.client.models.stream_result_of_v1_trials_snapshot_response import StreamResultOfV1TrialsSnapshotResponse
from determined._swagger.client.models.training_length_units import TrainingLengthUnits
from determined._swagger.client.models.trial_early_exit_exited_reason import TrialEarlyExitExitedReason
from determined._swagger.client.models.trial_profiler_metric_labels_profiler_metric_type import TrialProfilerMetricLabelsProfilerMetricType
from determined._swagger.client.models.trials_sample_response_data_point import TrialsSampleResponseDataPoint
from determined._swagger.client.models.trialv1_trial import Trialv1Trial
from determined._swagger.client.models.v1_activate_experiment_response import V1ActivateExperimentResponse
from determined._swagger.client.models.v1_agent import V1Agent
from determined._swagger.client.models.v1_agent_user_group import V1AgentUserGroup
from determined._swagger.client.models.v1_archive_experiment_response import V1ArchiveExperimentResponse
from determined._swagger.client.models.v1_aws_custom_tag import V1AwsCustomTag
from determined._swagger.client.models.v1_cancel_experiment_response import V1CancelExperimentResponse
from determined._swagger.client.models.v1_checkpoint import V1Checkpoint
from determined._swagger.client.models.v1_checkpoint_metadata import V1CheckpointMetadata
from determined._swagger.client.models.v1_checkpoint_workload import V1CheckpointWorkload
from determined._swagger.client.models.v1_command import V1Command
from determined._swagger.client.models.v1_complete_trial_searcher_validation_response import V1CompleteTrialSearcherValidationResponse
from determined._swagger.client.models.v1_complete_validate_after_operation import V1CompleteValidateAfterOperation
from determined._swagger.client.models.v1_compute_hp_importance_response import V1ComputeHPImportanceResponse
from determined._swagger.client.models.v1_container import V1Container
from determined._swagger.client.models.v1_create_experiment_request import V1CreateExperimentRequest
from determined._swagger.client.models.v1_create_experiment_response import V1CreateExperimentResponse
from determined._swagger.client.models.v1_current_user_response import V1CurrentUserResponse
from determined._swagger.client.models.v1_delete_experiment_response import V1DeleteExperimentResponse
from determined._swagger.client.models.v1_delete_template_response import V1DeleteTemplateResponse
from determined._swagger.client.models.v1_device import V1Device
from determined._swagger.client.models.v1_disable_agent_response import V1DisableAgentResponse
from determined._swagger.client.models.v1_disable_slot_response import V1DisableSlotResponse
from determined._swagger.client.models.v1_enable_agent_response import V1EnableAgentResponse
from determined._swagger.client.models.v1_enable_slot_response import V1EnableSlotResponse
from determined._swagger.client.models.v1_experiment import V1Experiment
from determined._swagger.client.models.v1_experiment_simulation import V1ExperimentSimulation
from determined._swagger.client.models.v1_file import V1File
from determined._swagger.client.models.v1_fitting_policy import V1FittingPolicy
from determined._swagger.client.models.v1_get_agent_response import V1GetAgentResponse
from determined._swagger.client.models.v1_get_agents_request_sort_by import V1GetAgentsRequestSortBy
from determined._swagger.client.models.v1_get_agents_response import V1GetAgentsResponse
from determined._swagger.client.models.v1_get_checkpoint_response import V1GetCheckpointResponse
from determined._swagger.client.models.v1_get_command_response import V1GetCommandResponse
from determined._swagger.client.models.v1_get_commands_request_sort_by import V1GetCommandsRequestSortBy
from determined._swagger.client.models.v1_get_commands_response import V1GetCommandsResponse
from determined._swagger.client.models.v1_get_current_trial_searcher_operation_response import V1GetCurrentTrialSearcherOperationResponse
from determined._swagger.client.models.v1_get_experiment_checkpoints_request_sort_by import V1GetExperimentCheckpointsRequestSortBy
from determined._swagger.client.models.v1_get_experiment_checkpoints_response import V1GetExperimentCheckpointsResponse
from determined._swagger.client.models.v1_get_experiment_labels_response import V1GetExperimentLabelsResponse
from determined._swagger.client.models.v1_get_experiment_response import V1GetExperimentResponse
from determined._swagger.client.models.v1_get_experiment_trials_request_sort_by import V1GetExperimentTrialsRequestSortBy
from determined._swagger.client.models.v1_get_experiment_trials_response import V1GetExperimentTrialsResponse
from determined._swagger.client.models.v1_get_experiment_validation_history_response import V1GetExperimentValidationHistoryResponse
from determined._swagger.client.models.v1_get_experiments_request_sort_by import V1GetExperimentsRequestSortBy
from determined._swagger.client.models.v1_get_experiments_response import V1GetExperimentsResponse
from determined._swagger.client.models.v1_get_hp_importance_response import V1GetHPImportanceResponse
from determined._swagger.client.models.v1_get_master_config_response import V1GetMasterConfigResponse
from determined._swagger.client.models.v1_get_master_response import V1GetMasterResponse
from determined._swagger.client.models.v1_get_model_response import V1GetModelResponse
from determined._swagger.client.models.v1_get_model_version_response import V1GetModelVersionResponse
from determined._swagger.client.models.v1_get_model_versions_request_sort_by import V1GetModelVersionsRequestSortBy
from determined._swagger.client.models.v1_get_model_versions_response import V1GetModelVersionsResponse
from determined._swagger.client.models.v1_get_models_request_sort_by import V1GetModelsRequestSortBy
from determined._swagger.client.models.v1_get_models_response import V1GetModelsResponse
from determined._swagger.client.models.v1_get_notebook_response import V1GetNotebookResponse
from determined._swagger.client.models.v1_get_notebooks_request_sort_by import V1GetNotebooksRequestSortBy
from determined._swagger.client.models.v1_get_notebooks_response import V1GetNotebooksResponse
from determined._swagger.client.models.v1_get_resource_pools_response import V1GetResourcePoolsResponse
from determined._swagger.client.models.v1_get_shell_response import V1GetShellResponse
from determined._swagger.client.models.v1_get_shells_request_sort_by import V1GetShellsRequestSortBy
from determined._swagger.client.models.v1_get_shells_response import V1GetShellsResponse
from determined._swagger.client.models.v1_get_slot_response import V1GetSlotResponse
from determined._swagger.client.models.v1_get_slots_response import V1GetSlotsResponse
from determined._swagger.client.models.v1_get_telemetry_response import V1GetTelemetryResponse
from determined._swagger.client.models.v1_get_template_response import V1GetTemplateResponse
from determined._swagger.client.models.v1_get_templates_request_sort_by import V1GetTemplatesRequestSortBy
from determined._swagger.client.models.v1_get_templates_response import V1GetTemplatesResponse
from determined._swagger.client.models.v1_get_tensorboard_response import V1GetTensorboardResponse
from determined._swagger.client.models.v1_get_tensorboards_request_sort_by import V1GetTensorboardsRequestSortBy
from determined._swagger.client.models.v1_get_tensorboards_response import V1GetTensorboardsResponse
from determined._swagger.client.models.v1_get_trial_checkpoints_request_sort_by import V1GetTrialCheckpointsRequestSortBy
from determined._swagger.client.models.v1_get_trial_checkpoints_response import V1GetTrialCheckpointsResponse
from determined._swagger.client.models.v1_get_trial_profiler_available_series_response import V1GetTrialProfilerAvailableSeriesResponse
from determined._swagger.client.models.v1_get_trial_profiler_metrics_response import V1GetTrialProfilerMetricsResponse
from determined._swagger.client.models.v1_get_trial_response import V1GetTrialResponse
from determined._swagger.client.models.v1_get_user_response import V1GetUserResponse
from determined._swagger.client.models.v1_get_users_response import V1GetUsersResponse
from determined._swagger.client.models.v1_kill_command_response import V1KillCommandResponse
from determined._swagger.client.models.v1_kill_experiment_response import V1KillExperimentResponse
from determined._swagger.client.models.v1_kill_notebook_response import V1KillNotebookResponse
from determined._swagger.client.models.v1_kill_shell_response import V1KillShellResponse
from determined._swagger.client.models.v1_kill_tensorboard_response import V1KillTensorboardResponse
from determined._swagger.client.models.v1_kill_trial_response import V1KillTrialResponse
from determined._swagger.client.models.v1_launch_command_request import V1LaunchCommandRequest
from determined._swagger.client.models.v1_launch_command_response import V1LaunchCommandResponse
from determined._swagger.client.models.v1_launch_notebook_request import V1LaunchNotebookRequest
from determined._swagger.client.models.v1_launch_notebook_response import V1LaunchNotebookResponse
from determined._swagger.client.models.v1_launch_shell_request import V1LaunchShellRequest
from determined._swagger.client.models.v1_launch_shell_response import V1LaunchShellResponse
from determined._swagger.client.models.v1_launch_tensorboard_request import V1LaunchTensorboardRequest
from determined._swagger.client.models.v1_launch_tensorboard_response import V1LaunchTensorboardResponse
from determined._swagger.client.models.v1_log_entry import V1LogEntry
from determined._swagger.client.models.v1_log_level import V1LogLevel
from determined._swagger.client.models.v1_login_request import V1LoginRequest
from determined._swagger.client.models.v1_login_response import V1LoginResponse
from determined._swagger.client.models.v1_logout_response import V1LogoutResponse
from determined._swagger.client.models.v1_master_logs_response import V1MasterLogsResponse
from determined._swagger.client.models.v1_metric_batches_response import V1MetricBatchesResponse
from determined._swagger.client.models.v1_metric_names_response import V1MetricNamesResponse
from determined._swagger.client.models.v1_metric_type import V1MetricType
from determined._swagger.client.models.v1_metrics import V1Metrics
from determined._swagger.client.models.v1_metrics_workload import V1MetricsWorkload
from determined._swagger.client.models.v1_model import V1Model
from determined._swagger.client.models.v1_model_version import V1ModelVersion
from determined._swagger.client.models.v1_notebook import V1Notebook
from determined._swagger.client.models.v1_notebook_logs_response import V1NotebookLogsResponse
from determined._swagger.client.models.v1_order_by import V1OrderBy
from determined._swagger.client.models.v1_pagination import V1Pagination
from determined._swagger.client.models.v1_patch_experiment_response import V1PatchExperimentResponse
from determined._swagger.client.models.v1_patch_model_request import V1PatchModelRequest
from determined._swagger.client.models.v1_patch_model_response import V1PatchModelResponse
from determined._swagger.client.models.v1_pause_experiment_response import V1PauseExperimentResponse
from determined._swagger.client.models.v1_post_checkpoint_metadata_request import V1PostCheckpointMetadataRequest
from determined._swagger.client.models.v1_post_checkpoint_metadata_response import V1PostCheckpointMetadataResponse
from determined._swagger.client.models.v1_post_model_response import V1PostModelResponse
from determined._swagger.client.models.v1_post_model_version_request import V1PostModelVersionRequest
from determined._swagger.client.models.v1_post_model_version_response import V1PostModelVersionResponse
from determined._swagger.client.models.v1_post_trial_profiler_metrics_batch_request import V1PostTrialProfilerMetricsBatchRequest
from determined._swagger.client.models.v1_post_trial_profiler_metrics_batch_response import V1PostTrialProfilerMetricsBatchResponse
from determined._swagger.client.models.v1_post_user_request import V1PostUserRequest
from determined._swagger.client.models.v1_post_user_response import V1PostUserResponse
from determined._swagger.client.models.v1_preview_hp_search_request import V1PreviewHPSearchRequest
from determined._swagger.client.models.v1_preview_hp_search_response import V1PreviewHPSearchResponse
from determined._swagger.client.models.v1_put_template_response import V1PutTemplateResponse
from determined._swagger.client.models.v1_report_trial_checkpoint_metadata_response import V1ReportTrialCheckpointMetadataResponse
from determined._swagger.client.models.v1_report_trial_progress_response import V1ReportTrialProgressResponse
from determined._swagger.client.models.v1_report_trial_searcher_early_exit_response import V1ReportTrialSearcherEarlyExitResponse
from determined._swagger.client.models.v1_report_trial_training_metrics_response import V1ReportTrialTrainingMetricsResponse
from determined._swagger.client.models.v1_report_trial_validation_metrics_response import V1ReportTrialValidationMetricsResponse
from determined._swagger.client.models.v1_resource_allocation_aggregated_entry import V1ResourceAllocationAggregatedEntry
from determined._swagger.client.models.v1_resource_allocation_aggregated_response import V1ResourceAllocationAggregatedResponse
from determined._swagger.client.models.v1_resource_allocation_aggregation_period import V1ResourceAllocationAggregationPeriod
from determined._swagger.client.models.v1_resource_allocation_raw_entry import V1ResourceAllocationRawEntry
from determined._swagger.client.models.v1_resource_allocation_raw_response import V1ResourceAllocationRawResponse
from determined._swagger.client.models.v1_resource_pool import V1ResourcePool
from determined._swagger.client.models.v1_resource_pool_aws_detail import V1ResourcePoolAwsDetail
from determined._swagger.client.models.v1_resource_pool_detail import V1ResourcePoolDetail
from determined._swagger.client.models.v1_resource_pool_gcp_detail import V1ResourcePoolGcpDetail
from determined._swagger.client.models.v1_resource_pool_priority_scheduler_detail import V1ResourcePoolPrioritySchedulerDetail
from determined._swagger.client.models.v1_resource_pool_type import V1ResourcePoolType
from determined._swagger.client.models.v1_runnable_operation import V1RunnableOperation
from determined._swagger.client.models.v1_runnable_type import V1RunnableType
from determined._swagger.client.models.v1_scheduler_type import V1SchedulerType
from determined._swagger.client.models.v1_searcher_operation import V1SearcherOperation
from determined._swagger.client.models.v1_set_user_password_response import V1SetUserPasswordResponse
from determined._swagger.client.models.v1_shell import V1Shell
from determined._swagger.client.models.v1_slot import V1Slot
from determined._swagger.client.models.v1_template import V1Template
from determined._swagger.client.models.v1_tensorboard import V1Tensorboard
from determined._swagger.client.models.v1_training_length import V1TrainingLength
from determined._swagger.client.models.v1_training_metrics import V1TrainingMetrics
from determined._swagger.client.models.v1_trial_early_exit import V1TrialEarlyExit
from determined._swagger.client.models.v1_trial_logs_fields_response import V1TrialLogsFieldsResponse
from determined._swagger.client.models.v1_trial_logs_response import V1TrialLogsResponse
from determined._swagger.client.models.v1_trial_preemption_signal_response import V1TrialPreemptionSignalResponse
from determined._swagger.client.models.v1_trial_profiler_metric_labels import V1TrialProfilerMetricLabels
from determined._swagger.client.models.v1_trial_profiler_metrics_batch import V1TrialProfilerMetricsBatch
from determined._swagger.client.models.v1_trial_simulation import V1TrialSimulation
from determined._swagger.client.models.v1_trials_sample_response import V1TrialsSampleResponse
from determined._swagger.client.models.v1_trials_sample_response_trial import V1TrialsSampleResponseTrial
from determined._swagger.client.models.v1_trials_snapshot_response import V1TrialsSnapshotResponse
from determined._swagger.client.models.v1_trials_snapshot_response_trial import V1TrialsSnapshotResponseTrial
from determined._swagger.client.models.v1_unarchive_experiment_response import V1UnarchiveExperimentResponse
from determined._swagger.client.models.v1_user import V1User
from determined._swagger.client.models.v1_validate_after_operation import V1ValidateAfterOperation
from determined._swagger.client.models.v1_validation_history_entry import V1ValidationHistoryEntry
from determined._swagger.client.models.v1_validation_metrics import V1ValidationMetrics
