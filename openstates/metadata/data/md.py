from ..models import State, Chamber, District, simple_numbered_districts

MD = State(
    name="Maryland",
    abbr="MD",
    capital="Annapolis",
    capital_tz="America/New_York",
    fips="24",
    unicameral=False,
    legislature_name="Maryland General Assembly",
    legislature_organization_id="ocd-organization/15f3b217-1d89-40dd-ab4e-d5ed2ffe5322",
    executive_name="Office of the Governor",
    executive_organization_id="ocd-organization/8af93cc2-fc5f-48b9-abc9-53b7a56b2beb",
    division_id="ocd-division/country:us/state:md",
    jurisdiction_id="ocd-jurisdiction/country:us/state:md/government",
    url="http://mgaleg.maryland.gov/",
    lower=Chamber(
        chamber_type="lower",
        name="House",
        organization_id="ocd-organization/bd8388d3-8fcd-4e28-9c1b-f23f0e376544",
        num_seats=141,
        title="Delegate",
        districts=[
            District("1A", "lower", "ocd-division/country:us/state:md/sldl:1a", 1),
            District("1B", "lower", "ocd-division/country:us/state:md/sldl:1b", 1),
            District("1C", "lower", "ocd-division/country:us/state:md/sldl:1c", 1),
            District("2A", "lower", "ocd-division/country:us/state:md/sldl:2a", 2),
            District("2B", "lower", "ocd-division/country:us/state:md/sldl:2b", 1),
            District("3A", "lower", "ocd-division/country:us/state:md/sldl:3a", 2),
            District("3B", "lower", "ocd-division/country:us/state:md/sldl:3b", 1),
            District("4", "lower", "ocd-division/country:us/state:md/sldl:4", 3),
            District("5", "lower", "ocd-division/country:us/state:md/sldl:5", 3),
            District("6", "lower", "ocd-division/country:us/state:md/sldl:6", 3),
            District("7", "lower", "ocd-division/country:us/state:md/sldl:7", 3),
            District("8", "lower", "ocd-division/country:us/state:md/sldl:8", 3),
            District("9A", "lower", "ocd-division/country:us/state:md/sldl:9a", 2),
            District("9B", "lower", "ocd-division/country:us/state:md/sldl:9b", 1),
            District("10", "lower", "ocd-division/country:us/state:md/sldl:10", 3),
            District("11", "lower", "ocd-division/country:us/state:md/sldl:11", 3),
            District("12", "lower", "ocd-division/country:us/state:md/sldl:12", 3),
            District("13", "lower", "ocd-division/country:us/state:md/sldl:13", 3),
            District("14", "lower", "ocd-division/country:us/state:md/sldl:14", 3),
            District("15", "lower", "ocd-division/country:us/state:md/sldl:15", 3),
            District("16", "lower", "ocd-division/country:us/state:md/sldl:16", 3),
            District("17", "lower", "ocd-division/country:us/state:md/sldl:17", 3),
            District("18", "lower", "ocd-division/country:us/state:md/sldl:18", 3),
            District("19", "lower", "ocd-division/country:us/state:md/sldl:19", 3),
            District("20", "lower", "ocd-division/country:us/state:md/sldl:20", 3),
            District("21", "lower", "ocd-division/country:us/state:md/sldl:21", 3),
            District("22", "lower", "ocd-division/country:us/state:md/sldl:22", 3),
            District("23A", "lower", "ocd-division/country:us/state:md/sldl:23a", 1),
            District("23B", "lower", "ocd-division/country:us/state:md/sldl:23b", 2),
            District("24", "lower", "ocd-division/country:us/state:md/sldl:24", 3),
            District("25", "lower", "ocd-division/country:us/state:md/sldl:25", 3),
            District("26", "lower", "ocd-division/country:us/state:md/sldl:26", 3),
            District("27A", "lower", "ocd-division/country:us/state:md/sldl:27a", 1),
            District("27B", "lower", "ocd-division/country:us/state:md/sldl:27b", 1),
            District("27C", "lower", "ocd-division/country:us/state:md/sldl:27c", 1),
            District("28", "lower", "ocd-division/country:us/state:md/sldl:28", 3),
            District("29A", "lower", "ocd-division/country:us/state:md/sldl:29a", 1),
            District("29B", "lower", "ocd-division/country:us/state:md/sldl:29b", 1),
            District("29C", "lower", "ocd-division/country:us/state:md/sldl:29c", 1),
            District("30A", "lower", "ocd-division/country:us/state:md/sldl:30a", 2),
            District("30B", "lower", "ocd-division/country:us/state:md/sldl:30b", 1),
            District("31A", "lower", "ocd-division/country:us/state:md/sldl:31a", 1),
            District("31B", "lower", "ocd-division/country:us/state:md/sldl:31b", 2),
            District("32", "lower", "ocd-division/country:us/state:md/sldl:32", 3),
            District("33", "lower", "ocd-division/country:us/state:md/sldl:33", 3),
            District("34A", "lower", "ocd-division/country:us/state:md/sldl:34a", 2),
            District("34B", "lower", "ocd-division/country:us/state:md/sldl:34b", 1),
            District("35A", "lower", "ocd-division/country:us/state:md/sldl:35a", 1),
            District("35B", "lower", "ocd-division/country:us/state:md/sldl:35b", 2),
            District("36", "lower", "ocd-division/country:us/state:md/sldl:36", 3),
            District("37A", "lower", "ocd-division/country:us/state:md/sldl:37a", 1),
            District("37B", "lower", "ocd-division/country:us/state:md/sldl:37b", 2),
            District("38A", "lower", "ocd-division/country:us/state:md/sldl:38a", 1),
            District("38B", "lower", "ocd-division/country:us/state:md/sldl:38b", 1),
            District("38C", "lower", "ocd-division/country:us/state:md/sldl:38c", 1),
            District("39", "lower", "ocd-division/country:us/state:md/sldl:39", 3),
            District("40", "lower", "ocd-division/country:us/state:md/sldl:40", 3),
            District("41", "lower", "ocd-division/country:us/state:md/sldl:41", 3),
            District("42A", "lower", "ocd-division/country:us/state:md/sldl:42a", 1),
            District("42B", "lower", "ocd-division/country:us/state:md/sldl:42b", 2),
            District("43", "lower", "ocd-division/country:us/state:md/sldl:43", 3),
            District("44A", "lower", "ocd-division/country:us/state:md/sldl:44a", 1),
            District("44B", "lower", "ocd-division/country:us/state:md/sldl:44b", 2),
            District("45", "lower", "ocd-division/country:us/state:md/sldl:45", 3),
            District("46", "lower", "ocd-division/country:us/state:md/sldl:46", 3),
            District("47A", "lower", "ocd-division/country:us/state:md/sldl:47a", 2),
            District("47B", "lower", "ocd-division/country:us/state:md/sldl:47b", 1),
        ],
    ),
    upper=Chamber(
        chamber_type="upper",
        name="Senate",
        organization_id="ocd-organization/6328292e-c35e-4187-903c-75829a17d5d8",
        num_seats=47,
        title="Senator",
        districts=simple_numbered_districts(
            "ocd-division/country:us/state:md", "upper", 47
        ),
    ),
)