import datetime
import calendar
import math


class Dates:
    def __init__(self, data):
        self.__dict__ = data


def juliandate(now):
    """
    :param now: preferably inputted as `datetime.datetime.now()`
    :return: Julian date
    """
    y = now.year  # year
    m = now.month  # month
    d = now.day  # day
    if m == 1 or m == 2:  # add 12 to the month -1 from the year
        y = y - 1  # -1 from the year
        m = m + 12  # add 1
    A = math.floor(y / 100)
    B = 2 - A + math.floor(A / 4)
    C = math.floor(365.25 * y)
    D = math.floor(30.6001 * (m + 1))
    return B + C + D + d + 1720994.5  # return Julian Date


def planetMeanAnomaly(planet):
    """
    :param planet: An str that contains the planet's name
    :return: the planet's mean anomaly
    """
    planet = planet.lower()
    m01 = {"mercury": [174.7948, 4.09233445],
           "venus": [50.4161, 1.60213034],
           "earth": [357.5291, 0.98560028],
           'mars': [19.3730, 0.52402068],
           'jupiter': [20.0202, 0.08308529],
           'saturn': [317.0207, 0.03344414],
           'uranus': [141.0498, 0.01172834],
           'neptune': [256.2250, 0.00598103],
           'pluto': [14.882, 0.00396]
           }
    j = juliandate(datetime.datetime.now())
    m_list = m01[planet]
    m0 = m_list[0]
    m1 = m_list[1]
    m = (m0 + m1 * (j - 2451545)) % 360
    return m


def planetEquationOfCenter(planet):
    """
    :param planet: an str that contains the planet's name (pluto is supported)
    :return: the planet's equation of center
    """
    """
    The orbits of the planets are not perfect circles but rather ellipses, so the speed of the planet in its orbit 
    varies,and therefore the apparent speed of the Sun along the ecliptic also varies throughout the planet's year. This
    correction factor is called the equation of center
    """
    c_dict = {
        "mercury": [23.4400, 2.9818, 0.5255, 0.1058, 0.0241, 0.0055],  # 0.0026 is the maximum error
        "venus": [0.7758, 0.0033, 0, 0, 0, 0],  # 0.0000 is the maximum error
        "earth": [1.9148, 0.0200, 0.0003, 0, 0, 0],  # 0.0000 is the maximum error
        "mars": [10.6912, 0.6228, 0.0503, 0.0046, 0.0005, 0],  # 0.0001 is the maximum error
        "jupiter": [5.5549, 0.1683, 0.0071, 0.0003, 0, 0],  # 0.0001 is the maximum error
        "saturn": [6.3585, 0.2204, 0.0106, 0.0006, 0, 0],  # 0.0001 is the maximum error
        "uranus": [5.3042, 0.1534, 0.0062, 0.0003, 0, 0],  # 0.0001 is the maximum error
        "neptune": [1.0302, 0.0058, 0, 0, 0, 0],  # 0.0001 is the maximum error
        "pluto": [28.3150, 4.3408, 0.9214, 0.2235, 0.0627, 0.0174]  # 0.0096 is the maximum error
    }
    # the formula used is from https://www.aa.quae.nl/en/reken/zonpositie.html#10
    # c = c1 * sin(m) + c2 * sin(2m) + c3 * sin(3m) + c4 * sin(4m) + c5 * sin(5m) + c6 * sin(6m)

    if planet.lower() in c_dict.keys():
        c = c_dict[planet.lower()]
    else:
        raise ValueError("planet is invalid")
    m = planetMeanAnomaly(planet.lower())
    center_eq = c[0] * math.sin(m) + c[1] * math.sin(2 * m) + c[2] * math.sin(3 * m) + c[3] * math.sin(4 * m) + \
                c[4] * math.sin(5 * m) + c[5] * math.sin(6 * m)
    return center_eq


def planetTrueAnomaly(planet):
    m = planetMeanAnomaly(planet)  # this is the mean anomaly of the planet
    c = planetEquationOfCenter(planet)  # this is the eq of center (correction factor)
    return m + c  # corrected anomaly


