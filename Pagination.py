import requests

# ============================================================
# ORACLE LEADS API
# ============================================================

BASE_URL = "https://dabiqy.ds-fa.oraclepdemos.com/crmRestApi/resources/11.13.18.05/leads"

# Your API parameters
params = {
    "fields": "Name,LeadNumber,StatusCode,LeadId,PrimaryContactEmailAddress,Rank,ProductGroupName",
    "onlyData": "true",
    "limit": 25,
    "offset": 0
}

# ============================================================
# AUTHENTICATION
# ============================================================
# Replace these with your Oracle credentials

USERNAME = "natalie.salesrep"
PASSWORD = "L7WG#7?m"

# ============================================================
# PAGINATION
# ============================================================

all_leads = []

while True:

    print(f"\nCalling API with offset = {params['offset']}")

    response = requests.get(
        BASE_URL,
        params=params,
        auth=(USERNAME, PASSWORD),
        headers={
            "Accept": "application/json"
        },
        timeout=60
    )

    # Stop if API returns an error
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    # Get leads from current page
    items = data.get("items", [])

    # Add current page to overall list
    all_leads.extend(items)

    # Read pagination information
    has_more = data.get("hasMore", False)

    print(f"Records received : {len(items)}")
    print(f"Total collected  : {len(all_leads)}")
    print(f"hasMore          : {has_more}")

    # ========================================================
    # STOP WHEN THERE ARE NO MORE RECORDS
    # ========================================================

    if not has_more:
        break

    # ========================================================
    # MOVE TO NEXT PAGE
    # ========================================================

    params["offset"] += params["limit"]


# ============================================================
# FINAL RESULT
# ============================================================

print("\n===================================")
print("PAGINATION COMPLETED")
print("===================================")

print(f"Total leads retrieved: {len(all_leads)}")

# Print all leads
for lead in all_leads:

    print(
        f"LeadNumber: {lead.get('LeadNumber')} | "
        f"Name: {lead.get('Name')} | "
        f"Status: {lead.get('StatusCode')} | "
        f"Rank: {lead.get('Rank')}"
    )