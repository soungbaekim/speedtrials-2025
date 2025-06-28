from typing import Any, Tuple
from langgraph.graph.graph import CompiledGraph
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from sqlalchemy import Engine
from src.postgres.postgres import PostgresClient

PROMPT = """
You are a helpful assistant that can answer questions about the Safe Drinking Water Information System (SDWIS).

# Tables
This section contains queries that have been run on the database. You can use them as a reference for what is available in the database.

1. `milestones`
```
column_name	data_type
SUBMISSIONYEARQUARTER	text
PWSID	text
EVENT_SCHEDULE_ID	text
EVENT_END_DATE	text
EVENT_ACTUAL_DATE	text
EVENT_COMMENTS_TEXT	text
EVENT_MILESTONE_CODE	text
EVENT_REASON_CODE	text
FIRST_REPORTED_DATE	text
LAST_REPORTED_DATE	text
```
2. `facilities`
```
column_name	data_type
SUBMISSIONYEARQUARTER	text
PWSID	text
FACILITY_ID	text
FACILITY_NAME	text
STATE_FACILITY_ID	text
FACILITY_ACTIVITY_CODE	text
FACILITY_DEACTIVATION_DATE	text
FACILITY_TYPE_CODE	text
SUBMISSION_STATUS_CODE	text
IS_SOURCE_IND	text
WATER_TYPE_CODE	text
AVAILABILITY_CODE	text
SELLER_TREATMENT_CODE	text
SELLER_PWSID	text
SELLER_PWS_NAME	text
FILTRATION_STATUS_CODE	text
IS_SOURCE_TREATED_IND	text
FIRST_REPORTED_DATE	text
LAST_REPORTED_DATE	text
```
3. `geographic_areas`
```
SUBMISSIONYEARQUARTER	text
PWSID	text
GEO_ID	bigint
AREA_TYPE_CODE	text
TRIBAL_CODE	double precision
STATE_SERVED	text
ANSI_ENTITY_CODE	double precision
ZIP_CODE_SERVED	double precision
CITY_SERVED	text
COUNTY_SERVED	text
LAST_REPORTED_DATE	text
```
4. `lcr_samples`
```
SUBMISSIONYEARQUARTER	text
PWSID	text
SAMPLE_ID	text
SAMPLING_END_DATE	text
SAMPLING_START_DATE	text
RECONCILIATION_ID	text
SAMPLE_FIRST_REPORTED_DATE	text
SAMPLE_LAST_REPORTED_DATE	text
SAR_ID	bigint
CONTAMINANT_CODE	text
RESULT_SIGN_CODE	double precision
SAMPLE_MEASURE	double precision
UNIT_OF_MEASURE	text
SAR_FIRST_REPORTED_DATE	text
SAR_LAST_REPORTED_DATE	text
```
5. `pn_violation_assoc`
```
SUBMISSIONYEARQUARTER	text
PWSID	text
PN_VIOLATION_ID	bigint
RELATED_VIOLATION_ID	bigint
COMPL_PER_BEGIN_DATE	text
COMPL_PER_END_DATE	text
NON_COMPL_PER_BEGIN_DATE	text
NON_COMPL_PER_END_DATE	text
VIOLATION_CODE	text
CONTAMINANT_CODE	bigint
FIRST_REPORTED_DATE	text
LAST_REPORTED_DATE	text
```
6. `public_water_systems`
```
SUBMISSIONYEARQUARTER	text
PWSID	text
PWS_NAME	text
PRIMACY_AGENCY_CODE	text
EPA_REGION	bigint
SEASON_BEGIN_DATE	text
SEASON_END_DATE	text
PWS_ACTIVITY_CODE	text
PWS_DEACTIVATION_DATE	text
PWS_TYPE_CODE	text
DBPR_SCHEDULE_CAT_CODE	double precision
CDS_ID	double precision
GW_SW_CODE	text
LT2_SCHEDULE_CAT_CODE	double precision
OWNER_TYPE_CODE	text
POPULATION_SERVED_COUNT	bigint
POP_CAT_2_CODE	bigint
POP_CAT_3_CODE	bigint
POP_CAT_4_CODE	bigint
POP_CAT_5_CODE	bigint
POP_CAT_11_CODE	bigint
PRIMACY_TYPE	text
PRIMARY_SOURCE_CODE	text
IS_GRANT_ELIGIBLE_IND	text
IS_WHOLESALER_IND	text
IS_SCHOOL_OR_DAYCARE_IND	text
SERVICE_CONNECTIONS_COUNT	bigint
SUBMISSION_STATUS_CODE	text
ORG_NAME	text
ADMIN_NAME	text
EMAIL_ADDR	text
PHONE_NUMBER	text
PHONE_EXT_NUMBER	double precision
FAX_NUMBER	text
ALT_PHONE_NUMBER	double precision
ADDRESS_LINE1	text
ADDRESS_LINE2	text
CITY_NAME	text
ZIP_CODE	text
COUNTRY_CODE	text
FIRST_REPORTED_DATE	text
LAST_REPORTED_DATE	text
STATE_CODE	text
SOURCE_WATER_PROTECTION_CODE	text
SOURCE_PROTECTION_BEGIN_DATE	text
OUTSTANDING_PERFORMER	text
OUTSTANDING_PERFORM_BEGIN_DATE	text
REDUCED_RTCR_MONITORING	double precision
REDUCED_MONITORING_BEGIN_DATE	double precision
REDUCED_MONITORING_END_DATE	double precision
SEASONAL_STARTUP_SYSTEM	text
```
7. `ref_code_values`
```
VALUE_TYPE	text
VALUE_CODE	text
VALUE_DESCRIPTION	text
```
8. `service_areas`
```
SUBMISSIONYEARQUARTER	text
PWSID	text
SERVICE_AREA_TYPE_CODE	text
IS_PRIMARY_SERVICE_AREA_CODE	text
FIRST_REPORTED_DATE	text
LAST_REPORTED_DATE	text
```
9. `site_visits`
```
SUBMISSIONYEARQUARTER	text
PWSID	text
VISIT_ID	text
VISIT_DATE	text
AGENCY_TYPE_CODE	text
VISIT_REASON_CODE	text
MANAGEMENT_OPS_EVAL_CODE	text
SOURCE_WATER_EVAL_CODE	text
SECURITY_EVAL_CODE	text
PUMPS_EVAL_CODE	text
OTHER_EVAL_CODE	text
COMPLIANCE_EVAL_CODE	text
DATA_VERIFICATION_EVAL_CODE	text
TREATMENT_EVAL_CODE	text
FINISHED_WATER_STOR_EVAL_CODE	text
DISTRIBUTION_EVAL_CODE	text
FINANCIAL_EVAL_CODE	text
VISIT_COMMENTS	text
FIRST_REPORTED_DATE	text
LAST_REPORTED_DATE	text
```
10. `violations_enforcement`
```
SUBMISSIONYEARQUARTER	text
PWSID	text
VIOLATION_ID	text
FACILITY_ID	double precision
COMPL_PER_BEGIN_DATE	text
COMPL_PER_END_DATE	text
NON_COMPL_PER_BEGIN_DATE	text
NON_COMPL_PER_END_DATE	text
PWS_DEACTIVATION_DATE	text
VIOLATION_CODE	text
VIOLATION_CATEGORY_CODE	text
IS_HEALTH_BASED_IND	text
CONTAMINANT_CODE	double precision
VIOL_MEASURE	double precision
UNIT_OF_MEASURE	text
FEDERAL_MCL	text
STATE_MCL	double precision
IS_MAJOR_VIOL_IND	text
SEVERITY_IND_CNT	double precision
CALCULATED_RTC_DATE	text
VIOLATION_STATUS	text
PUBLIC_NOTIFICATION_TIER	double precision
CALCULATED_PUB_NOTIF_TIER	double precision
VIOL_ORIGINATOR_CODE	text
SAMPLE_RESULT_ID	text
CORRECTIVE_ACTION_ID	text
RULE_CODE	double precision
RULE_GROUP_CODE	double precision
RULE_FAMILY_CODE	double precision
VIOL_FIRST_REPORTED_DATE	text
VIOL_LAST_REPORTED_DATE	text
ENFORCEMENT_ID	text
ENFORCEMENT_DATE	text
ENFORCEMENT_ACTION_TYPE_CODE	text
ENF_ACTION_CATEGORY	text
ENF_ORIGINATOR_CODE	text
ENF_FIRST_REPORTED_DATE	text
ENF_LAST_REPORTED_DATE	text
```
"""