def astroNorthernSeasonDates(year):
    # Calculate the spring equinox
    spring_equinox = (datetime.datetime(year, 3, 20, 21, 58) + datetime.timedelta(days=calendar.isleap(year))). \
        strftime("%h %d:%H:%S, %Y")
    # Calculate the summer solstice
    summer_solstice = (datetime.datetime(year, 6, 21, 10, 31) + datetime.timedelta(days=calendar.isleap(year))). \
        strftime("%h %d:%H:%S, %Y")
    # Calculate the autumnal equinox
    autumnal_equinox = (datetime.datetime(year, 9, 22, 19, 21) + datetime.timedelta(days=calendar.isleap(year))). \
        strftime("%h %d:%H:%S, %Y")
    # Calculate the winter solstice
    winter_solstice = (datetime.datetime(year, 12, 21, 15, 59) + datetime.timedelta(days=calendar.isleap(year))). \
        strftime("%h %d:%H:%S, %Y")

    # Return a dictionary of the astronomical seasons
    return Dates({
        'spring': spring_equinox,
        'summer': summer_solstice,
        'autumn': autumnal_equinox,
        'winter': winter_solstice
    })


def astroSouthernSeasonDates(year):
    # Calculate the autumnal equinox for the Southern Hemisphere
    autumnal_equinox = (datetime.datetime(year, 3, 20, 21, 58) + datetime.timedelta(days=calendar.isleap(year))). \
        strftime("%h %d:%H:%S, %Y")
    # Calculate the winter solstice for the Southern Hemisphere
    winter_solstice = (datetime.datetime(year, 6, 21, 10, 31) + datetime.timedelta(days=calendar.isleap(year))). \
        strftime("%h %d:%H:%S, %Y")
    # Calculate the spring equinox for the Southern Hemisphere
    spring_equinox = (datetime.datetime(year, 9, 22, 19, 21) + datetime.timedelta(days=calendar.isleap(year))). \
        strftime("%h %d:%H:%S, %Y")
    # Calculate the summer solstice for the Southern Hemisphere
    summer_solstice = (datetime.datetime(year, 12, 21, 15, 59) + datetime.timedelta(days=calendar.isleap(year))). \
        strftime("%h %d:%H:%S, %Y")

    # Return a dictionary of the astronomical seasons
    return Dates({
        'autumn': autumnal_equinox,
        'winter': winter_solstice,
        'spring': spring_equinox,
        'summer': summer_solstice,
    })


LUNAR_MONTH = 29.530588853


def get_lunar_age(date=datetime.date.today()):
    percent = get_lunar_age_percent(date)
    age = percent * LUNAR_MONTH
    return age


def get_lunar_age_percent(date=datetime.date.today()):
    julian_date = juliandate(date)
    return normalize((julian_date - 2451550.1) / LUNAR_MONTH)


def normalize(value):
    value = value - int(value)
    if value < 0:
        value = value + 1
    return value


def getLunarPhase(date=datetime.datetime.now()):
    age = get_lunar_age(date)
    if age < 1.84566:
        return "New"
    elif age < 5.53699:
        return "Waxing Crescent"
    elif age < 9.22831:
        return "First Quarter"
    elif age < 12.91963:
        return "Waxing Gibbous"
    elif age < 16.61096:
        return "Full"
    elif age < 20.30228:
        return "Waning Gibbous"
    elif age < 23.99361:
        return "Last Quarter"
    elif age < 27.68493:
        return "Waning Crescent"
    return "New"


def enthalpy(cp, m, delta_t):
    """
    Calculate enthalpy of a substance.
    :param cp: specific heat capacity of the substance
    :param m: mass of the substance
    :param delta_t: change in temperature of the substance
    :return: enthalpy of the substance
    """
    return cp * m * delta_t


def specificHeat(cp, m):
    """
    Calculate specific heat of a substance.
    :param cp: specific heat capacity of the substance
    :param m: mass of the substance
    :return: specific heat of the substance
    """
    return cp * m


def entropy(q, t):
    """
    Calculate entropy of a substance.
    :param q: heat added or removed from the substance
    :param t: temperature of the substance
    :return: entropy of the substance
    """
    return q / t


def internalEnergy(cv, m, delta_t):
    """
    Calculate internal energy of a substance.
    :param cv: specific heat capacity at constant volume of the substance
    :param m: mass of the substance
    :param delta_t: change in temperature of the substance
    :return: internal energy of the substance
    """
    return cv * m * delta_t


def gibbs_free_energy(h, t, s):
    """
    Calculate Gibbs free energy of a substance.
    :param h: enthalpy of the substance
    :param t: temperature of the substance
    :param s: entropy of the substance
    :return: Gibbs free energy of the substance
    """
    return h - t * s


