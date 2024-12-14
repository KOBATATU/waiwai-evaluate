# Local Development

## Introduction

Thank you for viewing this document. This document provides instructions for setting up and running the development environment locally.

## Preparation

- The environment setup for the waiwai repository is complete.

Once the preparation is complete, please execute the following command. The initial setup is now complete.

`docker-compose up`

## Environment Variables

The environment variables are as follows:

```bash
# .env
GCS_BUCKET=
GCS_CREDENTIAL=
DATABASE_URL=postgresql://user:postgres@host.docker.internal:5432/waiwai
```

The above environment variable settings are the same as those configured in the `waiwai` repository. Please refer to the [documentation here](https://github.com/KOBATATU/waiwai/blob/main/docs/local_development.md).

## Preparing Evaluation Data

For details on the data, please see [this link](https://github.com/KOBATATU/waiwai/blob/main/docs/local_development.md#answer-data).
