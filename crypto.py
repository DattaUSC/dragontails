from coinmarketcap import Market

coinmarketcap = Market()
coinmarketcap.listings()
{
    "cached": false,
    "data": [
        {
            "symbol": "BTC",
            "website_slug": "bitcoin",
            "id": 1,
            "name": "Bitcoin"
        },
        {
            "symbol": "LTC",
            "website_slug": "litecoin",
            "id": 2,
            "name": "Litecoin"
        },
        {
            "symbol": "NMC",
            "website_slug": "namecoin",
            "id": 3,
            "name": "Namecoin"
        },
        ...
    ],
    "metadata": {
        "timestamp": 1525776852,
        "num_cryptocurrencies": 1597,
        "error": null
    }
}