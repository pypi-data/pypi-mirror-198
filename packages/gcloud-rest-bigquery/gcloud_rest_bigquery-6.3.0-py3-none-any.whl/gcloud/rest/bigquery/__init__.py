"""
This library implements various methods for working with the Google Bigquery
APIs.

## Installation

```console
$ pip install --upgrade gcloud-rest-bigquery
```

## Usage

We're still working on documentation -- for now, you can use the
[smoke test][smoke-test] as an example.

## Emulators

For testing purposes, you may want to use `gcloud-rest-bigquery` along with a
local emulator. Setting the `$BIGQUERY_EMULATOR_HOST` environment variable to
the address of your emulator should be enough to do the trick.

[smoke-test]:
https://github.com/talkiq/gcloud-rest/blob/master/bigquery/tests/integration/smoke_test.py
"""
from pkg_resources import get_distribution
__version__ = get_distribution('gcloud-rest-bigquery').version

from gcloud.rest.bigquery.bigquery import Disposition
from gcloud.rest.bigquery.bigquery import SCOPES
from gcloud.rest.bigquery.bigquery import SchemaUpdateOption
from gcloud.rest.bigquery.bigquery import SourceFormat
from gcloud.rest.bigquery.dataset import Dataset
from gcloud.rest.bigquery.job import Job
from gcloud.rest.bigquery.table import Table
from gcloud.rest.bigquery.utils import query_response_to_dict


__all__ = [
    'Dataset',
    'Disposition',
    'Job',
    'SCOPES',
    'SchemaUpdateOption',
    'SourceFormat',
    'Table',
    '__version__',
    'query_response_to_dict',
]
