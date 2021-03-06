# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ._common_ops import wait_for_job_done, cancel_job

from kfp_component.core import KfpExecutionContext
from ._client import MLEngineClient
from .. import common as gcp_common

def wait_job(project_id, job_id, wait_interval=30, show_tensorboard=True):
    """Waits a MLEngine job.

    Args:
        project_id (str): Required. The ID of the parent project of the job.
        job_id (str): Required. The ID of the job to wait.
        wait_interval (int): optional wait interval between calls
            to get job status. Defaults to 30.
        show_tensorboard (bool): optional. True to dump Tensorboard metadata.

    Outputs:
        /tmp/kfp/output/ml_engine/job.json: The json payload of the waiting job.
        /tmp/kfp/output/ml_engine/job_id.txt: The ID of the waiting job.
        /tmp/kfp/output/ml_engine/job_dir.txt: The `jobDir` of the waiting job.
    """
    ml_client = MLEngineClient()
    with KfpExecutionContext(on_cancel=lambda: cancel_job(ml_client, project_id, job_id)):
        return wait_for_job_done(ml_client, project_id, job_id, wait_interval, show_tensorboard = show_tensorboard)