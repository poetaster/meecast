VERSION = 0.9.15
TEMPLATE = subdirs
CONFIG += ordered

SUBDIRS += omweather-fmi-fi-stations-db omweather-weather-com-stations-db omweather-gismeteo-ru-stations-db omweather-yr-no-stations-db omweather-foreca-com-stations-db omweather-bom-gov-au-stations-db omweather-hko-gov-hk-stations-db omweather-openweathermap-org-stations-db meecast/sqlite3 meecast/libxml2 meecast/core meecast/predeamon meecast/meegotouchplugin
OTHER_FILES += rpm/meecastd.spec
