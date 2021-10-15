import torch
import torch.distributed.rpc as rpc
import os
os.environ['MASTER_ADDR'] = 'localhost'
os.environ['MASTER_PORT'] = '5678'
print("good")
rpc.init_rpc("worker0", rank=0, world_size=2)
fut1 = rpc.rpc_async("worker1", torch.add, args=(torch.ones(2), 3))
fut2 = rpc.rpc_async("worker1", min, args=(1, 2))
result = fut1.wait() + fut2.wait()
print(result)
rpc.shutdown()