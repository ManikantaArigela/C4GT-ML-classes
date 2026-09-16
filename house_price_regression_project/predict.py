import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

DATA_FILE = "house_price_regression.csv"

def main():
    print("=" * 55)
    print("       HOUSE PRICE REGRESSION PREDICTOR")
    print("=" * 55)
    print("Enter the house details below.\n")

    try:
        area = float(input("Area in square feet: "))
        bedrooms = int(input("Number of bedrooms: "))
        age = float(input("House age in years: "))
        distance = float(input("Distance from city center (km): "))

        if area <= 0 or bedrooms <= 0 or age < 0 or distance < 0:
            raise ValueError

        df = pd.read_csv(DATA_FILE)
        X = df[["area_sqft", "bedrooms", "age_years", "distance_km"]]
        y = df["price_lakhs"]

        X_train, _, y_train, _ = train_test_split(
            X, y, test_size=0.20, random_state=42
        )

        model = LinearRegression()
        model.fit(X_train, y_train)

        user_house = pd.DataFrame([{
            "area_sqft": area,
            "bedrooms": bedrooms,
            "age_years": age,
            "distance_km": distance
        }])

        prediction = model.predict(user_house)[0]

        print("\n" + "=" * 55)
        print("             REGRESSION OUTPUT")
        print("=" * 55)
        print(f"Area       : {area:.0f} sqft")
        print(f"Bedrooms   : {bedrooms}")
        print(f"Age        : {age:.1f} years")
        print(f"Distance   : {distance:.1f} km")
        print("-" * 55)
        print(f"Predicted Price: ₹{prediction:.2f} lakhs")
        print("=" * 55)

    except ValueError:
        print("\nPlease enter valid numeric values.")
    except FileNotFoundError:
        print(f"\nCould not find {DATA_FILE}. Run this script from the project folder.")

if __name__ == "__main__":
    main()
