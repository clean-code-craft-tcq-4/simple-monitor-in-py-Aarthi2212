TEMPERATURE = "Temperature"
SOC = "SOC"
CHARGE_RATE = "ChargeRate"
TEST_PARAM = "Test Param"
MIN_TEMP = 0
MAX_TEMP = 45
MIN_SOC = 20
MAX_SOC = 80
MAX_CHARGE_RATE = 0.8
CELSIUS = "°C"
FARENHEIT = "°F"
UNIT_CONVERSIONS = [{
    "From": FARENHEIT,
    "To": CELSIUS,
    "Formula": "(({}-32)*5)/9"
}]
ENGLISH = "English"
GERMAN = "German"
LANGUAGES_SUPPORTED = [ENGLISH, GERMAN]
INRANGE = "InRange"
OUT_OF_RANGE = "OutofRange"
IN_LOW_LIMIT = "InLowLimit"
OUT_OF_LOW_LIMIT = "OutofLowLimit"
IN_HIGH_LIMIT = "InHighLimit"
OUT_OF_HIGH_LIMIT = "OutofHighLimit"
LANGUAGE_TEMPLATES = {
    ENGLISH:{
        TEMPERATURE : TEMPERATURE,
        SOC : SOC,
        CHARGE_RATE : CHARGE_RATE,
        TEST_PARAM: TEST_PARAM,
        INRANGE : "{} is in range",
        OUT_OF_RANGE : "{} out of range",
        IN_LOW_LIMIT : "{} is in low limit",
        OUT_OF_LOW_LIMIT : "{} is too low",
        IN_HIGH_LIMIT : "{} is in high limit",
        OUT_OF_HIGH_LIMIT : "{} is too high"
    },
    GERMAN:{
        TEMPERATURE : "Temperatur",
        SOC : SOC,
        CHARGE_RATE : "Ladestrom",
        TEST_PARAM: "Testparam", 
        INRANGE :  "{} ist im Bereich",
        OUT_OF_RANGE : "{} außerhalb des Bereichs",
        IN_LOW_LIMIT : "Die {} ist im unteren Bereich",
        OUT_OF_LOW_LIMIT : "Die {} ist zu niedrig",
        IN_HIGH_LIMIT : "Die {} ist im oberen Bereich",
        OUT_OF_HIGH_LIMIT : "Die {} ist zu hoch"
    }
        
    }
