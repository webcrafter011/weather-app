# Weather Dashboard

A modern weather application built with Django that displays weather information and city images using OpenWeather API and Pexels API.

![Weather Dashboard Screenshot](screenshot.png)

## Features

- Real-time weather data using OpenWeather API
- City images using Pexels API
- Modern, responsive user interface
- Displays temperature, pressure, humidity, and location data
- Beautiful glass-morphism design elements

## Technologies Used

- Python 3.x
- Django
- HTML5
- CSS3
- Bootstrap 3
- OpenWeather API
- Pexels API

## Installation

1. Clone the repository
```bash
git clone git@github.com:webcrafter011/weather-app.git
cd weather-detection
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages
```bash
pip install django
pip install pexels-api
```

4. Set up environment variables
Create a `.env` file in the root directory and add your API keys:
```
OPENWEATHER_API_KEY=your_openweather_api_key
PEXELS_API_KEY=your_pexels_api_key
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000` in your browser

## API Keys

You'll need to obtain API keys from:
- [OpenWeather](https://openweathermap.org/api)
- [Pexels](https://www.pexels.com/api/)

## Usage

1. Enter a city name in the search bar
2. Click the search button or press Enter
3. View the weather information and a representative image of the city

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenWeather API for weather data
- Pexels API for city images
- Bootstrap for UI components
