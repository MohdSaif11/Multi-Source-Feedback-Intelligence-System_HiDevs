from google_play_scraper import reviews

def fetch_playstore_reviews(app_id, count=100):
    result, _ = reviews(app_id, count=count)
    
    data = []
    for r in result:
        data.append({
            "text": r["content"],
            "rating": r["score"]
        })
    
    return data
