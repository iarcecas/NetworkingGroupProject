#Lab 5: Threads

#Name: Andres Palacios
#Student ID: 301253910

#Name: Ignacio Arce
#Student ID: 301264338

#Name: Sebastian Tipan
#Student ID: 301264991

#Name: Susmita Roy
#Student ID: 301207557

#Course: COMP216-008
#Date: Feb 15, 2024

import requests
import argparse
import time
import threading
import os
#os library was imported in order to create and remove the Images folder

directory = "Images"
urls = [
    'https://th.bing.com/th/id/OIP.z-dkECmUFma29zYrb27JkwAAAA?w=264&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.MhwSzfXnBG1MpuuA6IFi-AAAAA?w=218&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.m8b7Y9-81Q4UMCBMaFkw2QAAAA?w=198&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.XN9D7tH47WNJ8h214YgqTwAAAA?w=220&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.cFvfW8dARmuVtR3zOxfTSAHaE9?w=274&h=183&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.wcEy7Ow-TaAohBCz6USqCAAAAA?w=265&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.9FWt0sWpi4UOee5o3WdI-QHaFj?w=224&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.JYXSCIpGskpiOxYTw1vuwgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.QjWOHkojgYSz1LhaypSB-gAAAA?w=190&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.Wlfm_lF4VWlYLiPNfbmbDwHaHa?w=181&h=181&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.ZquJ_NwCCyWfvpAEeU-vngAAAA?w=142&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.C6q29lesR7-Ork5YKuI6LwAAAA?w=257&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.A7o1Bm-XNr9A_4pLPCCujgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.oSjt2rY3YUScDY7pw3b1WAHaFj?w=236&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.AroTG9KnmisPIhICyGjoDAHaFj?w=223&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.zSyHBN9_rn_O9XBkdPx-agAAAA?w=189&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.pGTxkbwreLj7l2ORZrtA8gAAAA?w=147&h=184&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.5SaLUh616MU7KDIP2_0VCwAAAA?w=204&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.S-lrZd2TFhSEpI3VRQyKqQAAAA?w=173&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.sDmZWxXBrF329vZvDu2HrAAAAA?w=266&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.5umgRLykyWn-v_5HmOS0NAHaE7?w=243&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.MPayRq2bYdhfVUj5O9BCnwAAAA?w=125&h=184&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.OeLv1q1dEfGkl1bRHfM5awHaFj?w=240&h=180&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.MksSZEmu5Cgly2HNvRp4NQAAAA?w=180&h=163&c=7&r=0&o=5&pid=1.7',
    'https://th.bing.com/th/id/OIP.HCpPn-IRV8SVidBlRoBRUwHaE7?w=287&h=191&c=7&r=0&o=5&pid=1.7'
]

#Check if the folder exist and delete files if the folder is not empty
def validateFolder(directory):
    if(os.path.exists(directory)):       
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if(os.path.isfile(item_path)):  #Delete only if it's file.
                os.remove(item_path)        #Delete files inside the folder   
    else: 
        os.mkdir(directory)

def download_file(url, pathname):
    """
    Download a file from a given URL and save it with the specified filepath.

    Arguments:
        url: The URL of the file to download.
        pathname: The path to save the file.
    """
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(pathname, 'wb') as f:
            f.write(response.content)
        print("File downloaded successfully:", pathname)
    else:
        print("File not available:", url)  

#Download the set of images sequentially and measure the elapsed time.
def download_images_sequentially():
    start_time = time.perf_counter()

    if not os.path.exists(directory):
        os.mkdir(directory)

    for i, url in enumerate(urls, start=1):
        filename = f"{i}.jpg"
        filepath = os.path.join(directory, filename)
        download_file(url, filepath)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time (sequential): {elapsed_time:.2f} seconds")

#Download the set of images using threads and measure the elapsed time.
def download_images_with_threads():

    start_time = time.perf_counter()

    if not os.path.exists(directory):
        os.mkdir(directory)

    threads = []
    for i, url in enumerate(urls, start=1):
        filename = f"{i}.jpg"
        filepath = os.path.join(directory, filename)
        thread = threading.Thread(target=download_file, args=(url, filepath))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time (threads): {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-mode','-m',                                          #name of the mandatory argument
        required=True,                      
        choices='serial threaded'.split(),
        help='mode to run this program (serial/threaded)'      #more information to the user
    )
    parser.add_argument(
        '-folder',                                             #optional argument
        default="Images",                                      
        type=str,
        help='folder where you want to download the images'
    )
    args = parser.parse_args()
    if args.mode == 'serial':
        validateFolder(args.folder)
        directory = args.folder     #As we are not passing arguments we use the global directory variable
        download_images_sequentially()
    elif args.mode == 'threaded':
        validateFolder(args.folder)
        directory = args.folder
        download_images_with_threads()

