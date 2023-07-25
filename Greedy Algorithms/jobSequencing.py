def job_sequencing(jobs):
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)  # Sort jobs by profit in descending order
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    schedule = [-1] * max_deadline

    for job in jobs:
        deadline = job[1]
        slot = deadline - 1

        while slot >= 0:
            if schedule[slot] == -1:
                schedule[slot] = job[0]
                break
            slot -= 1

    return [job_id for job_id in schedule if job_id != -1]


# Example usage
jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]

scheduled_jobs = job_sequencing(jobs)
print("Job sequence:", scheduled_jobs)