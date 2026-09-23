[README.md](https://github.com/user-attachments/files/32572439/README.md)
# JAVA-Tutor-Learning-Project# 8051-Based Secure Offline Wallet

An embedded-systems project built around the AT89S52 microcontroller to demonstrate PIN-based access and basic offline wallet operations.

## Project overview

The prototype uses an IR sensor to detect a person, a 4×4 keypad for user input, and a 16×2 LCD for prompts and status messages. After authentication, the program provides a menu for balance checking, depositing, and withdrawing. LEDs provide status indication, and the buzzer is listed among the project components.

> **Implementation note:** The supplied Assembly program keeps the registered ID, PIN, balance, and wrong-attempt counter in internal RAM. It does not contain EEPROM read/write routines. The report lists EEPROM as a component, but persistent EEPROM storage is not demonstrated by this source file. Also, the report mentions fund transfer, while the supplied program implements deposit and withdrawal; confirm/implement transfer before describing it as a completed feature.

## Features shown in the supplied source

- IR-low user detection loop
- Two-character user ID entry
- Four-digit PIN entry with masked LCD display
- Login validation against values held in RAM
- Three-attempt lock message and `#` key reset
- Balance display
- Deposit and withdrawal flow, including low-balance handling
- LCD messages and green/red LED status indication

## Hardware and tools

- AT89S52 8051 microcontroller
- 4×4 keypad
- 16×2 LCD
- IR sensor
- Green and red LEDs
- Buzzer (listed in the project description; not directly driven in the supplied program)
- MB102 power module, breadboard and jumper wires
- 11.0592 MHz crystal, capacitors, resistors, contrast potentiometer and reset push button
- Keil uVision / A51 Assembly
- Proteus (for circuit design/simulation, if applicable)

## Repository layout

```text
Secure-Offline-Wallet-8051/
├── README.md
├── src/
│   └── secure_offline_wallet.a51
├── docs/
│   └── project-report.pdf
└── hardware/
    └── circuit-diagram-page.jpg
```

## How to inspect

1. Open `src/secure_offline_wallet.a51` in Keil uVision configured for the appropriate 8051 target.
2. Review the wiring diagram in `hardware/`.
3. Refer to the report in `docs/` for the project background, component list, objectives, and development schedule.

This repository contains project documentation and source supplied by the student. Verify the hardware and behavior in the target setup before relying on it as a production security or financial system.

## Author

Deepak Kumar Mohapatra  
B.Tech, Electronics and Communication Engineering
