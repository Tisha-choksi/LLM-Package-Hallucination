import difflib
import pkg_resources

# List of popular packages (you can fetch this from PyPI or any other source)
known_packages = ['pandas', 'numpy', 'requests', 'matplotlib', 'flask', 'django']  # example

def check_typosquatting(import_name):
    # Check if the import is a known package or if it's very similar to a known package
    close_matches = difflib.get_close_matches(import_name, known_packages, n=1, cutoff=0.8)

    if close_matches:
        suggested_package = close_matches[0]
        if import_name != suggested_package:
            print(f"Warning: Potential typosquatting detected. Did you mean '{suggested_package}' instead of '{import_name}'?")
    else:
        print(f"Warning: '{import_name}' is not a known package. Please verify if the import is correct.")

# Example imports to test
test_imports = ['pandos', 'numy', 'requsts', 'flask']

for imp in test_imports:
    check_typosquatting(imp)
