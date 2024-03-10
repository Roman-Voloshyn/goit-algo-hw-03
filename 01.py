from datetime import datetime


get_days_from_today = lambda date: (datetime.today() - datetime.fromisoformat(date)).days
