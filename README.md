# Round Robin Scheduling App

A Kivy-based application to simulate the **Round Robin CPU Scheduling Algorithm**. This app allows users to input the number of processes, their arrival times, burst times, and the time quantum, and then calculates the scheduling order, average waiting time, average turnaround time, and context switches.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Structure](#structure)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)

---

## Program Demo 

![Round Robin](https://github.com/Poyamohamadi/Round_Robin/blob/main/demo.gif)

---

## Features

- **Dynamic Process Input**: Users can specify the number of processes dynamically.
- **Interactive UI**: Built with Kivy, providing an intuitive and responsive user interface.
- **Round Robin Scheduling**: Implements the Round Robin algorithm to calculate:
  - Scheduling order
  - Average waiting time
  - Average turnaround time
  - Number of context switches
- **Validation**: Ensures all inputs are valid before proceeding to the next step.
- **Visualization**: Displays the scheduling order in a clear and visually appealing format.

---

## Installation

To run this application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Poyamohamadi/Round_Robin.git
   cd Round_Robin
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

---

## Usage

1. **Enter the Number of Processes**:
   - On the first screen, input the number of processes you want to simulate.

2. **Input Arrival Times**:
   - Enter the arrival times for each process.

3. **Input Burst Times**:
   - Specify the burst times for each process.

4. **Set the Time Quantum**:
   - Provide the time quantum value for the Round Robin algorithm.

5. **View Results**:
   - The app will display the scheduling order, average waiting time, average turnaround time, and the number of context switches.

---

## Structure

The application is organized into the following classes and screens:

- **ManagerScreen**: Manages transitions between different screens.
- **NumProcesses**: Allows users to input the number of processes.
- **Processes**: Collects arrival times for each process.
- **RequestTimes**: Collects burst times for each process.
- **Quantum**: Accepts the time quantum value and displays results.
- **Result**: Displays the final output of the Round Robin algorithm.

The `round_robin` function implements the core logic of the Round Robin scheduling algorithm.

---

## Dependencies

- **Python 3.8+**: The application is written in Python and requires version 3.8 or higher.
- **Kivy**: A Python framework for developing multitouch applications.

---

## Contributing

Contributions are welcome! If you'd like to improve this project, feel free to:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request detailing your changes.

Please ensure your code adheres to the existing style and includes appropriate documentation.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](https://github.com/Poyamohamadi/Round_Robin/blob/main/LICENSE.md) file for details.

---

## Acknowledgments

- **Kivy Framework**: Thanks to the Kivy team for providing an excellent framework for building cross-platform applications.
- **Python Community**: Special thanks to the Python community for their support and resources.

---

For questions or feedback, feel free to reach out:

- **GitHub**: [Poyamohamadi](https://github.com/Poyamohamadi)

---

Thank you for using **Round Robin**! 😊
