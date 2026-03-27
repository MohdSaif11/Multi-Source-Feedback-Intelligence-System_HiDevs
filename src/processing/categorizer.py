def categorize(text):
    if "crash" in text or "error" in text:
        return "bug"
    elif "feature" in text:
        return "feature request"
    else:
        return "general"
        