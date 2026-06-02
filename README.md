# 🚀 AstroHealth & Space Safety Dashboard

An AI-powered mission control dashboard that combines **Astronaut Health Monitoring** and **Satellite Collision Prevention** into a unified real-time intelligence platform.

The system continuously analyzes astronaut vitals, tracks satellites and orbital debris, detects anomalies using Machine Learning, and generates predictive alerts for mission operators. Designed as a scalable prototype, the platform can be adapted for future applications in ISRO, NASA, ESA missions, smart healthcare systems, and autonomous space operations. 

---

## 🌟 Features

### 👨‍🚀 Astronaut Health Monitoring

* Real-time monitoring of:

  * Heart Rate
  * Blood Oxygen (SpO₂)
  * Stress Levels
  * Bone Density Risk
  * Muscle Health Metrics
* AI-based anomaly detection
* Early warning alerts for abnormal vitals
* Historical trend analysis

### 🛰️ Satellite & Space Debris Monitoring

* Real-time satellite tracking
* Orbital trajectory visualization
* Space debris detection
* Collision risk prediction
* Automated warning generation

### 🤖 AI & Machine Learning

* Isolation Forest for anomaly detection
* Predictive analytics for health risks
* Future orbit behavior forecasting
* Pattern recognition from telemetry streams

### 📊 Interactive Dashboard

* Real-time mission overview
* Health analytics panels
* Satellite tracking visualization
* Alert management system
* Historical data insights

### 🔄 Real-Time Data Streaming

* MQTT-based telemetry communication
* WebSocket support
* Low-latency event processing
* Continuous monitoring architecture

---

# 🏗️ System Architecture

```text
Astronaut Sensors
        │
        ▼
Telemetry Simulation
        │
        ▼
 MQTT / WebSockets
        │
        ▼
 FastAPI Backend
        │
 ┌──────┴──────┐
 ▼             ▼
AI Engine   Database
 │             │
 ▼             ▼
Alert System  Logs
      │
      ▼
Real-Time Dashboard
      │
      ▼
Mission Operators
```

The architecture integrates astronaut telemetry, satellite tracking systems, AI prediction engines, and real-time communication channels into a centralized monitoring platform. 

---

# 🧠 AI Models Used

## Anomaly Detection

* Isolation Forest
* Detects unusual astronaut vitals
* Identifies abnormal satellite behavior

## Predictive Analytics

* Regression Models
* Health risk forecasting
* Orbit decay prediction
* Fuel consumption estimation

## Risk Assessment Engine

* Collision probability calculation
* Debris threat classification
* Mission safety recommendations

---

# 🛠️ Tech Stack

## Frontend

* React.js
* Tailwind CSS
* Plotly.js
* CesiumJS / Three.js

## Backend

* FastAPI
* Python

## Database

* SQLite

## Real-Time Communication

* MQTT
* WebSockets

## Machine Learning

* Scikit-Learn
* Pandas
* NumPy

## Satellite Tracking

* SGP4
* Skyfield
* TLE Data Processing

---

# 📂 Project Structure

```bash
astro-health-dashboard/
│
├── frontend/
│   ├── dashboard-ui
│   ├── charts
│   └── satellite-visualization
│
├── backend/
│   ├── api
│   ├── services
│   ├── telemetry
│   └── websocket
│
├── ml/
│   ├── anomaly_detection
│   ├── prediction_models
│   └── training
│
├── database/
│   ├── sqlite
│   └── migrations
│
├── docs/
│   ├── SDS
│   ├── diagrams
│   └── architecture
│
└── README.md
```

---

# 📊 Database Design

### Astronaut Table

Stores astronaut profile information:

* Name
* Mission ID
* Rank
* Contact Information

### Astronaut Vitals Table

Stores:

* Heart Rate
* Blood Pressure
* Oxygen Level
* Bone Density
* Muscle Mass
* Activity Levels

### Alerts Table

Stores:

* Alert Type
* Severity
* Timestamp
* Status
* Recipient

### System Logs

Tracks:

* Events
* Actions
* User Activities
* Monitoring Logs

### Configuration Settings

Stores:

* Threshold Values
* Alert Rules
* Monitoring Parameters



---

# 🔄 Workflow

1. Collect astronaut telemetry data.
2. Receive satellite orbit information.
3. Stream data using MQTT/WebSockets.
4. Store telemetry in database.
5. Process data using AI models.
6. Detect anomalies and risks.
7. Generate alerts.
8. Visualize insights on dashboard.
9. Assist mission operators in decision-making.

---

# 📈 Testing Strategy

The system incorporates:

### Unit Testing

* API validation
* ML model verification

### Integration Testing

* Backend ↔ Database
* MQTT ↔ Dashboard

### System Testing

* End-to-end mission simulation

### Performance Testing

* Real-time latency validation
* High-volume telemetry testing

### Security Testing

* Authentication checks
* API vulnerability testing

### Reliability Testing

* Recovery from network failures
* Database backup validation



---

# 🔮 Future Enhancements

* Integration with real NASA/ISRO mission feeds
* Advanced AI-powered digital twin for astronauts
* Autonomous collision avoidance recommendations
* Deep learning health prediction models
* Cloud deployment on AWS/Azure/GCP
* Edge AI support for spacecraft systems
* Multi-mission fleet monitoring

---

# 🌍 Potential Applications

### Space Missions

* ISRO
* NASA
* ESA
* SpaceX

### Healthcare

* Remote Patient Monitoring
* ICU Observation Systems
* Wearable Health Analytics

### Defense & Aerospace

* Satellite Fleet Monitoring
* Space Situational Awareness
* Autonomous Mission Control

---




