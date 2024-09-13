def balance_load(machine_usage, max_load):
    total_usage = sum(machine_usage)
    if total_usage > max_load:
        print("Overload! Redistributing load.")
        machine_usage = [usage - (total_usage - max_load) / len(machine_usage) for usage in machine_usage]
    return machine_usage

machine_usage = [40, 35, 50, 60]
max_load = 150
balanced_load = balance_load(machine_usage, max_load)
print("Balanced Machine Usage:", balanced_load)
