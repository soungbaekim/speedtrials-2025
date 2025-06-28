"""
Query:
```
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
  AND table_schema NOT IN ('pg_catalog', 'information_schema')
ORDER BY table_schema, table_name;
```
Response:
```
public	facilities
public	geographic_areas
public	lcr_samples
public	milestones
public	pn_violation_assoc
public	public_water_systems
public	ref_code_values
public	service_areas
public	site_visits
public	violations_enforcement
```



Query:
```
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'milestones'
  AND table_schema = 'public';
```
Response:
```
SUBMISSIONYEARQUARTER	text	YES	
PWSID	text	YES	
EVENT_SCHEDULE_ID	text	YES	
EVENT_END_DATE	text	YES	
EVENT_ACTUAL_DATE	text	YES	
EVENT_COMMENTS_TEXT	text	YES	
EVENT_MILESTONE_CODE	text	YES	
EVENT_REASON_CODE	text	YES	
FIRST_REPORTED_DATE	text	YES	
LAST_REPORTED_DATE	text	YES	
```
"""