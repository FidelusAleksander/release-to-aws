# Release to AWS

>[!NOTE]
> This project is a demonstration repository for educational purposes on how to use GitHub Actions to automate the release process to AWS ECR (Elastic Container Registry) with an example FastAPI application.


## Overview

This project contains:

- **FastAPI Application**: A simple Python web API built with FastAPI that provides basic endpoints (`/` and `/status`)
- **Containerization**: Complete Docker setup with optimized multi-stage builds using `uv` for fast Python package management
- **Automated Release Management**: Uses [Release Drafter](https://github.com/release-drafter/release-drafter) to automatically generate release notes from pull requests
- **CI/CD Pipeline**: GitHub Actions workflows that automatically build and push Docker images to Amazon ECR when releases are published


## GitHub Actions Workflows

The repository uses these key automated workflows:

- **Release** (`release.yml`): Automatically builds and pushes Docker images to ECR when a GitHub release is published
- **PR Checks** (`pr-checks.yml`): Runs tests and code quality checks on pull requests
- **Release Drafter** (`release-drafter.yml`): Generates release notes from PR labels and descriptions
- **Build ECR Artifacts** (`build-ecr-artifacts.yml`): Reusable workflow for building and pushing Docker images to Amazon ECR, used by other workflows


