import streamlit as st
import pandas as pd
import joblib

model = joblib.load("airbnb_price_pipeline.pkl")

st.title("Airbnb Price Prediction")

st.write("Enter the Airbnb listing details to estimate the nightly price.")

# User inputs

neighbourhood_group = st.selectbox(
    "Neighbourhood Group",
    ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"]
)

neighbourhood = st.text_input(
    "Neighbourhood",
    "Harlem"
)

room_type = st.selectbox(
    "Room Type",
    ["Entire home/apt", "Private room", "Shared room"]
)

latitude = st.number_input(
    "Latitude",
    value=40.80
)

longitude = st.number_input(
    "Longitude",
    value=-73.95
)

minimum_nights = st.number_input(
    "Minimum Nights",
    min_value=1,
    value=3
)

number_of_reviews = st.number_input(
    "Number of Reviews",
    min_value=0,
    value=10
)

reviews_per_month = st.number_input(
    "Reviews Per Month",
    min_value=0.0,
    value=1.0
)

calculated_host_listings_count = st.number_input(
    "Host Listings Count",
    min_value=1,
    value=1
)

availability_365 = st.number_input(
    "Availability (Days per Year)",
    min_value=0,
    max_value=365,
    value=180
)

#  engineered features

has_reviews = 1 if number_of_reviews > 0 else 0

is_multi_listing_host = (
    1 if calculated_host_listings_count > 1 else 0
)

# Prediction button

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "neighbourhood_group": [neighbourhood_group],
        "neighbourhood": [neighbourhood],
        "latitude": [latitude],
        "longitude": [longitude],
        "room_type": [room_type],
        "minimum_nights": [minimum_nights],
        "number_of_reviews": [number_of_reviews],
        "reviews_per_month": [reviews_per_month],
        "calculated_host_listings_count": [calculated_host_listings_count],
        "availability_365": [availability_365],
        "has_reviews": [has_reviews],
        "is_multi_listing_host": [is_multi_listing_host]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Nightly Price: ${prediction:.2f}"
    )