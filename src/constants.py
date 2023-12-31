from gi.repository import Gio, GLib

settings = Gio.Settings.new("io.github.amit9838.weather")
API_KEY = settings.get_string("personal-api-key")
use_personal_api_key = settings.get_boolean("use-personal-api-key")

icon_loc = "/app/share/icons/hicolor/scalable/weather_icons/"

icons = {
    "0": icon_loc + "clear-day.svg",
    "1": icon_loc + "clear-day.svg",
    "2": icon_loc + "overcast-day.svg",
    "3": icon_loc + "overcast.svg",
    "51": icon_loc + "partly-cloudy-day-drizzle.svg",
    "53": icon_loc + "drizzle.svg",
    "55": icon_loc + "overcast-drizzle.svg",
    "56": icon_loc + "partly-cloudy-day-snow.svg",
    "57": icon_loc + "overcast-snow.svg",
    "61": icon_loc + "partly-cloudy-day-rain.svg",
    "63": icon_loc + "rain.svg",
    "65": icon_loc + "thunderstorms-rain.svg",
    "66": icon_loc + "overcast-snow.svg",
    "67": icon_loc + "thunderstorms-rain.svg",
    "45": icon_loc + "fog.svg",
    "48": icon_loc + "fog.svg",
    "71": icon_loc + "partly-cloudy-day-snow.svg",
    "73": icon_loc + "snow.svg",
    "75": icon_loc + "snowflake.svg",
    "77": icon_loc + "snowflake.svg",
    "80": icon_loc + "overcast-day-rain.svg",
    "81": icon_loc + "rain.svg",
    "82": icon_loc + "thunderstorms-rain.svg",
    "85": icon_loc + "snow.svg",
    "86": icon_loc + "snowflake.svg",
    "96": icon_loc + "thunderstorms-day-overcast-snow.svg",
    "99": icon_loc + "snowflake.svg",
    
     "0n": icon_loc + "clear-night.svg",
     "1n": icon_loc + "clear-night.svg",
     "2n": icon_loc + "overcast-night.svg",
     "3n": icon_loc + "overcast.svg",
    "51n": icon_loc + "partly-cloudy-night-drizzle.svg",
    "53n": icon_loc + "drizzle.svg",
    "55n": icon_loc + "overcast-drizzle.svg",
    "56n": icon_loc + "partly-cloudy-night-snow.svg",
    "57n": icon_loc + "overcast-snow.svg",
    "61n": icon_loc + "partly-cloudy-night-rain.svg",
    "63n": icon_loc + "rain.svg",
    "65n": icon_loc + "thunderstorms-rain.svg",
    "66n": icon_loc + "overcast-snow.svg",
    "67n": icon_loc + "thunderstorms-rain.svg",
    "45n": icon_loc + "fog.svg",
    "48n": icon_loc + "fog.svg",
    "71n": icon_loc + "partly-cloudy-night-snow.svg",
    "73n": icon_loc + "snow.svg",
    "75n": icon_loc + "snowflake.svg",
    "77n": icon_loc + "snowflake.svg",
    "80n": icon_loc + "overcast-night-rain.svg",
    "81n": icon_loc + "rain.svg",
    "82n": icon_loc + "thunderstorms-rain.svg",
    "85n": icon_loc + "snow.svg",
    "86n": icon_loc + "snowflake.svg",
    "96n": icon_loc + "thunderstorms-night-overcast-snow.svg",
    "99n": icon_loc + "snowflake.svg",

    "arrow" : icon_loc + "arrow.svg",
}

bg_css = {
    "01d": "clear_sky",
    "02d": "few_clouds",
    "03d": "overcast",
    "04d": "overcast",
    "09d": "showers_scattered",
    "10d": "showers_large",
    "11d": "storm",
    "13d": "snow",
    "50d": "fog",
    "01n": "clear_sky_night",
    "02n": "few_clouds_night",
    "03n": "overcast_night",
    "04n": "showers_scattered_night",
    "09n": "showers_large_night",
    "10n": "showers_large_night",
    "11n": "storm_night",
    "13n": "snow_night",
    "50n": "fog_night",
}
# 1 ->   indicates day
# 1n ->  indicates night

