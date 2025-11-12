from datetime import datetime

def generate_schedule(data, hours_per_day, exam_date):
    today = datetime.now()
    days_left = (exam_date - today).days

    if days_left <= 0:
        return [{"Subject": "Invalid", "Difficulty": "-", "Hours": "Exam date passed"}]

    total_weight = 0
    for _, diff in data:
        if diff.lower() == "hard":
            total_weight += 3
        elif diff.lower() == "medium":
            total_weight += 2
        else:
            total_weight += 1

    schedule = []
    for subject, diff in data:
        if diff.lower() == "hard":
            weight = 3
        elif diff.lower() == "medium":
            weight = 2
        else:
            weight = 1

        hours = round((weight / total_weight) * hours_per_day, 2)
        schedule.append({
            "Subject": subject,
            "Difficulty": diff,
            "Hours": f"{hours} hrs/day"
        })

    return schedule
