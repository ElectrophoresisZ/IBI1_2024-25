import xml.dom.minidom
import xml.sax
import os
from datetime import datetime

# -------------------------- DOM --------------------------
def DOM_process(xml_file):
    # Time start
    start_time = datetime.now()
    
    # Initialize statistics dictionary
    namespace_stats = {
        'molecular_function': {'max_term': '', 'count': 0},
        'biological_process': {'max_term': '', 'count': 0},
        'cellular_component': {'max_term': '', 'count': 0}
    }
    
    try:
        # Parse the XML file with DOM
        with open(xml_file, 'r') as f:
            dom_tree = xml.dom.minidom.parse(f)
        
        # Directly access the root element
        terms = dom_tree.getElementsByTagName("term")
        
        # Optimized term processing
        for term in terms:
            # Get namespace
            namespace_nodes = term.getElementsByTagName("namespace")
            if not namespace_nodes or not namespace_nodes[0].firstChild:
                continue
            namespace = namespace_nodes[0].firstChild.data.strip()
            if namespace not in namespace_stats:
                continue
            
            # Get ID
            id_nodes = term.getElementsByTagName("id")
            if not id_nodes or not id_nodes[0].firstChild:
                continue
            term_id = id_nodes[0].firstChild.data.strip()
            
            # Count is_a relationships
            is_a_count = len(term.getElementsByTagName("is_a"))
            
            # Update statistics
            if is_a_count > namespace_stats[namespace]['count']:
                namespace_stats[namespace]['max_term'] = term_id
                namespace_stats[namespace]['count'] = is_a_count
    
    except Exception as e:
        print(f"Error processing file with DOM: {e}")
        return {}, 0
    
    # Time end
    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    return namespace_stats, time_taken

# -------------------------- SAX --------------------------
class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.current_tag = ""
        self.current_namespace = ""
        self.current_id = ""
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
            self.current_id = ''
            self.is_a_count = 0

    def characters(self, content):
        if self.current_tag == "namespace":
            self.current_namespace += content.strip()
        elif self.current_tag == "id":
            self.current_id += content.strip()

    def endElement(self, tag):
        if tag == "is_a":
            self.is_a_count += 1
        elif tag == "term" and self.current_namespace in self.namespace_stats:
            if self.is_a_count > self.namespace_stats[self.current_namespace]['count']:
                self.namespace_stats[self.current_namespace]['max_term'] = self.current_id
                self.namespace_stats[self.current_namespace]['count'] = self.is_a_count
        self.current_tag = ""

def SAX_process(xml_file):
    # Time start
    start_time = datetime.now()
    
    try:
        # Parse the XML file with SAX
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        handler = MyContentHandler()
        parser.setContentHandler(handler)
        
        with open(xml_file, 'r') as f:
            parser.parse(f)
    
    except Exception as e:
        print(f"Error processing file with SAX: {e}")
        return {}, 0
    
    # Time end
    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    return handler.namespace_stats, time_taken

# -------------------------- Main --------------------------
def main():
    # Use os.path for file path handling
    current_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
    xml_file = os.path.join(current_dir, 'go_obo.xml')
    
    # Check if file exists
    if not os.path.isfile(xml_file):
        print(f"Error: XML file '{xml_file}' not found.")
        return
    
    # Process the file with both methods
    namespace_stats1, time_taken1 = DOM_process(xml_file)
    namespace_stats2, time_taken2 = SAX_process(xml_file)
    
    # Print results
    print("DOM processing time:", time_taken1, "seconds")
    print("SAX processing time:", time_taken2, "seconds")
    
    # Determine the faster method
    faster_method = "SAX" if time_taken1 > time_taken2 else "DOM"
    
    # Print namespace statistics
    for namespace in ['molecular_function', 'biological_process', 'cellular_component']:
        stats1 = namespace_stats1.get(namespace, {})
        stats2 = namespace_stats2.get(namespace, {})
        
        # Check if both methods produced results
        if stats1.get('max_term') and stats2.get('max_term'):
            print(f'{namespace}:')
            print(f'  DOM: ID={stats1["max_term"]}, Count={stats1["count"]}')
            print(f'  SAX: ID={stats2["max_term"]}, Count={stats2["count"]}')
            print(f'  Match: {stats1["max_term"] == stats2["max_term"]}')
        else:
            print(f'{namespace}: Incomplete data')
    
    print(f"\nFaster method: {faster_method}")

# ------------------------ End of code ----------------------
if __name__ == '__main__':
    main() 