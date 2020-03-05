import xml.dom.minidom


def main():
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("C:\Chandra Sekhar\Python\Python Project\Scripts\My XML.xml");

    # print out the document node and the name of the first child tag
    print (doc.nodeName)
    print (doc.firstChild.tagName)
    print(doc.childNodes.count('author'))
    # get a list of XML tags from the document and print each one
    expertise = doc.getElementsByTagName("description")
    print ("%d expertise:" % expertise.length)
    for skill in expertise:
        print (skill.getAttribute("price"))