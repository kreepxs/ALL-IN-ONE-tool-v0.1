import os

tools_to_download = ['nmap', 'sqlinjection', 'nano', 'python']

def download_tools(tools):
    for tool in tools:
        os.system('sudo apt-get install -y {}'.format(tool))

def show_interface():
    print('\033[1;31mALL IN ONE by kreepxs.com\033[0m')

download_tools(tools_to_download)
show_interface()