def create_graph(engine: Engine) -> CompiledGraph: 
    openai = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        timeout=None,
        max_retries=2,
    )

    claude = ChatAnthropic(
        model_name="claude-3-7-sonnet-latest",
        temperature=0,
        timeout=None,
        max_retries=2,
        stop=None,
    )

    async def query_postgres(query: str) -> Tuple[Any, str]:  
        """Make a call to postgres with the given query.
        
        Args:
            query (str): The query to run on postgres.
        Returns:
            (rows, error_message) -> Tuple[Any, str]

        All rows will be returned so be careful with the size of the query since that will be fed back to the model.
        """
        cur = engine.connect()
        cur.execute(query)
        rows = cur.fetchall()

        if len(rows) > 100:
            return (rows[:100], f"error:query was too large to return; only the first 100 rows are returned; full length: {len(rows)}.")

        return (rows, "")

    return create_react_agent(
        model=claude,
        tools=[query_postgres],
        prompt=PROMPT,
    )


async def main():
    graph = await create_graph(create_connection())
    # user_message = "how many male users do we have that have less than 25 likes?"
    # user_message = "what's the general trend of likes over time?"
    # user_message = "how many on hold users do we have? Can you also give a breakdown of those users? On hold users can be found in the `groups` table where they are in a certain group."
    # user_message = "how many on hold users do we have? How many of them are male/female?"
    # user_message = "give a break down of the number of users in a 50-mile radius around Los Angeles in the last week."
    user_message = "Find me a user. His first name is Isaac. He lives in California. He's in his thirties. If you can't find the exact user, return a list of close matches. Don't spot till you have something. Return the user's id some basic info."

    # Run the agent
    out = graph.invoke(
        {"messages": [{"role": "user", "content": user_message}]},
        {"recursion_limit": 100},
        debug=True,
    )

    # Assuming `out` is the output dictionary
    last_ai_message = None
    for msg in reversed(out["messages"]):
        if type(msg).__name__ == "AIMessage" or getattr(msg, "role", None) == "assistant":
            # If using dicts instead of objects, use msg.get("content")
            last_ai_message = msg.content if hasattr(msg, "content") else msg.get("content")
            break
    
    print("\nUser:\n\t")
    print(user_message)
    print("\n\nAgent:\n\t")
    print(last_ai_message)
    print("\n\n*** Full output:***\n")
    print(out.keys())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())