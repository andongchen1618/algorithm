def print_tree(tree, level=0):
    # Iterate over keys in tree
    for key in sorted(tree):
        # Print key with indentation
        print('  ' * level + '-- ' + key)
        # Recursively print subdirectories
        if isinstance(tree[key], dict):
            print_tree(tree[key], level + 1)

def directory_structure(files):
    tree = {}
    for file in files:
        path_segments = file.split('/')
        node = tree
        for segment in path_segments:
            # Ignore if segment is empty (occurs for paths starting with '/')
            if segment:
                node = node.setdefault(segment, {})
    print_tree(tree)

# Testing the function
files = [
  "/app/components/header",
  "/app/services",
  "/app/tests/components/header",
  "/images/image.png",
  "/tsconfig.json",
  "/index.html",
]
directory_structure(files)
