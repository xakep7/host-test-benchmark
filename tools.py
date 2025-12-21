#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time,json,sys
import shlex
import datetime
import urllib.request
import urllib.parse
import subprocess
from importlib import reload

reload(sys)

def is_json(json_arr):
	try:
		json.loads(json_arr)
	except ValueError as e:
		return False
	return True
	
def GetGeoioInfo(para):
	header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 host-test.ru benchmark"}
	request = urllib.request.Request("https://ip2whois.ru/api/whoisinfo/ip/my", header)
	response = urllib.request.urlopen(request, data=bytes(json.dumps(header), encoding="utf-8"))
	info = response.read()
	if(is_json(info)):
		jsons = json.loads(info)
		print(jsons[para])
	else:
		print("data error")
		print(info)
	
def Upload_test_data(para):
	try:
		with open(para, 'r') as file:
			content = file.read()
		post_data = urllib.parse.urlencode({"clbin": content}).encode("utf-8")
		header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 host-test.ru benchmark"}
		request = urllib.request.Request("https://host-test.ru/api/test_upload",data=post_data,method="POST", header)
		response = urllib.request.urlopen(request, data=bytes(json.dumps(header), encoding="utf-8"))
		info = response.read()
		if(is_json(info)):
			jsons = json.loads(info)
			print(jsons['link'])
		else:
			print("data error")
			print(info)
	except FileNotFoundError:
		print(f"Error: The file '{file_path}' was not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

def GetDiskInfo(para):
	temp = ExecShell("df -h -P|grep '/'|grep -v tmpfs")[0];
	temp1 = temp.split('\n');
	diskInfo = [];
	n = 0
	cuts = ['/mnt/cdrom','/boot','/boot/efi','/dev','/dev/shm','/run/lock','/run','/run/shm','/run/user'];
	for tmp in temp1:
		n += 1
		disk = tmp.split();
		if len(disk) < 5: continue;
		if disk[1].find('M') != -1: continue;
		if disk[1].find('K') != -1: continue;
		if len(disk[5].split('/')) > 4: continue;
		if disk[5] in cuts: continue;
		arr = {}
		diskInfo = [disk[1],disk[2],disk[3],disk[4],disk[5]];
	print(diskInfo[int(para)]);

def ExecShell(cmdstring, cwd=None, timeout=None, shell=True):
	if shell:
		cmdstring_list = cmdstring
	else:
		cmdstring_list = shlex.split(cmdstring)
	if timeout:
		end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
	sub = subprocess.Popen(cmdstring_list, cwd=cwd, stdin=subprocess.PIPE,shell=shell,bufsize=4096,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	while sub.poll() is None:
		time.sleep(0.1)
		if timeout:
			if end_time <= datetime.datetime.now():
				raise Exception("Timeout:%s"%cmdstring)
	return sub.communicate()

if __name__ == "__main__":
	type = sys.argv[1];
	if type == 'disk':
		GetDiskInfo(sys.argv[2])
	elif type == 'geoip':
		GetGeoioInfo(sys.argv[2])
	elif type == 'upload':
		Upload_test_data(sys.argv[2])
	else:
		print('ERROR: Parameter error')
