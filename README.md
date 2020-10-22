# Fluentd Parsing Configuration

## Fluentd Json Parser
1. Running script generator
```bash
python3 json-generator.py >> /var/log/json/python-json.log &
tail -f /var/log/json/python-json.log
```
2. Copy file config for parse json log
```bash
cp json-parsing.conf /etc/td-agent/config.d/json-parsing.conf
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



1. Create generator XML log
```bash
sudo apt -y install python3-lxml
```

2. Create generator XML log 
```bash
vim xml-generator.py
```
```python
from lxml import etree

# create XML 
root = etree.Element('root')
root.append(etree.Element('child'))
# another child with text
child = etree.Element('child')
child.text = 'some text'
root.append(child)

# pretty string
s = etree.tostring(root, pretty_print=True)
print(s)
```
  
Example Output  
```
<root>
  <child/>
  <child>some text</child>
</root>
```

3. Install plugin for parsing XML log
```bash
td-agent-gem install  fluent-plugin-xml-parser
td-agent-gem install  fluent-plugin-xml-simple-filter
```

4. Copy file config for parse xml log
```bash
cp xml-parsing.conf /etc/td-agent/config.d/xml-parsing.conf
```
5. Restart service
```bash
systemctl restart td-agent
systemctl status td-agent
```
6. Parsing result
```bash
tail -f /var/log/td-agent/td-agent.log
