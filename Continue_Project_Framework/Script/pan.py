import pandas as pd

def test_pandas_basic():
    try:
        # Create simple data
        data = {
            "Name": ["Deepak", "John", "Alice"],
            "Age": [28, 30, 25]
        }

        # Create DataFrame
        df = pd.DataFrame(data)

        Log.Message("DataFrame:")
        Log.Message(str(df))

        # Calculate average age
        avg_age = df["Age"].mean()
        Log.Message("Average Age: " + str(avg_age))

    except Exception as e:
        Log.Error("Pandas error: " + str(e))