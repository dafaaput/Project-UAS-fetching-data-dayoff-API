import requests


def fetch_dayOffAPI(year=None, month=None):
    url = "https://dayoffapi.vercel.app/api"
    params = {}

    if year is not None:
        params["year"] = year

    if month is not None:
        params["month"] = month

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        holidays_data = response.json()

        return holidays_data

    except requests.exceptions.RequestException as error:
        print(f"Error fetching data from API: {error}")
        return None


def main():
    current_year_data = fetch_dayOffAPI(year=2020, month=5)
    if current_year_data:
        print(f"\nHari libur tahun 2020:\n")
        for holiday in current_year_data:
            print(f"{holiday['tanggal']}: {holiday['keterangan']}")


if __name__ == "__main__":
    main()