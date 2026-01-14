# Alternative APIs for College Basketball Data

## Current Issue with SportsDataIO
The SportsDataIO free trial version provides **scrambled/synthetic data** which explains why:
- Spreads and totals are unrealistic (e.g., 237.4 total instead of 142.5)
- The data doesn't match real betting lines
- Free trial only has access to future seasons (2026+)

## Recommended Alternative APIs

### 1. **The Odds API** (RECOMMENDED)
- **Website**: https://the-odds-api.com/
- **Free Tier**: 500 requests/month
- **Data Available**:
  - Live betting odds (spreads, totals, moneylines)
  - Multiple sportsbooks
  - Pre-game and live odds
  - College basketball (NCAAB) coverage
- **Pricing**: Free tier adequate for development, $10-50/month for production
- **Pros**: 
  - Real betting lines from actual sportsbooks
  - Well-documented API
  - Good free tier for testing
- **Cons**: Request limits on free tier

**Example Usage**:
```python
import requests

API_KEY = 'your_api_key'
SPORT = 'basketball_ncaab'
REGIONS = 'us'
MARKETS = 'spreads,totals'

url = f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds'
params = {
    'apiKey': API_KEY,
    'regions': REGIONS,
    'markets': MARKETS,
    'oddsFormat': 'american'
}

response = requests.get(url, params=params)
odds_data = response.json()
```

### 2. **ESPN Hidden API** (FREE)
- **Website**: No official documentation (reverse-engineered)
- **Free Tier**: Unlimited (rate-limited)
- **Data Available**:
  - Scores
  - Schedules
  - Team stats
  - Some betting lines
- **Pros**: 
  - Completely free
  - Comprehensive game data
  - Reliable
- **Cons**: 
  - No official documentation
  - API structure can change without notice
  - May not have all betting lines

**Example Usage**:
```python
import requests

# Get scoreboard for a specific date
date = '20260115'  # YYYYMMDD format
url = f'https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard?dates={date}'

response = requests.get(url)
games = response.json()
```

### 3. **RapidAPI - Sports Data**
- **Website**: https://rapidapi.com/
- **Free Tier**: Varies by provider (usually 100-1000 requests/month)
- **Data Available**:
  - Multiple providers aggregate on RapidAPI
  - Look for "college basketball", "NCAAB", or "NCAA" APIs
  - Betting odds, scores, stats
- **Pricing**: $0-50/month depending on provider
- **Pros**: 
  - Many options to choose from
  - Single API key for multiple services
  - Good documentation
- **Cons**: 
  - Need to evaluate each provider individually
  - Quality varies

### 4. **CollegeBasketballAPI** (if available)
- Some community-maintained APIs exist
- Check GitHub for open-source college basketball data APIs
- May have limited betting line data

### 5. **Odds Jam / Odds Shark** (Web Scraping)
- **Not recommended for production** but possible for personal projects
- Would require web scraping (use BeautifulSoup/Selenium)
- Legal gray area - check terms of service

## Recommendation for Your Project

**For Development & Testing:**
1. Start with **ESPN API** for scores and game data (free)
2. Add **The Odds API** free tier for real betting lines (500 requests/month)
3. This combination gives you real data without cost

**For Production:**
1. **The Odds API** paid tier ($25-50/month) - reliable betting lines
2. **ESPN API** for supplemental game data (free)
3. Consider caching strategies to minimize API calls

## Implementation Strategy

```python
# config.py additions
ODDS_API_KEY = os.getenv("ODDS_API_KEY")
ESPN_API_ENABLED = True
USE_ODDS_API = True  # Toggle between APIs

# data_collector.py additions
class BettingLinesCollector:
    def __init__(self):
        self.odds_api_key = config.ODDS_API_KEY
        self.base_url = "https://api.the-odds-api.com/v4"
    
    def get_ncaab_odds(self, date=None):
        """Fetch current NCAAB betting lines."""
        url = f"{self.base_url}/sports/basketball_ncaab/odds"
        params = {
            'apiKey': self.odds_api_key,
            'regions': 'us',
            'markets': 'spreads,totals',
            'oddsFormat': 'american'
        }
        response = requests.get(url, params=params)
        return response.json()
```

## Cost Comparison

| API | Free Tier | Paid Tier | Real Betting Lines | Game Stats |
|-----|-----------|-----------|-------------------|------------|
| SportsDataIO | Scrambled data | $19-199/mo | ✓ (paid only) | ✓ |
| The Odds API | 500 req/mo | $25-100/mo | ✓ | ✗ |
| ESPN | Unlimited* | N/A | Limited | ✓ |
| RapidAPI | Varies | Varies | Depends on provider | Depends |

*Rate-limited but generous

## Next Steps

1. Sign up for The Odds API free tier: https://the-odds-api.com/
2. Test with ESPN API for game data
3. Implement dual-API strategy (ESPN + The Odds API)
4. Add caching to minimize API calls
5. Monitor usage and upgrade if needed

