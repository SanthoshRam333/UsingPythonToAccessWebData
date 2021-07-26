#Parsing an XML which has one tree
import xml.etree.ElementTree as ET

data = '''
<person> #start tag
    <name>Chuck</name>
    <phone type= 'intl'> #type= 'intl' - attribute
    +12833728374 #text content
    </phone> #end tag
    <email hide='yes'/> #self closing tag
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

#Parsing an XML which has a list of trees
import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for tags in lst:
    print('Name', tags.find('name').text)
    print('Id', tags.find('id').text)
    print('Attribute', tags.get("x"))
