from datetime import datetime
def formater_temps(iso_string):

    if not iso_string or iso_string == "N/A":
        return "N/A"
    try:
        dt = datetime.fromisoformat(iso_string)
        return dt.strftime("%H:%M")
    except (ValueError, TypeError):
        return iso_string