def calculate_stats(df):
    if df.empty:
        return None

    total = len(df)

    status_counts = df['status'].value_counts()

    stats = {
        "total": total,
        "success": status_counts.get("success", 0),
        "city_not_found": status_counts.get("city_not_found", 0),
        "errors": status_counts.get("error", 0),
        "users": df['user_id'].nunique(),
        "top_cities": df[df['status'] == 'success']['city'].value_counts().head(5)
    }

    df['date'] = df['timestamp'].dt.date
    stats["daily"] = df.groupby('date').size()

    stats["top_users"] = df['username'].value_counts().head(5)

    return stats