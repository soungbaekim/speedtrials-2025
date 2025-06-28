import pandas as pd
from sqlalchemy import create_engine

class Item:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

items = [
    Item("milestones", "src/data/SDWA_EVENTS_MILESTONES.csv"),
    Item("facilities", "src/data/SDWA_FACILITIES.csv"),
    Item("geographic_areas", "src/data/SDWA_GEOGRAPHIC_AREAS.csv"),
    Item("lcr_samples", "src/data/SDWA_LCR_SAMPLES.csv"),
    Item("pn_violation_assoc", "src/data/SDWA_PN_VIOLATION_ASSOC.csv"),
    Item("public_water_systems", "src/data/SDWA_PUB_WATER_SYSTEMS.csv"),
    Item("ref_code_values", "src/data/SDWA_REF_CODE_VALUES.csv"),
    Item("service_areas", "src/data/SDWA_SERVICE_AREAS.csv"),
    Item("site_visits", "src/data/SDWA_SITE_VISITS.csv"),
    Item("violations_enforcement", "src/data/SDWA_VIOLATIONS_ENFORCEMENT.csv"),
]


def main():
    for item in items:
        print(f"Loading {item.name}...")
        df = pd.read_csv(item.location)
        engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
        df.to_sql(item.name, engine, if_exists='append', index=False)

if __name__ == "__main__":
    main()