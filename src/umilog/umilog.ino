#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

WiFiClient wifiClient;

#define SENSOR_PIN A0

const char* ssid = "XXXX";
const char* password = "****";

const char* server = "http://192.168.1.26:8000/log";

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
  int soil_moisture = analogRead(SENSOR_PIN);
  Serial.print("Soil Moisture: ");
  Serial.println(soil_moisture);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin(wifiClient, server);
    http.addHeader("Content-Type", "application/json");

    String payload = "{\"soil_moisture\": " + String(soil_moisture) + "}";

    int httpCode = http.POST(payload);
    String response = http.getString();

    Serial.print("HTTP Response code: ");
    Serial.println(httpCode);
    Serial.println("Response: " + response);

    http.end();
  }

  delay(5000);
}
