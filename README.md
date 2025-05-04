# release-drafter-repo

## Release Drafter Automation

This repository uses [release-drafter](https://github.com/release-drafter/release-drafter) to automate the process of drafting release notes.

### How to Use Release Drafter

1. Ensure that the `.github/release-drafter.yml` configuration file is present in the repository.
2. The release-drafter workflow is triggered on every push to the `main` branch.
3. When changes are pushed to the `main` branch, release-drafter will automatically update the release draft with the changes.
4. You can view and edit the release draft in the "Releases" section of the repository on GitHub.
5. Publish when ready!
