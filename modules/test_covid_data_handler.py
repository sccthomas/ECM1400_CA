"""[A python module to test the covid_data_handler.py and its methods]
    """
from covid_data_handler import *

data = [{'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-29',
         'Cumulative Deaths': None, 'New Hospital Admssions': None, 'Daily Cases': None},
        {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-28',
         'Cumulative Deaths': None, 'New Hospital Admssions': 5000, 'Daily Cases': 117},
        {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-27',
         'Cumulative Deaths': 144909, 'New Hospital Admssions': 4500, 'Daily Cases': 84},
        {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-26',
         'Cumulative Deaths': 144867, 'New Hospital Admssions': 4000, 'Daily Cases': 83},
        {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-25',
         'Cumulative Deaths': 144823, 'New Hospital Admssions': 3500, 'Daily Cases': None},
        {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-25',
         'Cumulative Deaths': 144798, 'New Hospital Admssions': 3000, 'Daily Cases': 111},
        {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-25',
         'Cumulative Deaths': 144746, 'New Hospital Admssions': 2500, 'Daily Cases': 170},
        {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-25',
         'Cumulative Deaths': 144734, 'New Hospital Admssions': 2000, 'Daily Cases': 44},
        {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-25',
         'Cumulative Deaths': 144703, 'New Hospital Admssions': 1500, 'Daily Cases': 75}]

full_data = {'data': [{'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-29',
                      'Cumulative Deaths': None, 'New Hospital Admssions': None, 'Daily Cases': None},
             {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-28',
              'Cumulative Deaths': None, 'New Hospital Admssions': 5000, 'Daily Cases': 117},
             {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-27',
              'Cumulative Deaths': 144909, 'New Hospital Admssions': 4500, 'Daily Cases': 84},
             {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-26',
              'Cumulative Deaths': 144867, 'New Hospital Admssions': 4000, 'Daily Cases': 83},
             {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-25',
              'Cumulative Deaths': 144823, 'New Hospital Admssions': 3500, 'Daily Cases': None},
             {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-25',
              'Cumulative Deaths': 144798, 'New Hospital Admssions': 3000, 'Daily Cases': 111},
             {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-25',
              'Cumulative Deaths': 144746, 'New Hospital Admssions': 2500, 'Daily Cases': 170},
             {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-25',
              'Cumulative Deaths': 144734, 'New Hospital Admssions': 2000, 'Daily Cases': 44},
             {'Area Code': 'E07000041', 'Area Name': 'Exeter', 'Area Type': 'ltla', 'Date': '2021-11-25',
              'Cumulative Deaths': 144703, 'New Hospital Admssions': 1500, 'Daily Cases': 75}],
             'lastUpdate': '2021-11-30T17:30:01.000000Z', 'length': 638, 'totalPages': 1, 'location type': 'ltla'}


def test_parse_csv_data():
    """[A function that tests the parse_csv_data methods]
    """
    data = parse_csv_data('nation_2021-10-28.csv')
    assert len(data) == 639


def test_process_covid_csv_data():
    """[A function to test the process_covid_csv_data function]
    """
    last7days_cases, current_hospital_cases, total_deaths = \
        process_covid_csv_data(parse_csv_data(
            'nation_2021-10-28.csv'))
    assert last7days_cases == 240_299
    assert current_hospital_cases == 7_019
    assert total_deaths == 141_544


def test_covid_API_request():
    """[A function to test the API request method]
    """
    data = covid_API_request()
    assert isinstance(data, dict)


def test_schedule_covid_updates():
    """[A function to test the schedule_covid_updates module]
    """
    schedule_covid_updates(update_interval=10, update_name='update test')


def test_find_latest_json_data():
    """[A function to test the find_latest_json_data method]
    """
    data_cumulative_deaths = find_latest_json_data(data, 'Cumulative Deaths')
    data_hospital_admissions = find_latest_json_data(
        data, 'New Hospital Admssions')
    assert data_cumulative_deaths == 144909
    assert data_hospital_admissions == 5000


def test_cumulative_data():
    """[A function to test the cumulative_data method]
    """
    data_cumulative_cases = cumulative_data(data)
    assert data_cumulative_cases == 565


def test_process_covid_json_data():
    """[A function to test the process_covid_json_data method]
    """
    results = process_covid_json_data(full_data)  # specimin data
    assert results['7_days_infection'] == 609
    assert results['Hospital_cases'] == 5000
    assert results['Total_deaths'] == 144909
