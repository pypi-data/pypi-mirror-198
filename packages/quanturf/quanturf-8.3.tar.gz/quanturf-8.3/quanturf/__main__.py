import os
import typer
import requests
import maskpass
import json
import site
import os
import shutil
from . import quanturf_logo

app=typer.Typer()

def get_js_file(site_package_dir,logo_code):
    os.chdir(site_package_dir)
    os.chdir("../")
    os.chdir("../")
    env_dir=os.getcwd()
    src_file_path=os.path.join(env_dir,"share","jupyter","labextensions","jupyterlab_templates","static","568.d53c3cb2b0017bfabe20.js")
    src_file_path = src_file_path.replace(os.sep, '/')
    src_file=open(src_file_path,"w")
    src_file.write(logo_code)
    src_file.close()
    return

# site_package_dir=site.getsitepackages()

# if len(site_package_dir) == 1:
#     logo_code=quanturf_logo.logo_js()
#     site_package_dir=' '.join(site_package_dir)
#     get_js_file(site_package_dir,logo_code)

# if len(site_package_dir) >= 2:
#     logo_code=quanturf_logo.logo_js()
#     get_js_file(site_package_dir[1],logo_code)

@app.command()
def deploy():   
    AUTH_URL="https://quanturf.com/api/auth/"
    URL="https://quanturf.com/api/files/"

    path=os.getcwd()
    dir_list = os.listdir(path)
    files=[]
    for file in dir_list:
        if file != '__pycache__':
            files.append(('file',open(path+'/'+str(file),"rb")))
    
    print("Enter your Quanturf username and password...")
    username=input("Enter Username: ")
    password=maskpass.askpass(mask="*")
    user_auth={'username':username,'password':password}
    user_auth=json.dumps(user_auth)
    headers = {'Content-type': 'application/json'}
    auth_request=requests.post(url=AUTH_URL,data=user_auth,headers=headers)
    auth_response=auth_request.json()
    print(auth_response['message'])

    if auth_response['message'] == 'Authentication Successful!':
        file_upload_request=requests.post(url=URL,files=files)
        file_upload_response=file_upload_request.json()
        print(file_upload_response['message'])

@app.command()
def jupyterlab():
    os.system("pip install jupyterlab_templates")
    os.system("jupyter labextension install jupyterlab_templates")
    os.system("jupyter serverextension enable --py jupyterlab_templates")

    
    print("Running Jupyter platform!")
    out = site.getsitepackages()

    if len(out) == 1:
        str_out = out
        out1 = ' '.join(str_out)

        logo_code=quanturf_logo.logo_js()
        get_js_file(out1,logo_code)

        filename = os.path.join(out1, "quanturf", "jupyter_notebook_config.py")
        filename2 = filename.replace(os.sep, '/')
        filename3 = os.path.join(
            out1, "jupyterlab_templates/templates/jupyterlab_templates/")
        src_file = os.path.join(out1, "quanturf", "quanturf.ipynb")
        src_path = src_file
        dst_path = filename3.replace(os.sep, '/')
        try:
            os.remove(dst_path+"Sample.ipynb")
        except:
            pass
        shutil.copy(src_path, dst_path)
        os.system("jupyter lab --config=" + filename2)

    if len(out) >= 2:
        str_out = out[1]

        logo_code=quanturf_logo.logo_js()
        get_js_file(str_out,logo_code)

        filename = os.path.join(str_out, "quanturf",
                                "jupyter_notebook_config.py")
        filename2 = filename.replace(os.sep, '/')
        filename3 = os.path.join(
            str_out, "jupyterlab_templates/templates/jupyterlab_templates/")
        filename3 = os.path.join(
            str_out, "jupyterlab_templates/templates/jupyterlab_templates/")
        src_file = os.path.join(str_out, "quanturf", "quanturf.ipynb")
        src_path = src_file
        dst_path = filename3.replace(os.sep, '/')
        try:
            os.remove(dst_path+"Sample.ipynb")
        except:
            pass
        shutil.copy(src_path, dst_path)
        os.system("jupyter lab --config=" + filename2)
    

if __name__ == "__main__":
    app()