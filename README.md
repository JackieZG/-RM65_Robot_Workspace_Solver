# RM65 Robot Workspace Solver

This repository contains the implementation of a workspace solver for the RM65 series robot using the Monte Carlo method and reinforcement learning.

## Overview

The RM65 series robot is a 6-degree-of-freedom collaborative robot developed by Realman Intelligent Technology (Beijing) Co., Ltd. This project aims to provide tools for solving the workspace of the RM65 robot, leveraging the Monte Carlo method for sampling and reinforcement learning for optimization.

## Features

- Monte Carlo-based workspace solver
- Reinforcement learning environment for the RM65 robot
- Extensive testing and documentation
- Support for RM65-B, RM65-ZF, and RM65-6F models

## Getting Started

### Prerequisites

- Python 3.8+
- Virtual environment tools (e.g., venv, conda)
- ROS Noetic
- Gazebo

### Installation

Please refer to the [INSTALL.md](docs/INSTALL.md) for detailed installation instructions.

### Usage

To run the Monte Carlo workspace solver:
```bash
python src/main.py --mode monte_carlo
