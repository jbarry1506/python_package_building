from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["things/*"]

setup(name = "mypackage",
    version = "100",
    description = "it's a package, y'all",
    author = "this guy right here",
    author_email = "email@ididathing.com",
    url = "notaurlatall",
    
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    
    packages = ['mypackage'],
    
    #'package' package must contain files (see list above)
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'package' : files },
    #'runner' is in the root.
    scripts = ["runner"],
    long_description = """Really long text here.""" 
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
) 
