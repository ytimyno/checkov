checkov -d images/ --external-checks-dir ../../extra_checks --framework dockerfile -c CKV_DOCKER_LABEL_CHECK

If I try, from the directory I am located in when running checkov, to open a file called containerfile_labels.json which is a dictionary similar to this, but if none exists, use the default 

{
    "maintainer": {
        "allowed_values": ".*",
        "version": "1.0",
        "description": "A sample label - Any value accepted"
    }, 
    "maintainer_specific":{
        "allowed_values": "^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$",
        "version": "1.0",
        "description": "A sample label - Specific regex"
    }
}

And double checked the file is obtained from the directory the checkov command is ran! So that's easy enough.