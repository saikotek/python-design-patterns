"""
Python State Machine

If you need more advanced features, instead of implementing your own state machine,
you can use off-the-shelf state machine library.

Example: Traffic light state machine
"""
import asyncio
from statemachine import StateMachine, State

class TrafficLightMachine(StateMachine):
    """A traffic light state machine"""
    green = State('Green', initial=True)
    yellow = State('Yellow')
    red = State('Red')

    slowdown = green.to(yellow)
    stop = yellow.to(red)
    go = red.to(green)

    cycle = slowdown | stop | go

    async def before_cycle(self,
                           event: str,
                           source: State,
                           target: State,
                           message: str = ""):
        message = ". " + message if message else ""
        print(f"{event}: Changing state {source} -> {target}{message}")

    def on_enter_red(self):
        print("Stop! The light is RED")

    def on_enter_green(self):
        print("Go! The light is GREEN")

    def on_enter_yellow(self):
        print("Caution! The light is YELLOW")


async def run_sm():
    traffic_light = TrafficLightMachine()
    for _ in range(3):
        await traffic_light.send('cycle')


# Example usage:
if __name__ == "__main__":
    asyncio.run(run_sm())