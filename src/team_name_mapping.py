"""
Team name mapping between SportsDataIO abbreviations/names and The Odds API full names.

This mapping is used to match games between the two APIs since they use different naming conventions.
"""

# Mapping from SportsDataIO abbreviation to The Odds API full team name
# Format: 'ABBREVIATION': 'Full Team Name from The Odds API'

SPORTSDATA_TO_ODDS_API = {
    # A
    'ALAAM': 'Alabama A&M Bulldogs',
    'ALAST': 'Alabama State Hornets',
    'ALCST': 'Alcorn St Braves',
    'AMERCN': 'American Eagles',
    'APSU': 'Austin Peay Governors',
    'ARK': 'Arkansas Razorbacks',
    'ARPB': 'Arkansas-Pine Bluff Golden Lions',
    'AUB': 'Auburn Tigers',
    
    # B
    'BALL': 'Ball State Cardinals',
    'BAY': 'Baylor Bears',
    'BC': 'Boston College Eagles',
    'BCOOK': 'Bethune-Cookman Wildcats',
    'BGSU': 'Bowling Green Falcons',
    'BING': 'Binghamton Bearcats',
    'BRAD': 'Bradley Braves',
    'BU': 'Boston University Terriers',
    'BUT': 'Butler Bulldogs',
    
    # C
    'CAL': 'California Golden Bears',
    'CHAR': 'Charlotte 49ers',
    'CLEM': 'Clemson Tigers',
    'CLEV': 'Cleveland State Vikings',
    'COLO': 'Colorado Buffaloes',
    'CONN': 'Connecticut Huskies',
    'COP': 'Coppin St Eagles',
    'COPPST': 'Coppin St Eagles',
    'CP': 'Cal Poly Mustangs',
    'CREI': 'Creighton Bluejays',
    'CSUB': 'CSU Bakersfield Roadrunners',
    
    # D
    'DART': 'Dartmouth Big Green',
    'DAY': 'Dayton Flyers',
    'DEL': 'Delaware Fightin Blue Hens',
    'DELST': 'Delaware St Hornets',
    'DEN': 'Denver Pioneers',
    'DEP': 'DePaul Blue Demons',
    'DET': 'Detroit Mercy Titans',
    'DREX': 'Drexel Dragons',
    'DUKE': 'Duke Blue Devils',
    'DUQ': 'Duquesne Dukes',
    
    # E
    'ECU': 'East Carolina Pirates',
    'EIU': 'Eastern Illinois Panthers',
    'EKY': 'Eastern Kentucky Colonels',
    'ELON': 'Elon Phoenix',
    'EMU': 'Eastern Michigan Eagles',
    'EWU': 'Eastern Washington Eagles',
    
    # F
    'FAIR': 'Fairfield Stags',
    'FAMU': 'Florida A&M Rattlers',
    'FLAM': 'Florida A&M Rattlers',
    'FDU': 'Fairleigh Dickinson Knights',
    'FGC': 'Florida Gulf Coast Eagles',
    'FIU': 'Florida International Panthers',
    'FLA': 'Florida Gators',
    'FOR': 'Fordham Rams',
    'FRES': 'Fresno State Bulldogs',
    'FSU': 'Florida State Seminoles',
    'FUR': 'Furman Paladins',
    
    # G
    'GASO': 'Georgia Southern Eagles',
    'GAST': 'Georgia State Panthers',
    'GRMBST': 'Grambling St Tigers',
    'GB': 'Green Bay Phoenix',
    'GC': 'Georgia College',  # May need verification
    'GONZ': 'Gonzaga Bulldogs',
    'GTOWN': 'Georgetown Hoyas',
    'GVSU': 'Grand Valley State',
    
    # H
    'HALL': 'Seton Hall Pirates',
    'HAMP': 'Hampton Pirates',
    'HARV': 'Harvard Crimson',
    'HAW': 'Hawaii Rainbow Warriors',
    'HBU': 'Houston Christian Huskies',
    'HOUBAP': 'Houston Christian Huskies',
    'HOWRD': 'Howard Bison',
    'HC': 'Holy Cross Crusaders',
    'HOF': 'Hofstra Pride',
    'HOU': 'Houston Cougars',
    'HOW': 'Howard Bison',
    'HP': 'High Point Panthers',
    
    # I
    'IDHO': 'Idaho Vandals',
    'INCAR': 'Incarnate Word Cardinals',
    'IDST': 'Idaho State Bengals',
    'ILL': 'Illinois Fighting Illini',
    'ILST': 'Illinois State Redbirds',
    'IND': 'Indiana Hoosiers',
    'INST': 'Indiana State Sycamores',
    'IONA': 'Iona Gaels',
    'IOWA': 'Iowa Hawkeyes',
    'IOST': 'Iowa State Cyclones',
    'IUPUI': 'IUPUI Jaguars',
    
    # J
    'JAC': 'Jacksonville Dolphins',
    'JACKST': 'Jackson St Tigers',
    'JVST': 'Jacksonville State Gamecocks',
    
    # K
    'KANS': 'Kansas Jayhawks',
    'KENT': 'Kent State Golden Flashes',
    'KSU': 'Kansas State Wildcats',
    'KY': 'Kentucky Wildcats',
    
    # L
    'LAF': 'Lafayette Leopards',
    'LAM': 'Lamar Cardinals',
    'LAMAR': 'Lamar Cardinals',
    'LAS': 'La Salle Explorers',
    'LB': 'Long Beach State Beach',
    'LEH': 'Lehigh Mountain Hawks',
    'LIB': 'Liberty Flames',
    'LIP': 'Lipscomb Bisons',
    'LIU': 'LIU Sharks',
    'LOU': 'Louisville Cardinals',
    'LSU': 'LSU Tigers',
    'LT': 'Louisiana Tech Bulldogs',
    'LUC': 'Loyola Chicago Ramblers',
    'LUM': 'Loyola Marymount Lions',
    
    # M
    'MAINE': 'Maine Black Bears',
    'MAN': 'Manhattan Jaspers',
    'MARQ': 'Marquette Golden Eagles',
    'MARY': 'Maryland Terrapins',
    'MASS': 'Massachusetts Minutemen',
    'MCNS': 'McNeese Cowboys',
    'MCNST': 'McNeese Cowboys',
    'MDES': 'Maryland-Eastern Shore Hawks',
    'MEM': 'Memphis Tigers',
    'MER': 'Mercer Bears',
    'MIA': 'Miami Hurricanes',
    'MIAOH': 'Miami (OH) RedHawks',
    'MICH': 'Michigan Wolverines',
    'MILW': 'Milwaukee Panthers',
    'MINN': 'Minnesota Golden Gophers',
    'MISS': 'Ole Miss Rebels',
    'MIZZ': 'Missouri Tigers',
    'MONM': 'Monmouth Hawks',
    'MONT': 'Montana Grizzlies',
    'MORG': 'Morgan State Bears',
    'MORGST': 'Morgan State Bears',
    'MOST': 'Missouri State Bears',
    'MRSH': 'Marshall Thundering Herd',
    'MSST': 'Mississippi State Bulldogs',
    'MSU': 'Michigan State Spartans',
    'MTN': 'Montana State Bobcats',
    'MTST': 'Middle Tennessee Blue Raiders',
    'MUR': 'Murray State Racers',
    'MSVLST': 'Miss Valley St Delta Devils',
    'MVSU': 'Mississippi Valley State Delta Devils',
    
    # N
    'NAU': 'Northern Arizona Lumberjacks',
    'NICHLS': 'Nicholls St Colonels',
    'NO': 'New Orleans Privateers',
    'NAVY': 'Navy Midshipmen',
    'NCAT': 'North Carolina A&T Aggies',
    'NCC': 'North Carolina Central Eagles',
    'NCCU': 'North Carolina Central Eagles',
    'NCST': 'NC State Wolfpack',
    'ND': 'Notre Dame Fighting Irish',
    'NDSU': 'North Dakota State Bison',
    'NEB': 'Nebraska Cornhuskers',
    'NEV': 'Nevada Wolf Pack',
    'NIAG': 'Niagara Purple Eagles',
    'NIU': 'Northern Illinois Huskies',
    'NJIT': 'NJIT Highlanders',
    'NKU': 'Northern Kentucky Norse',
    'NMSU': 'New Mexico State Aggies',
    'NORF': 'Norfolk St Spartans',
    'NORFST': 'Norfolk St Spartans',
    'NORST': 'Norfolk St Spartans',
    'NW': 'Northwestern Wildcats',
    'NWST': 'Northwestern State Demons',
    
    # O
    'ODU': 'Old Dominion Monarchs',
    'OHIO': 'Ohio Bobcats',
    'OKLA': 'Oklahoma Sooners',
    'OKST': 'Oklahoma State Cowboys',
    'ORE': 'Oregon Ducks',
    'ORST': 'Oregon State Beavers',
    
    # P
    'PENN': 'Pennsylvania Quakers',
    'PEPP': 'Pepperdine Waves',
    'PITT': 'Pittsburgh Panthers',
    'PORT': 'Portland Pilots',
    'PRES': 'Presbyterian Blue Hose',
    'PRIN': 'Princeton Tigers',
    'PROV': 'Providence Friars',
    'PURD': 'Purdue Boilermakers',
    'PV': 'Prairie View Panthers',
    'PVAM': 'Prairie View Panthers',
    
    # Q
    'QUIN': 'Quinnipiac Bobcats',
    
    # R
    'RAD': 'Radford Highlanders',
    'RICE': 'Rice Owls',
    'RICH': 'Richmond Spiders',
    'RID': 'Rider Broncs',
    'RMU': 'Robert Morris Colonials',
    'RUTG': 'Rutgers Scarlet Knights',
    
    # S
    'SAC': 'Sacramento State Hornets',
    'SAM': 'Samford Bulldogs',
    'SCARST': 'South Carolina St Bulldogs',
    'SCST': 'South Carolina St Bulldogs',
    'SELOU': 'SE Louisiana Lions',
    'SCUP': 'South Carolina Upstate Spartans',
    'SDAK': 'South Dakota Coyotes',
    'SDST': 'San Diego State Aztecs',
    'SDSU': 'South Dakota State Jackrabbits',
    'SEAT': 'Seattle Redhawks',
    'SELA': 'SE Louisiana Lions',
    'SEMO': 'Southeast Missouri State Redhawks',
    'SF': 'San Francisco Dons',
    'SFA': 'Stephen F. Austin Lumberjacks',
    'SFAUS': 'Stephen F. Austin Lumberjacks',
    'SFNY': 'St. Francis (NY) Terriers',
    'SHU': 'Sacred Heart Pioneers',
    'SIE': 'Siena Saints',
    'SIU': 'Southern Illinois Salukis',
    'SIUE': 'SIU Edwardsville Cougars',
    'SJU': 'St. John\'s Red Storm',
    'SMC': 'Saint Mary\'s Gaels',
    'SMU': 'SMU Mustangs',
    'SOU': 'South Carolina Gamecocks',
    'SOUTH': 'Southern Jaguars',
    'SPC': 'St. Peter\'s Peacocks',
    'STAN': 'Stanford Cardinal',
    'STON': 'Stony Brook Seawolves',
    'SUU': 'Southern Utah Thunderbirds',
    'SYR': 'Syracuse Orange',
    
    # T
    'TAMC': 'Texas A&M-CC Islanders',
    'TXS': 'Texas Southern Tigers',
    'TXAMC': 'Texas A&M-CC Islanders',
    'TAMU': 'Texas A&M Aggies',
    'TCU': 'TCU Horned Frogs',
    'TEMP': 'Temple Owls',
    'TENN': 'Tennessee Volunteers',
    'TNST': 'Tennessee State Tigers',
    'TNTECH': 'Tennessee Tech Golden Eagles',
    'TOL': 'Toledo Rockets',
    'TOWS': 'Towson Tigers',
    'TROY': 'Troy Trojans',
    'TULN': 'Tulane Green Wave',
    'TULS': 'Tulsa Golden Hurricane',
    
    # U
    'UAB': 'UAB Blazers',
    'UAPB': 'Arkansas-Pine Bluff Golden Lions',
    'UC': 'UC Davis Aggies',
    'UCA': 'Central Arkansas Bears',
    'UCF': 'UCF Knights',
    'UCI': 'UC Irvine Anteaters',
    'UCLA': 'UCLA Bruins',
    'UCSB': 'UC Santa Barbara Gauchos',
    'UIC': 'UIC Flames',
    'ULL': 'Louisiana Ragin\' Cajuns',
    'ULM': 'Louisiana Monroe Warhawks',
    'UMASS': 'Massachusetts Minutemen',
    'UMBC': 'UMBC Retrievers',
    'UMES': 'Maryland-Eastern Shore Hawks',
    'UML': 'UMass Lowell River Hawks',
    'UNC': 'North Carolina Tar Heels',
    'UNCA': 'UNC Asheville Bulldogs',
    'UNCG': 'UNC Greensboro Spartans',
    'UNCO': 'Northern Colorado Bears',
    'UNCW': 'UNC Wilmington Seahawks',
    'UNF': 'North Florida Ospreys',
    'UNI': 'Northern Iowa Panthers',
    'UNLV': 'UNLV Rebels',
    'UNM': 'New Mexico Lobos',
    'UNO': 'New Orleans Privateers',
    'URI': 'Rhode Island Rams',
    'USA': 'South Alabama Jaguars',
    'USC': 'USC Trojans',
    'USF': 'South Florida Bulls',
    'USM': 'Southern Miss Golden Eagles',
    'USU': 'Utah State Aggies',
    'UTA': 'UT Arlington Mavericks',
    'UTAH': 'Utah Utes',
    'UTEP': 'UTEP Miners',
    'UTM': 'UT Martin Skyhawks',
    'UTRGV': 'UT Rio Grande Valley Vaqueros',
    'UTSA': 'UTSA Roadrunners',
    'UVA': 'Virginia Cavaliers',
    'UVM': 'Vermont Catamounts',
    
    # V
    'VALP': 'Valparaiso Beacons',
    'VAN': 'Vanderbilt Commodores',
    'VCU': 'VCU Rams',
    'VILL': 'Villanova Wildcats',
    'VT': 'Virginia Tech Hokies',
    
    # W
    'WAG': 'Wagner Seahawks',
    'WAKE': 'Wake Forest Demon Deacons',
    'WASH': 'Washington Huskies',
    'WEBB': 'Gardner-Webb Runnin\' Bulldogs',
    'WIC': 'Wichita State Shockers',
    'WIN': 'Winthrop Eagles',
    'WISC': 'Wisconsin Badgers',
    'WKU': 'Western Kentucky Hilltoppers',
    'WM': 'William & Mary Tribe',
    'WMU': 'Western Michigan Broncos',
    'WOF': 'Wofford Terriers',
    'WSU': 'Washington State Cougars',
    'WVU': 'West Virginia Mountaineers',
    'WYO': 'Wyoming Cowboys',
    
    # X
    'XAV': 'Xavier Musketeers',
    
    # Y
    'YALE': 'Yale Bulldogs',
    'YSU': 'Youngstown State Penguins',
}

