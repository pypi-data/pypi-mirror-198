## Calculations

Several endpoints, including ratios and multiples, include values derived from figures reported in the financial statements. To calculate these values, we use the following formulas.

## Getting Started

To use the API, you'll need an API key. You can get one by emailing [founders@try-feather.com](mailto:founders@try-feather.com)

If you're using the Python client, you can set your API key as an environment variable `FEATHER_API_KEY`, or pass in the api key as a parameter to the client, as follows:

```
from featherapi import DataClient

API_KEY = 'xxyourfeatherapikeyherexx'

client = DataClient(api_key=API_KEY)
```

If calling the HTTP endpoints yourself, you need to include your api key as an `x-api-key` header. See the HTTP API documentation for more details.

## Financials

To get all available facts for an equity:

```
client.get_equity_facts('AAPL')
```

Additionally, equity facts can be fetched by range for available reporting periods:
    
```
# get the available reporting periods for AAPL
available = client.get_available('AAPL')

# get the latest 5 years of facts
end = available[-1]
start = available[-5]

results = client.get_equity_facts('AAPL', start=start, end=end)
```

To get the institutional ownership for an equity:

```
holders = client.get_institutional_holders('AAPL')
```
 