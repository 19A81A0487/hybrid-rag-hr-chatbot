def template_response(query, retrieved_emps):
    keywords = query.lower()
    min_exp = 3 if '3+' in keywords else 0

    filtered = [
        emp for emp in retrieved_emps
        if 'python' in [s.lower() for s in eval(emp['skills'])]
        and emp['experience_years'] >= min_exp
    ]

    if not filtered:
        return "❌ No matching employees found."

    lines = []
    for emp in filtered:
        line = f"- {emp['name']} ({emp['experience_years']} yrs) – Skills: {', '.join(eval(emp['skills']))} – Projects: {', '.join(eval(emp['past_projects']))} – Status: {emp['availability']}"
        lines.append(line)

    return f"✅ Found {len(filtered)} matching employee(s):\n\n" + "\n".join(lines)
