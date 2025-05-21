import xml.dom.minidom
import xml.sax
import os
from datetime import datetime


# -------------------------- DOM --------------------------
def DOM_process(xml_file):

    # Time start
    start_time = datetime.now()
    # Initialize a dictionary to store the namespace statistics
    namespace_stats = {
        'molecular_function': {'max_term': '', 'count': 0},
        'biological_process': {'max_term': '', 'count': 0},
        'cellular_component': {'max_term': '', 'count': 0}
    }
    DOMTree = xml.dom.minidom.parse(xml_file)
    Collection = DOMTree.documentElement
    terms = Collection.getElementsByTagName("term")

    for term in terms:
        # Get the namespace of the term
        namespace = term.getElementsByTagName("namespace")[0].firstChild.data.strip()

        # Get the id of the term
        name = term.getElementsByTagName("name")[0].firstChild.data.strip()

        # Find the maximum number of is_a relationships for each namespace
        is_a_list = term.getElementsByTagName("is_a")
        count = len(is_a_list)
        if count > namespace_stats[namespace]['count']:
            namespace_stats[namespace]['max_term'] = name
            namespace_stats[namespace]['count'] = count

    # Time end
    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    return namespace_stats, time_taken

# -------------------------- SAX --------------------------
class MyContentHandler(xml.sax.ContentHandler):
    
    def __init__(self):
        self.current_tag = ""
        self.current_namespace = ""
        self.current_name = ""
        self.is_a_count = 0
        
        self.namespace_stats = {
            'molecular_function': {'max_term': '', 'count': 0},
            'biological_process': {'max_term': '', 'count': 0},
            'cellular_component': {'max_term': '', 'count': 0}
        }

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == "term":
            self.current_namespace = ''
            self.current_name = ''
            self.is_a_count = 0

    def characters(self, content):
        if self.current_tag == "namespace":
            self.current_namespace += content.strip()
        elif self.current_tag == "name":
            self.current_name += content.strip()

    def endElement(self, tag):
        if tag == "is_a":
            self.is_a_count += 1
        elif tag == "term" and self.current_namespace in self.namespace_stats:
            if self.is_a_count > self.namespace_stats[self.current_namespace]['count']:
                self.namespace_stats[self.current_namespace]['max_term'] = self.current_name
                self.namespace_stats[self.current_namespace]['count'] = self.is_a_count
        self.current_tag = ""
        
def SAX_process(xml_file):
    
    # Time start
    start_time = datetime.now()

    parse = xml.sax.make_parser()
    parse.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = MyContentHandler()
    parse.setContentHandler(handler)
    parse.parse(xml_file)
    
    # Time end
    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    return handler.namespace_stats, time_taken

# -------------------------- Main --------------------------
def main():
    os.chdir("C:/Users/Administrator/Desktop/IBI/IBI/IBI1_2024-25/Practical14")
    xml_file = 'go_obo.xml'
    namespace_stats1, time_taken1 = DOM_process(xml_file)
    namespace_stats2, time_taken2 = SAX_process(xml_file)
    print("DOM processing time:", time_taken1, "seconds")
    print("SAX processing time:", time_taken2, "seconds")
    for namespace, stats in namespace_stats1.items():
        print(f'{namespace}: The name of maximum is_a relationships is {stats["max_term"]} and the count is {stats["count"]}.')

    if time_taken1 > time_taken2:
        print("SAX is faster than DOM")
    else:
        print("DOM is faster than SAX")

# ------------------------ End of code ----------------------
if __name__ == '__main__':
    main()
