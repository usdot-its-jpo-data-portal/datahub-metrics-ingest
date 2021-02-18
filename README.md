# Summary
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=usdot-its-jpo-data-portal_datahub-metrics-ingest&metric=alert_status)](https://sonarcloud.io/dashboard?id=usdot-its-jpo-data-portal_datahub-metrics-ingest)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=usdot-its-jpo-data-portal_datahub-metrics-ingest&metric=coverage)](https://sonarcloud.io/dashboard?id=usdot-its-jpo-data-portal_datahub-metrics-ingest)

This repository contains a Python package for collecting usage metrics relating to ITS DataHub's assets on data.transportation.gov and National Transportation Library. The metrics are ingested into ITS DataHub's Elasticsearch database for display on ITS DataHub.

# README Outline:
* Project Description
* Prerequisites
* Usage
	* Installing
	* Testing
	* Execution
* Version History and Retention
* License
* Contributions
* Contact Information
* Acknowledgements

# Project Description

This repository contains a Python package for collecting usage metrics relating to ITS DataHub's assets on data.transportation.gov and National Transportation Library. The metrics are ingested into ITS DataHub's Elasticsearch database for display on ITS DataHub.

# Prerequisites

Requires:
- Python 3.6+
- Elasticsearch (optional if you choose to write metrics to CSV)

# Usage

## Installing
 
```
git clone https://github.com/usdot-its-jpo-data-portal/datahub-metrics-ingest.git
cd datahub-metrics-ingest
pip install .
```

## Testing

```
sh unittest.sh
```

## Execution
Import into your python code.

```
import datahub_metrics_ingest
```
Example of the package usage can be found at [lambda-ingest-dtg-metric](https://github.com/usdot-its-jpo-data-portal/lambda-ingest-dtg-metric) and [lambda-ingest-ntl-metric](https://github.com/usdot-its-jpo-data-portal/lambda-ingest-ntl-metric).

# Version History and Retention

**Status:** This project is in the prototype phase.

**Release Frequency:** This project is currently in development and updated weekly.

**Release History: See [CHANGELOG.md](CHANGELOG.md)**

**Retention:** This project will remain publicly accessible for a minimum of five years (until at least 06/15/2025).

# License

This project is licensed under the Creative Commons 1.0 Universal (CC0 1.0) License - see the [LICENSE](https://github.com/usdot-jpo-codehub/codehub-readme-template/blob/master/LICENSE) for more details. 

# Contributions
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our Code of Conduct, the process for submitting pull requests to us, and how contributions will be released.

# Contact Information

Contact Name: ITS JPO
Contact Information: data.itsjpo@dot.gov

# Acknowledgements

## Citing this code

When you copy or adapt from this code, please include the original URL you copied the source code from and date of retrieval as a comment in your code. Additional information on how to cite can be found in the [ITS CodeHub FAQ](https://its.dot.gov/code/#/faqs).

## Contributors
Shout out to [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) for their README template.