def ideal_gas_law(p, v, n, r=8.314):
    """
    Calculate the ideal gas law for a gas.
    :param p: pressure of the gas
    :param v: volume of the gas
    :param n: number of moles of the gas
    :param r: universal gas constant (default is 8.314 J/(mol*K))
    :return: temperature of the gas
    """
    return (p * v) / (n * r)


def peng_robinson_eos(p, v, n, tc, pc, omega):
    import cmath
    """
    Calculate the Peng-Robinson equation of state for a gas.
    :param p: pressure of the gas
    :param v: volume of the gas
    :param n: number of moles of the gas
    :param tc: critical temperature of the gas
    :param pc: critical pressure of the gas
    :param omega: acentric factor of the gas
    :return: temperature of the gas
    """
    r = 8.314
    a = 0.45724 * (r * tc) ** 2 / pc
    b = 0.07780 * r * tc / pc
    alpha = (1 + (0.37464 + 1.54226 * omega - 0.26992 * omega ** 2) * (1 - (v / n) ** 0.5)) ** 2
    a_alpha = a * alpha
    b_alpha = b
    coeffs = [1, -(1 - b_alpha), a_alpha - 2 * b_alpha - 3 * b_alpha ** 2,
              -a_alpha * b_alpha + b_alpha ** 2 + b_alpha ** 3, a_alpha * b_alpha ** 2 - b_alpha ** 2 - b_alpha ** 3]
    z = [coef.real for i, coeff in enumerate(coeffs[:-1]) for coef in
         [cmath.sqrt(((-1) ** (i + 1)) * coeff / coeffs[-1]).real]]
    zl = min(z)
    zh = max(z)
    delta_g = a_alpha * (zh - zl) - r * tc * cmath.log((zl + b_alpha) / (zh + b_alpha)).real
    return (p * v + n ** 2 * delta_g) / (n * r)


def heat_flux(delta_T, k, thickness):
    """
    Calculate the heat flux through a material.

    :param delta_T: temperature difference across the material (in K)
    :param k: thermal conductivity of the material (in W/m.K)
    :param thickness: thickness of the material (in m)
    :return: heat flux through the material (in W/m^2)
    """
    return k * delta_T / thickness


def thermal_conductivity(diffusivity, specific_heat, density):
    """
    Calculate the thermal conductivity of a material given its thermal diffusivity,
    specific heat capacity, and density.

    :param diffusivity: thermal diffusivity of the material (in m^2/s)
    :param specific_heat: specific heat capacity of the material (in J/kg K)
    :param density: density of the material (in kg/m^3)
    :return: thermal conductivity of the material (in W/m K)
    """
    return diffusivity * specific_heat * density


def calculate_diffusivity(k, rho, cp):
    """
    Calculate the diffusivity of a material in m^2/s given its thermal conductivity (k),
    density (rho), and specific heat capacity (cp).
    """
    return k / (rho * cp)


class Star:
    def __init__(self, mass, age, distance):
        self.mass = mass
        self.age = age
        self.radius = None
        self.luminosity = None
        self.surface_temperature = None
        self.core_temperature = None
        self.apparent_brightness = None
        self.absolute_brightness = None
        self.distance = distance

    def calculate_luminosity(self):
        self.luminosity = self.mass ** 3.5
        return self.luminosity

    def calculate_surface_temperature(self):
        if self.luminosity is None:
            self.calculate_luminosity()
        if self.radius is None:
            self.calculate_radius()
        sigma = 5.67e-8
        self.surface_temperature = (self.luminosity / (4 * math.pi * sigma * self.radius ** 2)) ** 0.25
        return self.surface_temperature

    def calculate_radius(self):
        self.radius = (self.mass ** 0.8) * 1.1
        return self.radius

    def calculate_core_temperature(self):
        if self.mass is None:
            raise ValueError("Mass must be calculated before core temperature")
        if self.radius is None:
            self.calculate_radius()
        G = 6.6743e-11
        mu = 0.62  # mean molecular weight of ionized hydrogen
        self.core_temperature = ((self.mass * 2 * G) / (3 * mu * self.radius)) ** (1 / 3)
        return self.core_temperature

    def calculate_apparent_brightness(self):
        if self.luminosity is None:
            self.calculate_luminosity()
        if self.radius is None:
            self.calculate_radius()
        self.calculate_absolute_brightness()
        self.apparent_brightness = self.absolute_brightness + 5 * (math.log10(self.distance) - 1)
        return self.apparent_brightness

    def calculate_absolute_brightness(self):
        if self.luminosity is None:
            self.calculate_luminosity()
        if self.distance is None:
            raise ValueError("Distance must be known before calculating absolute brightness")
        self.absolute_brightness = self.luminosity - 2.5 * (math.log10(self.distance / 10)) ** 2
        return self.absolute_brightness


