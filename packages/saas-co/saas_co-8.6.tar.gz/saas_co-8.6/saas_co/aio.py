import os
import json
import asyncio
from typing import Any
from itertools import groupby
from functools import wraps, partial
from concurrent.futures import ThreadPoolExecutor

MAX_WORKERS = int(os.environ.get('MAX_WORKERS', '32'))
worker_pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)

def worker(func: Any) -> Any:
    """
    Runs blocking code asynchronously in worker thread from worker pool
    """
    @wraps(func)
    async def run(*args, **kwargs):
        pfunc = partial(func, *args, **kwargs)
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(worker_pool, pfunc)
    return run


@worker
def gather_data(account, region, instances):
    pass

def create_tasks(df, func=gather_data, account="account_id", region="region")
    records = json.loads(df.to_json(orient='records'))
    grouped_instances = groupby(records, lambda r: (r[account], r[region]))
    grouped_instances = {key: list(group) for key, group in grouped_instances}
    grouped_instances_dict = {key: list(group) for key, group in grouped_instances.items()}
    return [func(account, region, instances) for (account, region), instances in grouped_instances_dict.items()]    