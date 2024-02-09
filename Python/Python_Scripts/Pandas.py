import pandas as pd
import json
df={
    "name":['isha'],
    "ae":[25],
    "phone_number":[8905674321]
}
data=pd.DataFrame(df)
print(data)

lo=json.dumps(df)
print(lo)


