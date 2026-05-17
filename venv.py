# virtual environments in python help avoid package version conflicts, there is one global environment

# We generally use a separate environment to isolate the dependencies. 

# eg we are using pandas 2.2.2 and we want to use pandas 1.5.3
# we can only have one version of the particular library installed

# By using virtual environments we can create copies of the global python interpreter and install dependencies separately


# Step 1 --> pip install virtualenv
# Step 2 --> use python -m virtualenv env
# Step 3 --> an isolated env folder will be created


#to open the venv from the termina we use first enter the directory and then give the activation file path (use .bat for cmd)

# .\env\Scripts\activate.bat


# To find which modules are installed in a particular env we use the pip freeze command

#(env) PS D:\Ahmed\programming\python> pip freeze              
# numpy==2.4.5
# packaging==26.2
# pandas==3.0.3
# python-dateutil==2.9.0.post0
# setuptools==82.0.1
# six==1.17.0
# tzdata==2026.2
# wheel==0.47.0


# always write whatever you use in the project, always write it in the requirements.txt and use this command for that pip freeze > requirements.txt

# and to install all the packages we just have to write pip install -r .\requirements.txt