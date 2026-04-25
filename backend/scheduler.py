def priority_scheduling(tasks):
    return sorted(tasks, key=lambda x: x['priority'], reverse=True)


def greedy_allocation(tasks, total_resources=100):
    scheduled = priority_scheduling(tasks)

    result = []
    remaining = total_resources

    for task in scheduled:
        if remaining <= 0:
            break

        allocation = min(task['demand'], remaining)

        result.append({
            "task": task['name'],
            "priority": task['priority'],
            "allocated": allocation
        })

        remaining -= allocation

    return result