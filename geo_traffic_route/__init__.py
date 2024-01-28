import os

import pandas as pd

root_path = os.path.dirname(os.path.dirname(__file__))


def project_filepath(rel_path: str):
    return os.path.join(root_path, rel_path)


def processed_airports_data():
    airports_file = project_filepath('data/processed/airports_with_iata.csv')

    if not os.path.exists(airports_file):
        airports_raw_file = project_filepath('data/raw/airports.csv')
        airports = pd.read_csv(airports_raw_file,
                               usecols=['iata_code', 'name', 'type', 'iso_country',
                                        'iso_region', 'latitude_deg', 'longitude_deg'])

        airports = airports.dropna(subset=['iata_code'])[['iata_code', 'name', 'type', 'iso_country',
                                                          'iso_region', 'latitude_deg', 'longitude_deg']]

        airports.to_csv(airports_file, index=False)

    airports = pd.read_csv(airports_file)

    airports.set_index('iata_code', inplace=True)

    return airports.to_dict(orient='index')


__all__ = ['route']
