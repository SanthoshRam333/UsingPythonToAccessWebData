#XML- eXtensible Markup Language
#Primary Function of XML is to help informatiion systems share structured Data
<person> #start tag
    <name>Chuck</name>
    <phone type= 'intl'> #type= 'intl' - attribute
    +12833728374 #text content
    </phone> #end tag
    <email hide='yes'/> #self closing tag
</person>

#XML Terminology
##Tags - indicate the beginning and ending of elements
##Attributes- keyword/value pairs on the opening tag of XML
##Serialize/De-Serialize - convert Data in one program into
#common format that can be stored and/or transmitted between systems
#in a programming language-independent environment.

#XML Schema (decribing a 'contract' as to what is aceptable XML)
#Description of the legal format of an XML document

#Expressed in terms of constraints on the structure and content
#of documents

#Often used to specify a 'contract' between systems - 'My system will only
#accept XML that conforms to this particular Schema'

#If a particular piece of XML meets the specification of the Schema - it is
#said to 'validate'

#XML Schema contract
<xs.complexType name="person">
    <xs.sequence>
        <xs.element name="lastname" type="xs.string"/>
        <xs.element name="age" type="xs.integer"/>
        <xs.element name="dateborn" type="xs.date"/>
    </xs.sequence>
</xs.complexType>

#XSD XML Schema (W3C spec)

#We will focus on the World Wide Web Consortium (W3C) version
#It is often called 'W3C Schema', more commonly it is called XSD because
#the file name ends in .xsd

#XSD constraints
<xs.element name="lastname" type="xs.string"
    minOccurs="1" maxOccurs="1"/>
#This means there is one, exactly one.

#XSD Data Types
<xs.element name="lastname" type="xs.string"/>
<xs.element name="age" type="xs.integer"/>
<xs.element name="dateborn" type="xs.date"/>
<xs.element name="startdate" type="xs.dateTime"/> #2002-04-30T09:30:10Z
<xs.element name="weeks" type="xs.integer"/>
