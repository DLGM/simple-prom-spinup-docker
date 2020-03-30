# Prometheus simple deployment tool

This python3 tool is used to spin up a prometheus environment
containing Prometheus container with job scraping its own metrics,
Another container with Node Exporter being scraped by Prometheus and Grafana container with predefined datasource and dashboard
## Requirements

* Python 3.x
* Docker 19.x.x


## Usage
All parameters are required in order the tool to work:
* Prometheus_ver as: 2.17.0 or v2.17.0 
* Prometheus_Storage_retention_hours as: 10 or 15 (in hours) 
* Node_Exporter_version as 0.18.1 or v0.18.1
* Grafana_version as 6.7.1 or v6.7.1

command structure:
```bash
python spin.py Prometheus_ver Prometheus_Storage_retention_hours \
Node_Exporter_version Grafana_version
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)