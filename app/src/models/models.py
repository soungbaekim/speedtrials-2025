from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Milestones(Base):
    """
    SUBMISSIONYEARQUARTER,PWSID,EVENT_SCHEDULE_ID,EVENT_END_DATE,EVENT_ACTUAL_DATE,EVENT_COMMENTS_TEXT,EVENT_MILESTONE_CODE,EVENT_REASON_CODE,FIRST_REPORTED_DATE,LAST_REPORTED_DATE
    2025Q1,GA0010000,1,,03/10/1993,,DEEM,B1,11/15/2005,05/18/2007
    2025Q1,GA0010000,2,,03/10/1993,,DEEM,B1,09/22/2004,09/22/2004
    2025Q1,GA0010001,2,,03/09/1994,,DEEM,B1,11/15/2005,05/18/2007
    2025Q1,GA0010001,3,,03/09/1994,,DEEM,B1,09/22/2004,09/22/2004
    2025Q1,GA0010002,3,,02/22/1994,,DEEM,B1,11/15/2005,05/18/2007
    2025Q1,GA0010002,4,,02/22/1994,,DEEM,B1,09/22/2004,09/22/2004
    """
    __tablename__ = 'milestones'

    id = Column(Integer, primary_key=True)
    submission_year_quarter = Column(String)
    pwsid = Column(String)
    event_schedule_id = Column(String)
    event_end_date = Column(String)
    event_actual_date = Column(String)
    event_comments_text = Column(String)
    event_milestone_code = Column(String)
    event_reason_code = Column(String)
    first_reported_date = Column(String)
    last_reported_date = Column(String)

class Facilities(Base):
    """
    SUBMISSIONYEARQUARTER,PWSID,FACILITY_ID,FACILITY_NAME,STATE_FACILITY_ID,FACILITY_ACTIVITY_CODE,FACILITY_DEACTIVATION_DATE,FACILITY_TYPE_CODE,SUBMISSION_STATUS_CODE,IS_SOURCE_IND,WATER_TYPE_CODE,AVAILABILITY_CODE,SELLER_TREATMENT_CODE,SELLER_PWSID,SELLER_PWS_NAME,FILTRATION_STATUS_CODE,IS_SOURCE_TREATED_IND,FIRST_REPORTED_DATE,LAST_REPORTED_DATE
    2025Q1,GA0010000,10157,DISTRIBUTION SYSTEM,950,A,,DS,Y,N,,,,,,,,,03/20/2025
    2025Q1,GA0010000,2,102 NW PARK AVE WELL #1 PLANT,201,I,04/04/2010,TP,Y,N,,,,,,,,,03/20/2025
    2025Q1,GA0010000,22394,WEST INDUSTRIAL PARK WELL #5,105,A,,WL,Y,Y,GW,P,,,,,,03/01/2012,03/20/2025
    2025Q1,GA0010000,22395,WEST INDUSTRIAL PARK WELL #5 PLANT,205,A,,TP,Y,N,,,,,,,,03/01/2012,03/20/2025
    2025Q1,GA0010000,3299,465 FAIR ST WELL #3 PLANT,203,A,,TP,Y,N,,,,,,,,,03/20/2025
    2025Q1,GA0010000,3595,267 FORST IND. BLVD. WELL #4 PLANT,204,A,,TP,Y,N,,,,,,,,,03/20/2025
    2025Q1,GA0010000,4050,102 NW PARK AVE WELL #1,101,I,05/04/2010,WL,Y,Y,GW,O,,,,,Y,,03/20/2025
    2025Q1,GA0010000,4051,465 FAIR ST WELL #3,103,A,,WL,Y,Y,GW,P,,,,,Y,,03/20/2025
    """
    __tablename__ = 'facilities'

    id = Column(Integer, primary_key=True)
    submission_year_quarter = Column(String)
    pwsid = Column(String)
    facility_id = Column(String)
    facility_name = Column(String)
    state_facility_id = Column(String)
    facility_activity_code = Column(String)
    facility_deactivation_date = Column(String)
    facility_type_code = Column(String)
    submission_status_code = Column(String)
    is_source_ind = Column(String)
    water_type_code = Column(String)
    availability_code = Column(String)
    seller_treatment_code = Column(String)
    seller_pwsid = Column(String)
    seller_pws_name = Column(String)
    filtration_status_code = Column(String)
    is_source_treated_ind = Column(String)
    first_reported_date = Column(String)
    last_reported_date = Column(String)
    
