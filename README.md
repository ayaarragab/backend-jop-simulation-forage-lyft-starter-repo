# Backend Job Simulation - Forage Lyft Starter Repo

This repository is a backend job simulation project for Lyft, forked from the [Forage Lyft Starter Repo](https://github.com/vagabond-systems/forage-lyft-starter-repo). It includes implementations for various car components and their respective tests.

## Project Structure

backend-jop-simulation-forage-lyft-starter-repo/
│
├── battery/
│ ├── init.py
│ ├── battery.py
│ ├── nubbin.py
│ └── spindler.py
│
├── carAndFactory/
│ ├── car.py
│ ├── carFactory.py
│ └── carParts.py
│
├── engine/
│ ├── init.py
│ ├── capulet_engine.py
│ ├── sternman_engine.py
│ └── willoughby_engine.py
│
├── tires/
│ ├── init.py
│ ├── carrigan_tires.py
│ └── octoprime_tires.py
│
├── test/
│ ├── test_battery.py
│ ├── test_engine.py
│ └── test_tires.py
├── .gitignore
├── README.md
└── servicable.py

## Folders and Files Description

- **battery/**: Contains classes and methods related to different types of batteries.
  - `__init__.py`: Initializer for the battery module.
  - `battery.py`: Main battery class.
  - `nubbin.py`: Nubbin battery class implementation.
  - `spindler.py`: Spindler battery class implementation.

- **carAndFactory/**: Contains classes and methods related to car and car factory operations.
  - `car.py`: Car class implementation.
  - `carFactory.py`: Factory class for creating car instances.
  - `carParts.py`: Additional car parts implementations.

- **engine/**: Contains classes and methods related to different types of engines.
  - `__init__.py`: Initializer for the engine module.
  - `capulet_engine.py`: Capulet engine class implementation.
  - `sternman_engine.py`: Sternman engine class implementation.
  - `willoughby_engine.py`: Willoughby engine class implementation.

- **tires/**: Contains classes and methods related to different types of tires.
  - `__init__.py`: Initializer for the tires module.
  - `carrigan_tires.py`: Carrigan tires class implementation.
  - `octoprime_tires.py`: Octoprime tires class implementation.

- **test/**: Contains unit tests for the battery, engine, and tires modules.
  - `test_battery.py`: Unit tests for battery classes.
  - `test_engine.py`: Unit tests for engine classes.
  - `test_tires.py`: Unit tests for tires classes.

- **.gitignore**: Specifies files and directories to be ignored by git.
- **README.md**: Project documentation.
- **servicable.py**: Contains the servicable interface used by various car components.

## Getting Started

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/backend-jop-simulation-forage-lyft-starter-repo.git
   cd backend-jop-simulation-forage-lyft-starter-repo
2. **Run tests**
    ```sh
    Ensure you have Python installed:
    ```
    python -m unittest discover -s test
    ```
