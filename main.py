import argparse
from api_wrapper_generator.core.spec_parser import parse_openapi_spec
from api_wrapper_generator.core.code_generator import generate_api_wrapper

def main():
    parser = argparse.ArgumentParser(description="Generate API wrappers from OpenAPI specs.")
    parser.add_argument("spec_file", help="Path to the OpenAPI spec file.")
    parser.add_argument("-o", "--output", help="Output file name (default: wrapper.py)", default="wrapper.py")
    args = parser.parse_args()

    endpoints, api_name = parse_openapi_spec(args.spec_file)

    if endpoints:
        code = generate_api_wrapper(api_name, endpoints)
        with open(args.output, "w") as f:
            f.write(code)
        print(f"Wrapper generated to {args.output}")

if __name__ == "__main__":
    main()