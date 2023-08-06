from diffusers import (
    DDIMScheduler,
    EulerAncestralDiscreteScheduler,
    EulerDiscreteScheduler,
    HeunDiscreteScheduler,
    LMSDiscreteScheduler,
)

SCHEDULER_LIST = [
    "DDIM",
    "EulerA",
    "Euler",
    "LMS",
    "Heun",
]


def get_scheduler_list(pipe, scheduler):
    if scheduler == SCHEDULER_LIST[0]:
        pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)

    elif scheduler == SCHEDULER_LIST[1]:
        pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(
            pipe.scheduler.config
        )

    elif scheduler == SCHEDULER_LIST[2]:
        pipe.scheduler = EulerDiscreteScheduler.from_config(
            pipe.scheduler.config
        )

    elif scheduler == SCHEDULER_LIST[3]:
        pipe.scheduler = LMSDiscreteScheduler.from_config(pipe.scheduler.config)

    elif scheduler == SCHEDULER_LIST[4]:
        pipe.scheduler = HeunDiscreteScheduler.from_config(
            pipe.scheduler.config
        )

    return pipe
