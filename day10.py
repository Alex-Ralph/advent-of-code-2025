
def apply_button_press(indicators, button):
    return tuple([not indicators[i] if i in button else indicators[i] for i in range(len(indicators))])
    
class Machine:
    def __init__(self, indicators: tuple[bool], buttons: list[list[int]], joltages: list[int]):
        self.indicators = indicators
        self.buttons = buttons
        self.joltages = joltages
        
    def _get_shortest_button_presses(self, indicators):
        new_states = {apply_button_press(indicators, button) for button in self.buttons}
        if any(all(x) for x in new_states):
            return 1
        return new_states
    
    def get_shortest_button_presses(self) -> list[list[int]]:
        indicator_states = {tuple([False for _ in range(len(self.indicators))])}
        presses = 0
        while not any(x == self.indicators for x in indicator_states):
            presses += 1
            indicator_states = {apply_button_press(indicator, button) 
                                for indicator in indicator_states
                                for button in self.buttons}
        return presses


def parse_machine_string(machine_str: str) -> Machine:
    machine_parts = machine_str.split(" ")
    indicators = tuple(False if x == "." else True for x in machine_parts[0][1:-1])
    buttons = [[int(x) for x in y[1:-1].split(",")] for y in machine_parts[1:-1]]
    joltages = [int(x) for x in machine_parts[-1][1:-1].split(",")]
    return Machine(indicators, buttons, joltages)

with open("input/day10.txt") as file:
    machine_strings = file.read().splitlines()
    machines = [
        parse_machine_string(x) for x in machine_strings
    ]

print(sum(machine.get_shortest_button_presses() for machine in machines))