conditon = {
     "0": "Clear sky",
     "1": "Few Clouds",
     "2": "Partly Cloudy",
     "3": "Overcast",
    "45": "Fog",
    "48": "Rime Fog",
    "51": "Light Drizzle",
    "53": "Moderate Drizzle",
    "55": "Heavy Intensity Drizzle ",
    "56": "Light Freezing Drizzle",
    "57": "Heavy Freezing Drizzle",
    "61": "Light Rain",
    "63": "Moderate Rain",
    "65": "Heavy Rain",
    "66": "Light Freezing Rain",
    "67": "Heavy Freezing Rain",
    "71": "Light Snow Fall",
    "73": "Moderate Snow Fall",
    "75": "Heavy Snow Fall	",
    "77": "Snow grains",
    "80": "Light Rain Showers",
    "81": "Moderate Rain Showers",
    "82": "Heavy Rain Showers",
    "85": "Light Snow Showers",
    "86": "Heavy Snow Showers ",
    "95": "Thunderstorm",
    "96": "Thunderstorm with Hail",
}


COUNTRY_CODES = {
    "AD": "Andorra",
    "AE": "UAE",
    "AF": "Afghanistan",
    "AG": "Antigua & Barbuda",
    "AI": "Anguilla",
    "AL": "Albania",
    "AM": "Armenia",
    "AO": "Angola",
    "AQ": "Antarctica",
    "AR": "Argentina",
    "AS": "American Samoa",
    "AT": "Austria",
    "AU": "Australia",
    "AW": "Aruba",
    "AX": "Åland Islands",
    "AZ": "Azerbaijan",
    "BA": "Bosnia & Herzegovina",
    "BB": "Barbados",
    "BD": "Bangladesh",
    "BE": "Belgium",
    "BF": "Burkina Faso",
    "BG": "Bulgaria",
    "BH": "Bahrain",
    "BI": "Burundi",
    "BJ": "Benin",
    "BL": "Saint Barthélemy",
    "BM": "Bermuda",
    "BN": "Brunei Darussalam",
    "BO": "Bolivia",
    "BQ": "Bonaire",
    "BR": "Brazil",
    "BS": "Bahamas",
    "BT": "Bhutan",
    "BV": "Bouvet Island",
    "BW": "Botswana",
    "BY": "Belarus",
    "BZ": "Belize",
    "CA": "Canada",
    "CC": "Cocos",
    "CD": "Congo",
    "CF": "Central Africa",
    "CG": "Congo",
    "CH": "Switzerland",
    "CI": "Côte d'Ivoire",
    "CK": "Cook Islands",
    "CL": "Chile",
    "CM": "Cameroon",
    "CN": "China",
    "CO": "Colombia",
    "CR": "Costa Rica",
    "CU": "Cuba",
    "CV": "Cabo Verde",
    "CW": "Curaçao",
    "CX": "Christmas Island",
    "CY": "Cyprus",
    "CZ": "Czechia",
    "DE": "Germany",
    "DJ": "Djibouti",
    "DK": "Denmark",
    "DM": "Dominica",
    "DO": "Dominican Republic",
    "DZ": "Algeria",
    "EC": "Ecuador",
    "EE": "Estonia",
    "EG": "Egypt",
    "EH": "Western Sahara",
    "ER": "Eritrea",
    "ES": "Spain",
    "ET": "Ethiopia",
    "FI": "Finland",
    "FJ": "Fiji",
    "FK": "Falkland Islands",
    "FM": "Micronesia",
    "FO": "Faroe Islands",
    "FR": "France",
    "GA": "Gabon",
    "GB": "United Kingdom",
    "GD": "Grenada",
    "GE": "Georgia",
    "GF": "French Guiana",
    "GG": "Guernsey",
    "GH": "Ghana",
    "GI": "Gibraltar",
    "GL": "Greenland",
    "GM": "Gambia",
    "GN": "Guinea",
    "GP": "Guadeloupe",
    "GQ": "Equatorial Guinea",
    "GR": "Greece",
    "GS": "South Georgia",
    "GT": "Guatemala",
    "GU": "Guam",
    "GW": "Guinea-Bissau",
    "GY": "Guyana",
    "HK": "Hong Kong",
    "HM": "Heard & McDonald Islands",
    "HN": "Honduras",
    "HR": "Croatia",
    "HT": "Haiti",
    "HU": "Hungary",
    "ID": "Indonesia",
    "IE": "Ireland",
    "IL": "Israel",
    "IM": "Isle of Man",
    "IN": "India",
    "IO": "British Indian Ocean Territory",
    "IQ": "Iraq",
    "IR": "Iran",
    "IS": "Iceland",
    "IT": "Italy",
    "JE": "Jersey",
    "JM": "Jamaica",
    "JO": "Jordan",
    "JP": "Japan",
    "KE": "Kenya",
    "KG": "Kyrgyzstan",
    "KH": "Cambodia",
    "KI": "Kiribati",
    "KM": "Comoros",
    "KN": "Saint Kitts & Nevis",
    "KP": "Korea",
    "KR": "Korea",
    "KW": "Kuwait",
    "KY": "Cayman Islands",
    "KZ": "Kazakhstan",
    "LA": "Lao People's Democratic Republic",
    "LB": "Lebanon",
    "LC": "Saint Lucia",
    "LI": "Liechtenstein",
    "LK": "Sri Lanka",
    "LR": "Liberia",
    "LS": "Lesotho",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "LY": "Libya",
    "MA": "Morocco",
    "MC": "Monaco",
    "MD": "Moldova",
    "ME": "Montenegro",
    "MF": "Saint Martin",
    "MG": "Madagascar",
    "MH": "Marshall Islands",
    "MK": "North Macedonia",
    "ML": "Mali",
    "MM": "Myanmar",
    "MN": "Mongolia",
    "MO": "Macao",
    "MP": "Northern Mariana Islands",
    "MQ": "Martinique",
    "MR": "Mauritania",
    "MS": "Montserrat",
    "MT": "Malta",
    "MU": "Mauritius",
    "MV": "Maldives",
    "MW": "Malawi",
    "MX": "Mexico",
    "MY": "Malaysia",
    "MZ": "Mozambique",
    "NA": "Namibia",
    "NC": "New Caledonia",
    "NE": "Niger",
    "NF": "Norfolk Island",
    "NG": "Nigeria",
    "NI": "Nicaragua",
    "NL": "Netherlands",
    "NO": "Norway",
    "NP": "Nepal",
    "NR": "Nauru",
    "NU": "Niue",
    "NZ": "New Zealand",
    "OM": "Oman",
    "PA": "Panama",
    "PE": "Peru",
    "PF": "French Polynesia",
    "PG": "Papua New Guinea",
    "PH": "Philippines",
    "PK": "Pakistan",
    "PL": "Poland",
    "PM": "Saint Pierre & Miquelon",
    "PN": "Pitcairn",
    "PR": "Puerto Rico",
    "PS": "Palestine, State of",
    "PT": "Portugal",
    "PW": "Palau",
    "PY": "Paraguay",
    "QA": "Qatar",
    "RE": "Réunion",
    "RO": "Romania",
    "RS": "Serbia",
    "RU": "Russia",
    "RW": "Rwanda",
    "SA": "Saudi Arabia",
    "SB": "Solomon Islands",
    "SC": "Seychelles",
    "SD": "Sudan",
    "SE": "Sweden",
    "SG": "Singapore",
    "SH": "Saint Helena",
    "SI": "Slovenia",
    "SJ": "Svalbard & Jan Mayen",
    "SK": "Slovakia",
    "SL": "Sierra Leone",
    "SM": "San Marino",
    "SN": "Senegal",
    "SO": "Somalia",
    "SR": "Suriname",
    "SS": "South Sudan",
    "ST": "Sao Tome & Principe",
    "SV": "El Salvador",
    "SX": "Sint Maarten (Dutch)",
    "SY": "Syrian Arab Republic",
    "SZ": "Eswatini",
    "TC": "Turks & Caicos Islands",
    "TD": "Chad",
    "TF": "French Southern Territories",
    "TG": "Togo",
    "TH": "Thailand",
    "TJ": "Tajikistan",
    "TK": "Tokelau",
    "TL": "Timor-Leste",
    "TM": "Turkmenistan",
    "TN": "Tunisia",
    "TO": "Tonga",
    "TR": "Turkey",
    "TT": "Trinidad",
    "TV": "Tuvalu",
    "TW": "Taiwan",
    "TZ": "Tanzania",
    "UA": "Ukraine",
    "UG": "Uganda",
    "UM": "United States",
    "US": "USA",
    "UY": "Uruguay",
    "UZ": "Uzbekistan",
    "VA": "Holy See",
    "VC": "Saint Vincent",
    "VE": "Venezuela",
    "VG": "Virgin Islands (British)",
    "VI": "Virgin Islands (U.S.)",
    "VN": "Viet Nam",
    "VU": "Vanuatu",
    "WF": "Wallis & Futuna",
    "WS": "Samoa",
    "YE": "Yemen",
    "YT": "Mayotte",
    "ZA": "South Africa",
    "ZM": "Zambia",
    "ZW": "Zimbabwe",
}
