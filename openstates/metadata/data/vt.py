from ..models import State, Chamber, District

VT = State(
    name="Vermont",
    abbr="VT",
    capital="Montpelier",
    capital_tz="America/New_York",
    fips="50",
    unicameral=False,
    legislature_name="Vermont General Assembly",
    legislature_organization_id="ocd-organization/3f26dc84-921f-48db-a9c9-ff843594ea85",
    executive_name="Office of the Governor",
    executive_organization_id="ocd-organization/300018cf-7c78-415b-8a3c-b00f1a0eb2fa",
    division_id="ocd-division/country:us/state:vt",
    jurisdiction_id="ocd-jurisdiction/country:us/state:vt/government",
    url="http://legislature.vermont.gov/",
    lower=Chamber(
        chamber_type="lower",
        name="House",
        organization_id="ocd-organization/1bba67ba-1a0c-4edc-a9de-32c2e5c13c6e",
        num_seats=150,
        title="Representative",
        districts=[
            District(
                "Addison-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:addison-1",
                2,
            ),
            District(
                "Addison-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:addison-2",
                1,
            ),
            District(
                "Addison-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:addison-3",
                2,
            ),
            District(
                "Addison-4",
                "lower",
                "ocd-division/country:us/state:vt/sldl:addison-4",
                2,
            ),
            District(
                "Addison-5",
                "lower",
                "ocd-division/country:us/state:vt/sldl:addison-5",
                1,
            ),
            District(
                "Addison-Rutland",
                "lower",
                "ocd-division/country:us/state:vt/sldl:addison-rutland",
                1,
            ),
            District(
                "Bennington-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:bennington-1",
                1,
            ),
            District(
                "Bennington-2-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:bennington-2-1",
                2,
            ),
            District(
                "Bennington-2-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:bennington-2-2",
                2,
            ),
            District(
                "Bennington-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:bennington-3",
                1,
            ),
            District(
                "Bennington-4",
                "lower",
                "ocd-division/country:us/state:vt/sldl:bennington-4",
                2,
            ),
            District(
                "Bennington-Rutland",
                "lower",
                "ocd-division/country:us/state:vt/sldl:bennington-rutland",
                1,
            ),
            District(
                "Caledonia-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:caledonia-1",
                1,
            ),
            District(
                "Caledonia-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:caledonia-2",
                1,
            ),
            District(
                "Caledonia-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:caledonia-3",
                2,
            ),
            District(
                "Caledonia-4",
                "lower",
                "ocd-division/country:us/state:vt/sldl:caledonia-4",
                2,
            ),
            District(
                "Caledonia-Washington",
                "lower",
                "ocd-division/country:us/state:vt/sldl:caledonia-washington",
                1,
            ),
            District(
                "Chittenden-10",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-10",
                2,
            ),
            District(
                "Chittenden-20",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-20",
                2,
            ),
            District(
                "Chittenden-25",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-25",
                1,
            ),
            District(
                "Chittenden-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-1",
                1,
            ),
            District(
                "Chittenden-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-2",
                2,
            ),
            District(
                "Chittenden-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-3",
                2,
            ),
            District(
                "Chittenden-4-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-4-1",
                1,
            ),
            District(
                "Chittenden-4-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-4-2",
                1,
            ),
            District(
                "Chittenden-5-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-5-1",
                1,
            ),
            District(
                "Chittenden-5-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-5-2",
                1,
            ),
            District(
                "Chittenden-6-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-6-1",
                2,
            ),
            District(
                "Chittenden-6-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-6-2",
                1,
            ),
            District(
                "Chittenden-6-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-6-3",
                2,
            ),
            District(
                "Chittenden-6-4",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-6-4",
                2,
            ),
            District(
                "Chittenden-6-5",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-6-5",
                2,
            ),
            District(
                "Chittenden-6-6",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-6-6",
                1,
            ),
            District(
                "Chittenden-6-7",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-6-7",
                2,
            ),
            District(
                "Chittenden-7-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-7-1",
                1,
            ),
            District(
                "Chittenden-7-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-7-2",
                1,
            ),
            District(
                "Chittenden-7-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-7-3",
                1,
            ),
            District(
                "Chittenden-7-4",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-7-4",
                1,
            ),
            District(
                "Chittenden-8-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-8-1",
                2,
            ),
            District(
                "Chittenden-8-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-8-2",
                2,
            ),
            District(
                "Chittenden-8-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-8-3",
                1,
            ),
            District(
                "Chittenden-9-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-9-1",
                2,
            ),
            District(
                "Chittenden-9-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:chittenden-9-2",
                2,
            ),
            District(
                "Essex-Caledonia",
                "lower",
                "ocd-division/country:us/state:vt/sldl:essex-caledonia",
                1,
            ),
            District(
                "Essex-Caledonia-Orleans",
                "lower",
                "ocd-division/country:us/state:vt/sldl:essex-caledonia-orleans",
                1,
            ),
            District(
                "Essex-Orleans",
                "lower",
                "ocd-division/country:us/state:vt/sldl:essex-orleans",
                1,
            ),
            District(
                "Franklin-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:franklin-1",
                1,
            ),
            District(
                "Franklin-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:franklin-2",
                1,
            ),
            District(
                "Franklin-3-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:franklin-3-1",
                2,
            ),
            District(
                "Franklin-3-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:franklin-3-2",
                1,
            ),
            District(
                "Franklin-4",
                "lower",
                "ocd-division/country:us/state:vt/sldl:franklin-4",
                2,
            ),
            District(
                "Franklin-5",
                "lower",
                "ocd-division/country:us/state:vt/sldl:franklin-5",
                2,
            ),
            District(
                "Franklin-6",
                "lower",
                "ocd-division/country:us/state:vt/sldl:franklin-6",
                1,
            ),
            District(
                "Franklin-7",
                "lower",
                "ocd-division/country:us/state:vt/sldl:franklin-7",
                1,
            ),
            District(
                "Grand Isle-Chittenden",
                "lower",
                "ocd-division/country:us/state:vt/sldl:grand_isle-chittenden",
                2,
            ),
            District(
                "Lamoille-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:lamoille-1",
                1,
            ),
            District(
                "Lamoille-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:lamoille-2",
                2,
            ),
            District(
                "Lamoille-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:lamoille-3",
                1,
            ),
            District(
                "Lamoille-Washington",
                "lower",
                "ocd-division/country:us/state:vt/sldl:lamoille-washington",
                2,
            ),
            District(
                "Orange-1", "lower", "ocd-division/country:us/state:vt/sldl:orange-1", 2
            ),
            District(
                "Orange-2", "lower", "ocd-division/country:us/state:vt/sldl:orange-2", 1
            ),
            District(
                "Orange-Caledonia",
                "lower",
                "ocd-division/country:us/state:vt/sldl:orange-caledonia",
                1,
            ),
            District(
                "Orange-Washington-Addison",
                "lower",
                "ocd-division/country:us/state:vt/sldl:orange-washington-addison",
                2,
            ),
            District(
                "Orleans-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:orleans-1",
                2,
            ),
            District(
                "Orleans-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:orleans-2",
                2,
            ),
            District(
                "Orleans-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:orleans-3",
                1,
            ),
            District(
                "Orleans-4",
                "lower",
                "ocd-division/country:us/state:vt/sldl:orleans-4",
                1,
            ),
            District(
                "Orleans-Caledonia",
                "lower",
                "ocd-division/country:us/state:vt/sldl:orleans-caledonia",
                2,
            ),
            District(
                "Orleans-Lamoille",
                "lower",
                "ocd-division/country:us/state:vt/sldl:orleans-lamoille",
                1,
            ),
            District(
                "Rutland-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:rutland-1",
                1,
            ),
            District(
                "Rutland-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:rutland-2",
                2,
            ),
            District(
                "Rutland-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:rutland-3",
                2,
            ),
            District(
                "Rutland-4",
                "lower",
                "ocd-division/country:us/state:vt/sldl:rutland-4",
                1,
            ),
            District(
                "Rutland-5-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:rutland-5-1",
                1,
            ),
            District(
                "Rutland-5-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:rutland-5-2",
                1,
            ),
            District(
                "Rutland-5-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:rutland-5-3",
                1,
            ),
            District(
                "Rutland-5-4",
                "lower",
                "ocd-division/country:us/state:vt/sldl:rutland-5-4",
                1,
            ),
            District(
                "Rutland-6",
                "lower",
                "ocd-division/country:us/state:vt/sldl:rutland-6",
                2,
            ),
            District(
                "Rutland-Bennington",
                "lower",
                "ocd-division/country:us/state:vt/sldl:rutland-bennington",
                1,
            ),
            District(
                "Rutland-Windsor-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:rutland-windsor-1",
                1,
            ),
            District(
                "Rutland-Windsor-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:rutland-windsor-2",
                1,
            ),
            District(
                "Washington-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:washington-1",
                2,
            ),
            District(
                "Washington-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:washington-2",
                2,
            ),
            District(
                "Washington-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:washington-3",
                2,
            ),
            District(
                "Washington-4",
                "lower",
                "ocd-division/country:us/state:vt/sldl:washington-4",
                2,
            ),
            District(
                "Washington-5",
                "lower",
                "ocd-division/country:us/state:vt/sldl:washington-5",
                1,
            ),
            District(
                "Washington-6",
                "lower",
                "ocd-division/country:us/state:vt/sldl:washington-6",
                1,
            ),
            District(
                "Washington-7",
                "lower",
                "ocd-division/country:us/state:vt/sldl:washington-7",
                2,
            ),
            District(
                "Washington-Chittenden",
                "lower",
                "ocd-division/country:us/state:vt/sldl:washington-chittenden",
                2,
            ),
            District(
                "Windham-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windham-1",
                1,
            ),
            District(
                "Windham-2-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windham-2-1",
                1,
            ),
            District(
                "Windham-2-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windham-2-2",
                1,
            ),
            District(
                "Windham-2-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windham-2-3",
                1,
            ),
            District(
                "Windham-3",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windham-3",
                2,
            ),
            District(
                "Windham-4",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windham-4",
                2,
            ),
            District(
                "Windham-5",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windham-5",
                1,
            ),
            District(
                "Windham-6",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windham-6",
                1,
            ),
            District(
                "Windham-Bennington",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windham-bennington",
                1,
            ),
            District(
                "Windham-Bennington-Windsor",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windham-bennington-windsor",
                1,
            ),
            District(
                "Windsor-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windsor-1",
                2,
            ),
            District(
                "Windsor-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windsor-2",
                1,
            ),
            District(
                "Windsor-3-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windsor-3-1",
                1,
            ),
            District(
                "Windsor-3-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windsor-3-2",
                2,
            ),
            District(
                "Windsor-4-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windsor-4-1",
                1,
            ),
            District(
                "Windsor-4-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windsor-4-2",
                2,
            ),
            District(
                "Windsor-5",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windsor-5",
                1,
            ),
            District(
                "Windsor-Orange-1",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windsor-orange-1",
                1,
            ),
            District(
                "Windsor-Orange-2",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windsor-orange-2",
                2,
            ),
            District(
                "Windsor-Rutland",
                "lower",
                "ocd-division/country:us/state:vt/sldl:windsor-rutland",
                1,
            ),
        ],
    ),
    upper=Chamber(
        chamber_type="upper",
        name="Senate",
        organization_id="ocd-organization/21504998-e5c7-44b4-8ebe-99fe57ef520c",
        num_seats=30,
        title="Senator",
        districts=[
            District(
                "Addison", "upper", "ocd-division/country:us/state:vt/sldu:addison", 2
            ),
            District(
                "Bennington",
                "upper",
                "ocd-division/country:us/state:vt/sldu:bennington",
                2,
            ),
            District(
                "Caledonia",
                "upper",
                "ocd-division/country:us/state:vt/sldu:caledonia",
                2,
            ),
            District(
                "Chittenden",
                "upper",
                "ocd-division/country:us/state:vt/sldu:chittenden",
                6,
            ),
            District(
                "Essex-Orleans",
                "upper",
                "ocd-division/country:us/state:vt/sldu:essex-orleans",
                2,
            ),
            District(
                "Franklin", "upper", "ocd-division/country:us/state:vt/sldu:franklin", 2
            ),
            District(
                "Grand Isle",
                "upper",
                "ocd-division/country:us/state:vt/sldu:grand_isle",
                1,
            ),
            District(
                "Lamoille", "upper", "ocd-division/country:us/state:vt/sldu:lamoille", 1
            ),
            District(
                "Orange", "upper", "ocd-division/country:us/state:vt/sldu:orange", 1
            ),
            District(
                "Rutland", "upper", "ocd-division/country:us/state:vt/sldu:rutland", 3
            ),
            District(
                "Washington",
                "upper",
                "ocd-division/country:us/state:vt/sldu:washington",
                3,
            ),
            District(
                "Windham", "upper", "ocd-division/country:us/state:vt/sldu:windham", 2
            ),
            District(
                "Windsor", "upper", "ocd-division/country:us/state:vt/sldu:windsor", 3
            ),
        ],
    ),
)
