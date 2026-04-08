#21
import pandas as pd
from datetime import date

def users_dateframe(users):
    data=[]
    for user in users:
        data.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "registration_date": user.registration_date
        })
    return pd.DataFrame(data)