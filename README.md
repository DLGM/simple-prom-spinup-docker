# Prometheus simple deployment tool

This python3 tool is used to spin up a prometheus environment
containing Prometheus container with job scraping its own metrics,
Another container with Node Exporter being scraped by Prometheus and Grafana container with predefined datasource and dashboard
## Requirements

* Python 3.x
* Docker 19.x.x


## Usage

```python
python spin.py Prometheus_ver Prometheus_Storage_retention_hours \
Node_Exporter_version Grafana_version
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)