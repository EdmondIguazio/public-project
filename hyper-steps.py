import mlrun
from mlrun.execution import MLClientCtx
import time

def step(context:MLClientCtx, param1: int, param2: int):
    
    context.logger.info('Step - Begin')
    
    context.log_result("result", param1 * param2)
    
    context.logger.info('Step - End')
