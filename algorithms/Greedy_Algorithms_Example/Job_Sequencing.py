def jobScheduling(jobs):
    
    # Sort the jobs based on their profit in descending order
    jobs.sort(key = lambda x: x[2], reverse=True )
    
    # Find the maximum deadline among all the jobs
    max_deadline = max(job[1] for job in jobs)
    
    schedule = [None] * max_deadline
    
    total_profit = 0
    
    # Schedule jobs within their respective deadlines
    for job in jobs:
        deadline = job[1]
        
        # Find an available slot in the schedule for the current job
        while deadline > 0 and schedule[deadline-1] is not None:
            deadline -= 1
        
        # If an available slot is found, schedule the job at that slot and update the total profit
        if deadline > 0:
            schedule[deadline-1] = job[0]
            total_profit += job[2]
                
    return schedule, total_profit


if __name__ == "__main__":
    jobs = [
        ['A', 2, 100],  
        ['B', 1, 19],
        ['C', 2, 27],
        ['D', 1, 25],
        ['E', 3, 15]
    ]
        
    result, profit = jobScheduling(jobs)
    print("Total Profit:", profit)
    print("Schedule:", result)
    