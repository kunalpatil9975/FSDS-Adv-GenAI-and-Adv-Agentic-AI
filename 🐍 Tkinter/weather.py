import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "d0c161e58e864ec683984756262307"  # Replace with your actual API key from weatherapi.com

# ---------------- Weather Function ---------------- #

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("Warning", "Please enter a city name")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            messagebox.showerror("Error", data["error"]["message"])
            return

        city_name = data["location"]["name"]
        country = data["location"]["country"]

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]

        result.config(
            text=f"""
City : {city_name}

Country : {country}

Temperature : {temp} °C

Condition : {condition}

Humidity : {humidity} %

Wind Speed : {wind} km/h
""")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Weather App")
root.geometry("420x500")
root.configure(bg="#1E1E2F")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Weather App",
    font=("Arial", 22, "bold"),
    bg="#1E1E2F",
    fg="white"
)
title.pack(pady=20)

city_entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center"
)
city_entry.pack(pady=10)

search_btn = tk.Button(
    root,
    text="Search",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    command=get_weather
)
search_btn.pack(pady=10)

result = tk.Label(
    root,
    text="Enter a city name",
    font=("Arial", 14),
    bg="#1E1E2F",
    fg="white",
    justify="left"
)
result.pack(pady=20)

root.mainloop()