class GeographicAreas(Base):
    """
    SUBMISSIONYEARQUARTER,PWSID,GEO_ID,AREA_TYPE_CODE,TRIBAL_CODE,STATE_SERVED,ANSI_ENTITY_CODE,ZIP_CODE_SERVED,CITY_SERVED,COUNTY_SERVED,LAST_REPORTED_DATE
    2025Q1,GA0010000,9109805,CN,,,001,,,Appling,03/20/2025
    2025Q1,GA0010000,9109806,CT,,GA,,,BAXLEY,,03/20/2025
    2025Q1,GA0010001,9109807,CN,,,001,,,Appling,03/20/2025
    2025Q1,GA0010001,9109808,CT,,GA,,,SURRENCY,,03/20/2025
    2025Q1,GA0010002,9109809,CN,,,001,,,Appling,03/20/2025
    2025Q1,GA0010002,9109810,CT,,GA,,,BAXLEY,,03/20/2025
    2025Q1,GA0010003,9109811,CN,,,001,,,Appling,03/20/2025
    """
    __tablename__ = 'geographic_areas'

    id = Column(Integer, primary_key=True)
    submission_year_quarter = Column(String)
    pwsid = Column(String)
    geo_id = Column(String)
    area_type_code = Column(String)
    tribal_code = Column(String)
    state_served = Column(String)
    ansi_entity_code = Column(String)
    zip_code_served = Column(String)
    city_served = Column(String)
    county_served = Column(String)
    last_reported_date = Column(String)

class LCRSamples(Base):
    """
    SUBMISSIONYEARQUARTER,PWSID,SAMPLE_ID,SAMPLING_END_DATE,SAMPLING_START_DATE,RECONCILIATION_ID,SAMPLE_FIRST_REPORTED_DATE,SAMPLE_LAST_REPORTED_DATE,SAR_ID,CONTAMINANT_CODE,RESULT_SIGN_CODE,SAMPLE_MEASURE,UNIT_OF_MEASURE,SAR_FIRST_REPORTED_DATE,SAR_LAST_REPORTED_DATE
    2025Q1,GA0510092,GA25428,12/31/2009,01/01/2007,,11/16/2007,12/03/2008,14001676,PB90,,.0025,mg/L,11/16/2007,12/03/2008
    2025Q1,GA1850019,GA25642,12/31/2007,01/01/2007,,11/16/2007,02/16/2010,14003550,PB90,,.0025,mg/L,11/16/2007,02/16/2010
    2025Q1,GA0510067,GA25372,12/31/2009,01/01/2007,,11/16/2007,12/03/2008,14001659,PB90,,.0012,mg/L,11/16/2007,12/03/2008
    2025Q1,GA0510089,GA24831,12/31/2007,01/01/2007,,11/16/2007,08/18/2009,14001672,PB90,,.0026,mg/L,11/16/2007,08/18/2009
    2025Q1,GA0510104,GA24817,12/31/2007,01/01/2007,,11/16/2007,02/24/2014,14001699,PB90,,.0025,mg/L,11/16/2007,02/24/2014
    2025Q1,GA0510070,GA25207,12/31/2009,01/01/2007,,11/16/2007,08/26/2008,14001660,PB90,,0,mg/L,11/16/2007,08/26/2008
    """
    __tablename__ = 'lcr_samples'

    id = Column(Integer, primary_key=True)
    submission_year_quarter = Column(String)
    pwsid = Column(String)
    sample_id = Column(String)
    sampling_end_date = Column(String)
    sampling_start_date = Column(String)
    reconciliation_id = Column(String)
    sample_first_reported_date = Column(String)
    sample_last_reported_date = Column(String)
    sar_id = Column(String)
    contaminant_code = Column(String)
    result_sign_code = Column(String)
    sample_measure = Column(String)
    unit_of_measure = Column(String)
    sar_first_reported_date = Column(String)
    sar_last_reported_date = Column(String)