# Reverse mapping: The Odds API name to SportsDataIO abbreviation
ODDS_API_TO_SPORTSDATA = {v: k for k, v in SPORTSDATA_TO_ODDS_API.items()}


def get_odds_api_name(sportsdata_abbr: str) -> str:
    """
    Convert a SportsDataIO team abbreviation to The Odds API full name.
    
    Args:
        sportsdata_abbr: Team abbreviation from SportsDataIO (e.g., 'DUKE')
    
    Returns:
        The Odds API full team name (e.g., 'Duke Blue Devils')
        Returns the input if no mapping found.
    """
    return SPORTSDATA_TO_ODDS_API.get(sportsdata_abbr, sportsdata_abbr)


def get_sportsdata_abbr(odds_api_name: str) -> str:
    """
    Convert a The Odds API full team name to SportsDataIO abbreviation.
    
    Args:
        odds_api_name: Full team name from The Odds API (e.g., 'Duke Blue Devils')
    
    Returns:
        SportsDataIO abbreviation (e.g., 'DUKE')
        Returns the input if no mapping found.
    """
    return ODDS_API_TO_SPORTSDATA.get(odds_api_name, odds_api_name)


def fuzzy_match_team(team_name: str, candidates: list, threshold: float = 0.6) -> str:
    """
    Find the best fuzzy match for a team name from a list of candidates.
    
    Args:
        team_name: Team name to match
        candidates: List of candidate team names
        threshold: Minimum similarity score (0-1)
    
    Returns:
        Best matching candidate or empty string if no good match
    """
    from difflib import SequenceMatcher
    
    best_match = ""
    best_score = 0.0
    
    team_lower = team_name.lower()
    
    for candidate in candidates:
        candidate_lower = candidate.lower()
        
        # Check for substring match first
        if team_lower in candidate_lower or candidate_lower in team_lower:
            score = 0.9
        else:
            # Use sequence matcher
            score = SequenceMatcher(None, team_lower, candidate_lower).ratio()
        
        if score > best_score and score >= threshold:
            best_score = score
            best_match = candidate
    
    return best_match

