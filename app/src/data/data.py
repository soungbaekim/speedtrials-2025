import pandas as pd
from sqlalchemy import create_engine

class Item:
    def __init__(self, name: str, location: str, date_columns: list[str] = []):
        self.name = name
        self.location = location
        self.date_columns = date_columns

items = [
    Item("milestones", "src/data/SDWA_EVENTS_MILESTONES.csv", [
            "EVENT_END_DATE",
            "EVENT_ACTUAL_DATE",
            "FIRST_REPORTED_DATE",
            "LAST_REPORTED_DATE"
        ]),
    Item("facilities", "src/data/SDWA_FACILITIES.csv", [
           "FACILITY_DEACTIVATION_DATE",
           "FIRST_REPORTED_DATE",
           "LAST_REPORTED_DATE"
        ]),
    Item("geographic_areas", "src/data/SDWA_GEOGRAPHIC_AREAS.csv", ["LAST_REPORTED_DATE"]),
    Item("lcr_samples", "src/data/SDWA_LCR_SAMPLES.csv", [
            "SAMPLING_END_DATE",
            "SAMPLING_START_DATE",
            "SAMPLE_FIRST_REPORTED_DATE",
            "SAMPLE_LAST_REPORTED_DATE",
            "SAR_FIRST_REPORTED_DATE",
            "SAR_LAST_REPORTED_DATE"
        ]),
    Item("pn_violation_assoc", "src/data/SDWA_PN_VIOLATION_ASSOC.csv", [
            "COMPL_PER_BEGIN_DATE",
            "COMPL_PER_END_DATE",
            "NON_COMPL_PER_BEGIN_DATE",
            "NON_COMPL_PER_END_DATE",
            "FIRST_REPORTED_DATE",
            "LAST_REPORTED_DATE"
        ]),
    Item("public_water_systems", "src/data/SDWA_PUB_WATER_SYSTEMS.csv", [
            "PWS_DEACTIVATION_DATE",
            "FIRST_REPORTED_DATE",
            "LAST_REPORTED_DATE",
            "SOURCE_PROTECTION_BEGIN_DATE",
            "OUTSTANDING_PERFORM_BEGIN_DATE",
            "REDUCED_MONITORING_BEGIN_DATE",
            "REDUCED_MONITORING_END_DATE"
        ]),
    Item("ref_code_values", "src/data/SDWA_REF_CODE_VALUES.csv"),
    Item("service_areas", "src/data/SDWA_SERVICE_AREAS.csv", [
            "FIRST_REPORTED_DATE",
            "LAST_REPORTED_DATE"
        ]),
    Item("site_visits", "src/data/SDWA_SITE_VISITS.csv", [
            "VISIT_DATE",
            "FIRST_REPORTED_DATE",
            "LAST_REPORTED_DATE"
        ]),
    Item("violations_enforcement", "src/data/SDWA_VIOLATIONS_ENFORCEMENT.csv",[
        "COMPL_PER_BEGIN_DATE",
        "COMPL_PER_END_DATE",
        "NON_COMPL_PER_BEGIN_DATE",
        "NON_COMPL_PER_END_DATE",
        "PWS_DEACTIVATION_DATE",
        "CALCULATED_RTC_DATE",
        "VIOL_FIRST_REPORTED_DATE",
        "VIOL_LAST_REPORTED_DATE",
        "ENFORCEMENT_DATE",
        "ENF_FIRST_REPORTED_DATE",
        "ENF_LAST_REPORTED_DATE"
    ]),
]


def main():
    for item in items:
        print(f"Loading {item.name}...")
        df = pd.read_csv(item.location, low_memory=False, parse_dates=item.date_columns, dayfirst=False)
        engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
        df.to_sql(item.name, engine, if_exists='append', index=False)

if __name__ == "__main__":
    main()