class PNViolation(Base):
    """
    SUBMISSIONYEARQUARTER,PWSID,PN_VIOLATION_ID,RELATED_VIOLATION_ID,COMPL_PER_BEGIN_DATE,COMPL_PER_END_DATE,NON_COMPL_PER_BEGIN_DATE,NON_COMPL_PER_END_DATE,VIOLATION_CODE,CONTAMINANT_CODE,FIRST_REPORTED_DATE,LAST_REPORTED_DATE
    2025Q1,GA0510000,11619,11617,09/01/2019,09/30/2019,09/01/2019,09/30/2019,1A,8000,11/12/2019,06/27/2023
    2025Q1,GA2790015,42541,41410,04/01/2009,06/30/2009,04/01/2009,06/30/2009,02,4010,05/04/2018,03/17/2021
    2025Q1,GA2790015,42541,41510,07/01/2009,09/30/2009,07/01/2009,09/30/2009,02,4010,05/04/2018,03/17/2021
    2025Q1,GA2790015,42541,41610,10/01/2009,12/31/2009,10/01/2009,12/31/2009,02,4010,05/04/2018,03/17/2021
    2025Q1,GA2790015,42541,41710,01/01/2010,03/31/2010,01/01/2010,03/31/2010,02,4010,05/04/2018,03/17/2021
    2025Q1,GA2790015,42541,42212,07/01/2011,09/30/2011,07/01/2011,09/30/2011,02,4010,05/04/2018,03/17/2021
    """
    __tablename__ = 'pn_violation'

    id = Column(Integer, primary_key=True)
    submission_year_quarter = Column(String)
    pwsid = Column(String)
    pn_violation_id = Column(String)
    related_violation_id = Column(String)
    compl_per_begin_date = Column(String)
    compl_per_end_date = Column(String)
    non_compl_per_begin_date = Column(String)
    non_compl_per_end_date = Column(String)
    violation_code = Column(String)
    contaminant_code = Column(String)
    first_reported_date = Column(String)
    last_reported_date = Column(String)
    
