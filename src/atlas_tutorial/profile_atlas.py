import cProfile
import pstats
from atlas_logger import AtlasAgent
agent=AtlasAgent()
# 跑10000次chat
def run_benchmark():
    for i in range(10000):
        agent.chat(f"message {i}")
profiler=cProfile.Profile()
profiler.enable()
run_benchmark()
