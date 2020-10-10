# Fluentd Parsing Configuration

## Fluentd Json Parser
1. Running script generator
```bash
python3 json-generator.py > /var/log/json/python-json.log &
tail -f /var/log/json/python-json.log
```
2. Create file config for parse json log
```bash
vi /etc/td-agent/config.d/json-parsing.conf
```
3. Restart service
```bash
systemctl restart td-agent
systemctl status td-agent
```
4. Parsing result
```bash
tail -f /var/log/td-agent/td-agent.log
```

## Fluentd XML Parser
Fluentd XML Parser using fluentd plugins fluent-plugin-xml-parser and fluent-plugin-xml-simple-filter.
