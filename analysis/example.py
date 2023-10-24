# %% [markdown]
# # Example of `dask` Hello World

# %%
import ROOT
import awkward
import dask
from dask.distributed import Client

# %% [markdown]
# Following https://distributed.dask.org/en/latest/client.html

# %%
client = Client()
client


# %%
def inc(x):
    return x + 1


# %%
x = client.submit(inc, 10)
x

# %%
L = client.map(inc, range(30))
L

# %%
x.result()

# %%
client.gather(L)
