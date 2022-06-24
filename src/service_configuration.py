from constants import DEFAULT_POLLING_FREQUENCY, STATS_PACKET_LIMIT
from models import Configuration


class _ServiceInstanceConfiguration(Configuration):
    def __init__(self, *args, **kwargs):
        config = {
            "service_name": kwargs.get('service_name'),
            "server_url": kwargs.get('server_url'),
            "poll_method": kwargs.get('poll_method'),
            "poll_endpoint": kwargs.get('poll_endpoint') if kwargs.get('poll_endpoint') else None,
            "poll_retries": kwargs.get('poll_retries') if kwargs.get('poll_retries') else 0,
            "poll_delay": kwargs.get('poll_delay') if kwargs.get('poll_delay') else None,
            "poll_freq": kwargs.get('poll_frequency') if kwargs.get('poll_frequency') else DEFAULT_POLLING_FREQUENCY,
            "packet_limit": kwargs.get('packet_limit') if kwargs.get('packet_limit') else STATS_PACKET_LIMIT,
            "apis": kwargs.get('apis')
        }
        super().__init__(**config)

class _ServiceConfiguration:
    
    def __init__(self):
        self.service_configuration = []

    def add(self, config: _ServiceInstanceConfiguration):
        self.service_configuration.append(config)
        

