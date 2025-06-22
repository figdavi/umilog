#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

WiFiClient wifiClient;
HTTPClient http;

#define SENSOR_PIN A0

#include "secrets.h" // REMOVE THIS LINE

const char* ssid = WIFI_SSID; // Replace with your WiFi SSID
const char* password = WIFI_PASSWORD; // Replace with your WiFi password
const char* server = SERVER_URL_WITH_LOG; /* Replace with your server url
                                              + port 8000 + log endpoint
                                              (e.g., http://192.168.1.26:8000/log)
                                          */

// Send sensor data every 5 seconds
const int log_delay = 5*1000;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected!");
}

void loop() {
  HTTPClient http;
  int rawSoilMoisture = analogRead(SENSOR_PIN);

  if (WiFi.status() == WL_CONNECTED) {
    http.begin(wifiClient, server);
    http.addHeader("Content-Type", "application/json");

    String payload = "{\"raw_soil_moisture\": " + String(rawSoilMoisture) + "}";
    Serial.println(payload);

    int httpCode = http.POST(payload);
    String response = http.getString();

    Serial.println("HTTP Response code: " + httpCode);
    Serial.println("Response: " + response);

    http.end();
  }

  delay(log_delay);
}
