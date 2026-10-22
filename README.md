# Calour
A  home energy optimizer for heating and electricity \n
Note: Summary written by Claude

Calour is a Python-based project designed to help users understand household energy consumption, estimate energy costs, and explore how home heating configurations affect temperature distribution and energy efficiency.

The project combines energy data analysis with simplified thermal simulation to investigate how factors such as insulation, radiator placement, and outdoor temperature influence a home's heating performance.

## Project Goals

- **Energy Cost Calculator:** Estimate electricity and gas costs using energy consumption, unit rates, standing charges, and billing periods.
- **Energy Detective:** Import household energy data, visualise consumption patterns, compare usage over time, and identify unusual changes.
- **Floor Plan & Thermal Lab:** Import and calibrate a household floor plan, then mark room boundaries, windows, doors, and radiator positions.
- **Thermal Simulation:** Model approximate two-dimensional heat distribution across a room under different heating and environmental conditions.
- **Scenario Comparison:** Compare heating configurations using metrics such as average room temperature, temperature uniformity, estimated warm-up time, and energy use.

## Planned Technology Stack

- Python
- NumPy and pandas for numerical calculations and data analysis
- Matplotlib for charts and thermal visualisations
- Streamlit for the interactive web application
- pytest for testing
- Git and GitHub for version control and project documentation

## Development Approach

Calour is being developed incrementally, with each stage producing a working component before it is integrated into the wider application. The initial focus is on reliable cost calculations and energy data analysis, followed by floor-plan editing, thermal modelling, and scenario comparison.

The project prioritises reusable functions, input validation, testing, clear documentation, and transparent assumptions.

## Limitations

The thermal model is intended for educational exploration and relative comparisons, not as a replacement for professional building-energy analysis. Its simplified two-dimensional approach cannot fully represent real-world airflow, three-dimensional heat transfer, or all the complexities of building construction and heating systems.

## Project Status

**In development.** Features are being implemented and tested progressively. Planned functionality may not yet be available in the current version.

Completed: Energy Calculator
