"""
main should be set as the entry point for Google Cloud function
"""
import periodic_scraper as ps


def main(data, context):
    print("debug in main")
    reasonable_mp_update_frequency = 7
    ps.insert_and_update_data(day_frequency_for_party_and_mp_data=reasonable_mp_update_frequency)

