import mlrun
from kfp import dsl

from mlrun import run_function

def kfpipeline():
    step1 = run_function(function="steps",
                        name="step",
                        handler="step",
                        hyperparams={
                            "param1": [100, 500, 1000], 
                            "param2": [5, 15, 30]
                        }, 
                        selector="max.result")
