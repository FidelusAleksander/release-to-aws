# Release Management Demo with AWS ECR

## Overview

This repository demonstrates how to automate Python application Docker image builds and deployment to Amazon ECR whenever a GitHub Release is published. It uses:

- [Release Drafter](https://github.com/release-drafter/release-drafter) to automate the creation of release notes
- GitHub Actions to build and push Docker images to Amazon ECR when a release is published

