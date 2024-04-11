from prefect import flow

hello = flow.from_source(
    source="https://github.com/EmilRex/prefect-docker-compose.git",
    entrypoint="flows/hello.py:hello",
)

hello.deploy(
    name="hello-process",
    work_pool_name="process",
)

hello.deploy(
    name="hello-docker",
    work_pool_name="docker",
    job_variables={"networks": ["prefect"]},
)