class PublicWaterSystem(Base):
    """
    SUBMISSIONYEARQUARTER,PWSID,PWS_NAME,PRIMACY_AGENCY_CODE,EPA_REGION,SEASON_BEGIN_DATE,SEASON_END_DATE,PWS_ACTIVITY_CODE,PWS_DEACTIVATION_DATE,PWS_TYPE_CODE,DBPR_SCHEDULE_CAT_CODE,CDS_ID,GW_SW_CODE,LT2_SCHEDULE_CAT_CODE,OWNER_TYPE_CODE,POPULATION_SERVED_COUNT,POP_CAT_2_CODE,POP_CAT_3_CODE,POP_CAT_4_CODE,POP_CAT_5_CODE,POP_CAT_11_CODE,PRIMACY_TYPE,PRIMARY_SOURCE_CODE,IS_GRANT_ELIGIBLE_IND,IS_WHOLESALER_IND,IS_SCHOOL_OR_DAYCARE_IND,SERVICE_CONNECTIONS_COUNT,SUBMISSION_STATUS_CODE,ORG_NAME,ADMIN_NAME,EMAIL_ADDR,PHONE_NUMBER,PHONE_EXT_NUMBER,FAX_NUMBER,ALT_PHONE_NUMBER,ADDRESS_LINE1,ADDRESS_LINE2,CITY_NAME,ZIP_CODE,COUNTRY_CODE,FIRST_REPORTED_DATE,LAST_REPORTED_DATE,STATE_CODE,SOURCE_WATER_PROTECTION_CODE,SOURCE_PROTECTION_BEGIN_DATE,OUTSTANDING_PERFORMER,OUTSTANDING_PERFORM_BEGIN_DATE,REDUCED_RTCR_MONITORING,REDUCED_MONITORING_BEGIN_DATE,REDUCED_MONITORING_END_DATE,SEASONAL_STARTUP_SYSTEM
    2025Q1,GA0010000,BAXLEY,GA,04,,,A,,CWS,4,,GW,,L,5749,1,2,1,3,5,State,GW,Y,N,N,2576,Y,"MULLIS, CLIFFORD W","MULLIS, CLIFFORD W",wmullis@baxley.org,912-367-8314,,912-367-8324,,P.O. Box 290,,BAXLEY,31515,US,03/12/1980,03/20/2025,GA,Y,05/17/2018,Y,09/27/2013,,,,
    2025Q1,GA0010001,SURRENCY,GA,04,,,A,,CWS,4,,GW,,L,468,1,1,1,1,2,State,GW,Y,N,N,160,Y,"WEBSTER, PAT","WEBSTER, PAT",surrency@bellsouth.net,912-367-3816,,912-367-3816,,P. O. BOX 162,,SURRENCY,31563-0162,US,03/12/1980,03/20/2025,GA,Y,02/25/2007,N,,,,,
    2025Q1,GA0010002,ALTAMAHA ELEMENTARY SCHOOL,GA,04,01-01,12-31,A,,NTNCWS,4,,GW,,L,420,1,1,1,1,2,State,GW,Y,N,Y,4,Y,"MCBRIDE, BRENT","MCBRIDE, BRENT",brent.mcbride@appling.k12.ga.us,912-705-8119,,912-367-1011,,249 Blackshear Hwy,,BAXLEY,31513,US,03/12/1980,03/20/2025,GA,Y,10/24/2016,,,,,,
    2025Q1,GA0010003,FOURTH DISTRICT ELEM. SCHOOL,GA,04,01-01,12-31,A,,NTNCWS,4,,GW,,L,200,1,1,1,1,2,State,GW,Y,N,Y,1,Y,"MCBRIDE, BRENT","MCBRIDE, BRENT",brent.mcbride@appling.k12.ga.us,912-705-8119,,912-367-1011,,249 Blackshear Hwy,,BAXLEY,31513,US,03/12/1980,03/20/2025,GA,Y,10/24/2016,,,,,,
    2025Q1,GA0010005,SOUTHERN NUCLEAR-PLANT HATCH,GA,04,01-01,12-31,A,,NTNCWS,4,,GW,,P,950,1,1,1,2,3,State,GW,Y,N,N,1,Y,"GROCE, CASEY","GROCE, CASEY",cgroce@southernco.com,205-992-6443,,,,3535 Colonnade Parkway,BIN N-218-EC,BIRMINGHAM,35243,US,03/12/1980,03/20/2025,AL,Y,08/12/2019,,,,,,
    2025Q1,GA0010006,GA BAPTIST CHILDREN`S HOME - BAXLEY,GA,04,,,A,,CWS,4,,GW,,P,58,1,1,1,1,1,State,GW,Y,N,N,15,Y,"SHUMANS, MIKE","SHUMANS, MIKE",,912-367-6691,,912-367-2268,,9420 BLACKSHEAR HIGHWAY,,BAXLEY,31513,US,03/12/1980,03/20/2025,GA,Y,10/24/2016,Y,07/23/2019,,,,
    """
    __tablename__ = 'public_water_system'

    id = Column(Integer, primary_key=True)
    submission_year_quarter = Column(String)
    pwsid = Column(String)
    pws_name = Column(String)
    primacy_agency_code = Column(String)
    epa_region = Column(String)
    season_begin_date = Column(String)
    season_end_date = Column(String)
    pws_activity_code = Column(String)
    pws_deactivation_date = Column(String)
    pws_type_code = Column(String)
    dbpr_schedule_cat_code = Column(String)
    cds_id = Column(String)
    gw_sw_code = Column(String)
    lt2_schedule_cat_code = Column(String)
    owner_type_code = Column(String)
    population_served_count = Column(Integer)
    pop_cat_2_code = Column(String)
    pop_cat_3_code = Column(String)
    pop_cat_4_code = Column(String)
    pop_cat_5_code = Column(String)
    pop_cat_11_code = Column(String)
    primacy_type = Column(String)
    primary_source_code = Column(String)
    is_grant_eligible_ind = Column(String)
    is_wholesaler_ind = Column(String)
    is_school_or_daycare_ind = Column(String)
    service_connections_count = Column(Integer)
    submission_status_code = Column(String)
    org_name = Column(String)
    admin_name = Column(String)
    email_addr = Column(String)
    phone_number = Column(String)
    phone_ext_number = Column(String)
    fax_number = Column(String)
    alt_phone_number = Column(String)
    address_line1 = Column(String)
    address_line2 = Column(String)
    city_name = Column(String)
    zip_code = Column(String)
    country_code = Column(String)
    first_reported_date = Column(String)
    last_reported_date = Column(String)
    state_code = Column(String)
    source_water_protection_code = Column(String)
    source_protection_begin_date = Column(String)
    outstanding_performer = Column(String)
    outstanding_perform_begin_date = Column(String)
    reduced_rtcr_monitoring = Column(String)
    reduced_monitoring_begin_date = Column(String)
    reduced_monitoring_end_date = Column(String)
    seasonal_startup_system = Column(String)
    
    
    