# InformerBot

#### Архитектура проекта

    bot/
    │
    ├── main.py                
    ├── config.py              
    │
    ├── handlers/
    │   ├── start.py
    │   ├── menu.py
    │   ├── weather.py
    │   ├── currency.py
    │   └── stats.py
    │
    ├── services/
    │   ├── weather_service.py
    │   ├── currency_service.py
    │
    ├── utils/
    │   ├── logger.py
    │   ├── keyboards.py
    │   └── analytics.py
    │
    ├── data/
    │   └── weather_logs.csv
    │
    └── requirements.txt