def getElementName(number):
    element_names = [
         # a list of the elements in the periodic table
         "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",  # the elements are listed in order
         "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
         "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus",
         "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium",
         "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese",
         "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
         "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine",
         "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
         "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium",
         "Palladium", "Silver", "Cadmium", "Indium", "Tin",
         "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium",
         "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
         "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium",
         "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
         "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium",
         "Osmium", "Iridium", "Platinum", "Gold", "Mercury",
         "Thallium", "Lead", "Bismuth", "Polonium", "Astatine",
         "Radon", "Francium", "Radium", "Actinium", "Thorium",
         "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium",
         "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
         "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium",
         "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium",
         "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium",
         "Livermorium", "Tennessine", "Oganesson"  # the elements have weird names
     ]
    if number < 1 or number > 118:
        return None
    else:
        return element_names[number - 1]


def setInstVelocity(x1, y1, z1, x2, y2, z2, t1, t2):
    if t2 == t1:
        raise ZeroDivisionError("Both times are exactly the same, this causes the program to divide by 0")
    vx = (x2 - x1) / (t2 - t1)
    vy = (y2 - y1) / (t2 - t1)
    vz = (z2 - z1) / (t2 - t1)
    inst_velocity = [vx, vy, vz]
    return inst_velocity


def setInstSpeed(x1, y1, z1, x2, y2, z2, t1, t2):
    vx = (x2 - x1) / (t2 - t1)
    vy = (y2 - y1) / (t2 - t1)
    vz = (z2 - z1) / (t2 - t1)
    speed = math.sqrt(vx ** 2 + vy ** 2 + vz ** 2)
    return speed


