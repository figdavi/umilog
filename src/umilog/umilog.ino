#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

WiFiClient wifiClient;
HTTPClient http;

#define SENSOR_PIN A0

const char* ssid = "<YOUR_WIFI_SSID>";
const char* password = "<YOUR_WIFI_PASSWORD>";
const char* server = "http://<YOUR_LOCAL_SERVER_IPv4>:8000/log";

// Send sensor data every 30 minutes
const int log_delay = 30*60*1000

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
