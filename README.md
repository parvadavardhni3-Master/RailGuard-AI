# RailGuard AI 🚦

**Team ID:** HSC|TN|03285  
**Team Name:** Parvada Vardhni S.  
**Institution:** Sri Sai Ram Engineering College  
**State:** Tamil Nadu

## Problem
At railway level crossings, pedestrians and two-wheeler riders may enter a closed-gate danger zone. RailGuard AI is a prototype concept for detecting such unsafe entry, showing an alert, and notifying a gate operator.

## Prototype status
This repository contains a **basic demo**, sample events, and a rule-based simulation. It does not connect to railway infrastructure and does not perform validated real-time computer vision. It must not be used as a real railway safety system.

## Features
- Demo dashboard showing gate state and simulated detection events
- Alerts for a pedestrian or two-wheeler entering a danger zone while the gate is closed
- Sample data in `data/sample_events.json`
- Basic automated tests using Python's standard library
- Architecture and setup documentation

## Quick start
Requirements: Python 3.9+ (for tests) and any modern browser.

1. Download or clone this repository.
2. Open `index.html` in a browser to view the demo dashboard.
3. To run tests:
   ```bash
   python -m unittest discover -s tests -v
   ```

No API keys or environment variables are required for this demo. A future camera/AI integration would require a separately configured detection service and secure operator notification endpoint.

## Project structure
```text
RailGuard-AI/
├── index.html
├── app.js
├── styles.css
├── data/sample_events.json
├── docs/TECHNICAL_DESIGN.md
├── tests/test_detection.py
├── LICENSE
└── README.md
```

## Demo logic
An unsafe event is flagged when `gate_closed` is `true` and `in_danger_zone` is `true`. The dashboard uses sample/simulated data only.

## Test cases
See `tests/test_detection.py` and `data/sample_events.json`.

## Safety and limitations
This is an educational prototype only. It is not certified, not connected to railway signalling, and must never replace approved railway safety procedures, barriers, alarms, or trained operators. Real deployment would require domain-expert review, privacy/security controls, extensive validation, fail-safe design, and authorization from the relevant railway authorities.

## License
Released under the MIT License. See `LICENSE`.