def setVolumeSphere(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    return volume


def setVolumeCylinder(radius, height):
    V = math.pi * radius ** 2 * height
    return V


def setVolumeCone(radius, height):
    V = (1 / 3) * math.pi * radius ^ 2 * height
    return V


def setConeSurfaceArea(radius, height):
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    sa = math.pi * radius * slant_height + math.pi * radius ** 2
    return sa


def setCylinderSurfaceArea(radius, height):
    sa = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
    return sa


def setCharge(electrons):
    e = 1.602e-19
    q = electrons * e
    charge = q
    return charge


class Sun:
    def __init__(self, data):
        self.__dict__ = data


class LST:
    def __init__(self, data):
        self.__dict__ = data


class Moon:
    def __init__(self, data):
        self.__dict__ = data


def getSunData(latitude: float, date=datetime.datetime.now()) -> Sun:
    """
    :param latitude: latitude of the user
    :param date: any date the user wishes
    :return: an object that contains solar information
    """

    if latitude > 90 or latitude < -90:
        raise ValueError("Latitude out of range (-90, 90)")

    """
    SOLAR DISTANCE (MILES)
    """
    lat = latitude
    now = date
    # Calculate the Julian date
    julian_date = 367 * now.year - int(7 * (now.year + int((now.month + 9) / 12)) / 4) + int(
        275 * now.month / 9) + now.day + 1721013.5 + now.hour / 24 + now.minute / 1440 + now.second / 86400
    # days since greenwich noon
    n = julian_date - 2451545
    # positions
    # g is mean anomaly
    g = 357.528 + 0.9856003 * n
    tmp = math.cos(g)
    temp_two = math.cos(2 * g)
    # solar distance is in astronomical units
    solar_distance = (1.00014 - 0.01671 * tmp - 0.00014 * temp_two)

    """
    DECLINATION
    """
    current_utc = datetime.datetime.utcnow()
    day_of_year = current_utc.timetuple().tm_yday
    solar_declination = -23.45 * math.cos(math.radians((360 / 365) * (day_of_year + 10)))

    """
    GEOMETRIC MEAN LONGITUDE
    """
    jd = julian_date
    # Calculate the Julian Century (JC) for the given JD
    jc = (jd - 2451545) / 36525
    # Calculate the Geometric Mean Longitude of the Sun (L0) in degrees
    l0 = 280.46646 + jc * (36000.76983 + jc * 0.0003032) % 360

    """
    GEOMETRIC MEAN ANOMALY
    """
    # Calculate the Geometric Mean Anomaly of the Sun (M) in degrees
    m = 357.52911 + jc * (35999.05029 - 0.0001537 * jc)

    """
    TRUE SOLAR LONGITUDE
    """
    # Calculate the Eccentricity of Earth's Orbit (e)
    # Calculate the Equation of Center (C) in degrees
    c = math.sin(math.radians(m)) * (1.914602 - jc * (0.004817 + 0.000014 * jc)) + math.sin(math.radians(2 * m)) * (
            0.019993 - 0.000101 * jc) + math.sin(math.radians(3 * m)) * 0.000289
    # Calculate the True Longitude of the Sun (tl) in degrees
    tl = l0 + c

    """
    TRUE SOLAR ANOMALY
    """
    # calculate the true solar anomaly (v)
    v = m + c

    """
    LONGITUDE OF OMEGA
    """
    omega = 125.04 - 1934.136 * jc

    """
    SUN'S RIGHT ASCENSION (DEGREES) (ALPHA)
    """
    # Calculate the Mean Obliquity of the Ecliptic (epsilon) in degrees
    epsilon = 23.439291 - jc * (0.0130042 + 0.00000016 * jc)

    # Calculate the Sun's Right Ascension (alpha) in degrees
    alpha = math.degrees(
        math.atan2(math.cos(math.radians(epsilon)) * math.sin(math.radians(tl)), math.cos(math.radians(tl))))

    # Convert alpha to the range 0-360 degrees
    alpha = (alpha + 360) % 360

    """
    HOUR ANGLE
    """
    lat_rad = math.radians(lat)
    H = math.degrees(math.acos(
        (math.sin(math.radians(-0.83)) - math.sin(math.radians(lat_rad)) * math.sin(
            math.radians(solar_declination))) / (
                math.cos(math.radians(lat_rad)) * math.cos(math.radians(solar_declination)))))

    values = {
        "dec": solar_declination,
        "hour_angle": H,
        "ra": alpha,
        "long_omega": omega,
        "true_solar_anomaly": v,
        "true_solar_longitude": tl,
        "geo_anomaly": m,
        "geo_long": l0,
        "dist": solar_distance,
    }

    return Sun(values)


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def decimalhours(now):
    return (((now.second / 60) + now.minute) / 60) + now.hour


def gst(jd, dechours):
    S = jd - 2451545
    T = S / 36525
    T0 = 6.697374558 + (2400.051336 * T) + (0.000025862 * T ** 2)
    if T0 < 0:
        T0 = (T0 + abs(T0) // 24 * 24) % 24
    else:
        T0 = T0 % 24
    T0 = T0 + (dechours * 1.002737909)
    if T0 < 0:
        T0 = T0 + 24
    if T0 > 24:
        T0 = T0 - 24
    return T0


def localSiderealTime(long):
    now = datetime.datetime.utcnow()
    jd = juliandate(now)
    dechours = decimalhours(now)
    gstime = gst(jd, dechours)
    LONGITUDE = long
    utcdiff = math.fabs(LONGITUDE) / 15
    if sign(LONGITUDE) == -1:
        lstime = gstime - utcdiff
    else:
        lstime = gstime + utcdiff
    if lstime > 24:
        lstime = lstime - 24
    if lstime < 0:
        lstime = lstime + 24

    raw = lstime
    h = math.floor(lstime)
    m = math.floor((lstime - h) * 60)
    s = math.floor((((lstime - h) * 60) - m) * 60)

    times = {
        "raw": raw,
        "hour": h,
        "minute": m,
        "second": s
    }
    return LST(times)



def declination(l, b):
    e = math.radians(23.4397)  # obliquity of the ecliptic in degrees
    return math.asin(
        math.sin(math.radians(b)) * math.cos(e) + math.cos(math.radians(b)) * math.sin(e) * math.sin(math.radians(l)))


def eclipticLongitude(M):
    rad = math.pi / 180.0
    PI = math.pi

    C = rad * (1.9148 * math.sin(M) + 0.02 * math.sin(2 * M) + 0.0003 * math.sin(3 * M))  # equation of center
    P = rad * 102.9372  # perihelion of the Earth

    return M + C + P + PI


def solarMeanAnomaly(d):
    rad = math.pi / 180.0
    return rad * (357.5291 + 0.98560028 * d)


def daysSinceJ2000():
    # get current date and time in UTC
    now = datetime.datetime.utcnow()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    # calculate Julian Date
    a = math.floor((14 - month) / 12)
    Y = year + 4800 - a
    M = month + 12 * a - 3
    D = day
    UT = hour + minute / 60 + second / 3600
    JD = 367 * Y - math.floor(7 * (Y + math.floor((M + 9) / 12)) / 4) + math.floor(
        275 * M / 9) + D + 1721013.5 + UT / 24

    # calculate number of days since J2000.0
    days = (JD - 2451545.0) + (UT - 12) / 24
    return days


def altitude(lat, long):
    d = daysSinceJ2000()
    M = solarMeanAnomaly(d)
    L = eclipticLongitude(M)
    dec = declination(L, 0)
    H = solarHourAngle(long, localSiderealTime(long).raw)
    a = math.asin(math.sin(lat) * math.sin(dec) + math.cos(lat) * math.cos(dec) * math.cos(H))
    return a


def azimuth(lat, long):
    d = daysSinceJ2000()
    M = solarMeanAnomaly(d)
    L = eclipticLongitude(M)
    H = solarHourAngle(long, localSiderealTime(long).raw)
    dec = declination(L, 0)
    return math.atan2(math.sin(H), math.cos(H) * math.sin(lat) - math.tan(dec) * math.cos(lat))


def solarHourAngle(longitude, lst):
    """Calculate the solar hour angle for a given longitude and local sidereal time."""
    # Convert longitude and LST to radians
    longitude = math.radians(longitude)
    lst = math.radians(lst)
    # Calculate the solar noon for the given longitude
    solarNoon = longitude + (12 - 12 * 4.0 / 1440) * math.radians(360) / 24
    # Calculate the solar hour angle
    hourAngle = lst - solarNoon
    return hourAngle


def rightAscension(l, b):
    e = math.pi/180 * 23.4397
    return math.atan2(math.sin(l) * math.cos(e) - math.tan(b) * math.sin(e), math.cos(l))


def sunRA():
    d = daysSinceJ2000()
    M = solarMeanAnomaly(d)
    L = eclipticLongitude(M)
    return rightAscension(L, 0)


def moonCoords():
    rad = math.pi/180
    d = daysSinceJ2000()
    L = rad * (218.316 + 13.176396 * d)
    M = rad * (134.963 + 13.064993 * d)
    F = rad * (93.272 + 13.229350 * d)
    l = L + rad * 6.289 * math.sin(M)
    b = rad * 5.128 * math.sin(F)
    dt = 385001 - 20905 * math.cos(M)
    values = {
        'ra': rightAscension(l, b),
        'dec': declination(l, b),
        'dist': dt
    }
    return Moon(values)


def astronomicalRefraction(h):
    if h < 0:
        h = 0
    return 0.0002967 / math.tan(h + 0.00312536 / (h + 0.08901179))


def moon_azimuth(h, phi, dec):
    H = h
    return math.atan2(math.sin(H), math.cos(H) * math.sin(phi) - math.tan(dec) * math.cos(phi))


def moon_altitude(H, phi, dec):
    return math.asin(math.sin(phi) * math.sin(dec) + math.cos(phi) * math.cos(dec) * math.cos(H))


def tmpSiderealTime(d, lw):
    return math.radians(280.16 + 360.9856235 * d) - lw


def getMoonPosition(lat, long):
    rad = math.pi / 180
    lw = rad * -long
    phi = rad * lat
    d = daysSinceJ2000()
    c = moonCoords()
    H = tmpSiderealTime(d, lw) - c.ra
    alt = moon_altitude(H, phi, c.dec)
    pa = math.atan2(math.sin(H), math.tan(phi) * math.cos(c.dec) - math.sin(c.dec) * math.cos(H))
    alt += astronomicalRefraction(alt)

    values = {
        'azimuth': moon_azimuth(H, phi, c.dec),
        'altitude': alt,
        'distance': c.dist,
        'parallacticAngle': pa,
        'phase': getLunarPhase(datetime.datetime.now())
    }
    return Moon(values)


