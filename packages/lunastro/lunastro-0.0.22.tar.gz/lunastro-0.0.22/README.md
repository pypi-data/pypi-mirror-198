## Lunastro
Lunastro is a <strong>python</strong> library for calculating astronomical data, such as, but not limited to:
<ul>
    <li>RA of the sun</li>
    <li>Hour angle of the sun</li>
    <li>Declination of the sun</li>
    <li>Longitude of the Sun's Ascending Node (Omega)</li>
    <li>Solar Geometric mean Anomaly</li>
    <li>Solar Geometric mean Longitude</li>
    <li>True Solar Longitude</li>
    <li> Distance to the sun</li>
    <li> Local sidereal time (accurate to the second) </li>
    <li> Sun altitude </li>
    <li> Sun azimuth </li>
    <li> Moon Position</li>
</ul>


## Usage
Lunastro's functions return objects of information. Here is a list of each function and what it returns:

<h1>Solar Data</h1>

```python
latitude = 47.6101 # Bellevue WA latitude
solar_data = getSunData(latitude) # get the solar data
```

This returns:

| Attribute |  Description |
|-----------------|------------------|
| dec | current solar declination |
| hour_angle | current solar hour angle |
| ra | current solar right ascension |
| long_omega | Longitude of the Sun's ascending node|
| true_solar_anomaly | true solar anomaly |
| true_solar_longitude | true solar longitude |
| geo_anomaly | geometric mean anomaly of the sun |
| geo_long | geometric mean longitude of the sun |
| dist | distance to the sun in miles |


<h1>Altitude of the Sun</h1>

```python
# lat and long are of Bellevue WA
latitude = 47.6101
longitude = -122
alt = altitude(latitude, longitude)
```

This returns the <strong>altitude</strong> of the <i>sun</i> in radians

<h1>Azimuth of the Sun</h1>

```python
# lat and long are of Bellevue WA
latitude = 47.6101
longitude = -122
azi = azimuth(latitude, longitude)
```

This returns the <strong>azimuth</strong> of the <i>sun</i> in radians


<h1>Local Sidereal Time</h1>

```python
# longitude 
long = -122
time = localSiderealTime(long)
```

This returns the <b>local sidereal time </b> as an object:
| Attribute |  Description |
|-----------------|------------------|
| raw | raw sidereal time |
| hour | hours of sidereal time |
| minute | minutes of sidereal time |
| second | seconds of sidereal time|


<h1> Moon Positioning </h1>

```python
# lat and long are of Bellevue WA
lat = 47.6101
long = -122
moon_pos = getMoonPosition(lat, long)
```

This returns the <b>positioning of the moon </b> as an object:
| Attribute |  Description |
|-----------------|------------------|
| azimuth | azimuth of the moon |
| altitude | altitude of the moon |
| distance | distance to the moon in KM |
| parallacticAngle | parallactic angle of the moon|


## Changelog

### Version 0.0.21 (March 18th 2023)

- Edited most of the files by making the functions more accurate. Changed the functions to output objects.
