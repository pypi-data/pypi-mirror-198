import sys
import argparse

from template_res import template

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
subparsers = parser.add_subparsers()
parser_widget = subparsers.add_parser("list", help="资源列表")

def listTemplate():
    template.listTemplate()
    
module_func = {
    "list": listTemplate
}

def main():
    if len(sys.argv) < 2:
        return

    module = sys.argv[1]
    if module in module_func:
        module_func[module]()
    else:
        print("Unknown command:", module)
        sys.exit(0)
        
if __name__ == '__main__':
        main()
