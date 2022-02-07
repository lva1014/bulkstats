#!/usr/bin/python

import re
import datetime
import sys
import os
import subprocess
import time
from os import path
from insert import go_insert

node = 'spgw10'

schemas = ( 'card','port','ppp','gtpc','gtpp',
			'ippool','apn','diameter-auth','diameter-acct',
			'ecs','dcca-group','context','egtpc','imsa',
			'pgw','sgw','dpca','dcca','gtpu','vlan-npu',
			'diameter','samog','epdg',
			'radius','radius-group','p2p','vlan-npu','apn-qci-duration','pgw-egtpc-s5s8','pgw-egtpc-s2a','flow-kpi',)

sys_schemas = ('systemSch1','systemSch2','systemSch3',
				'systemSch4','systemSch5','systemSch6',
				'systemSch7','systemSch8','systemSch9',
				'systemSchA','systemSchB','systemSchC',
				'systemSchD','systemSchE','systemSchF',)

snames = ('Card','Card1','Card2','Car3','Port','PDSNSystem','PDSNSystem2',
			'PDSNSystem3','PDSNSystem4','PDSNSystem5','PDSNSystem6',
			'PDSNSystem7','PDSNSystem8','PDSNSystem9','PDSNSystemA',
			'PDSNSystemB','PDSNSystemC','PDSNSystemD','PDSNSystemE',
			'PDSNSystemF','PPP1','PPP2','GTPC1','GTPC2','GTPC3',
			'GTPC4','GTPC5','GTPC6','GTPP','GTPP2','IPPOOL','APN',
			'APN2','APN3','APN4','DIAMETERAUTH1','DIAMETERACCT1',
			'ECS1','ECS2','ECS3','ECS4','ECS5','ECS6','ECS7','ECS8',
			'ECS9','ECSA','ECSB','ECSC','ECSD','ECSE','DCCAGroup1',
			'DCCAGroup2','CONTEXT','CONTEXT2','CONTEXT3','EGTPC1',
			'EGTPC2','EGTPC3','IMSA','IMSA2','PGW1','PGW2','PGW3','PGW4',
			'PGW5','PGW6','PGW7','PGW8','PGW9','SGW1','SGW2','SGW3',
			'SGW4','SGW5','SGW6','SGW7','SGW8','SGW9','SGWA','SGWB',
			'SGWC','SGWD','DPCA1','DCCA1','DCCA2','GTPU1','GTPU2',
			'VLAN_NPU','VLAN_NPU2','VLAN_NPU3','DIAMETER1','SAMOG1',
			'SAMOG2','SAMOG3','SAMOG4','SAMOG5','SAMOG6','SAMOG7',
			'SAMOG8','SAMOG9','SAMOGA','EPDG1','EPDG2','EPDG3','samog',
			'flow_kpi1',
			'pgw_egtpc_s2a1','pgw_egtpc_s2a2','pgw_egtpc_s2a3','pgw_egtpc_s2a4','pgw_egtpc_s2a5','pgw_egtpc_s2a6',
			'pgw_egtpc_s2a7','pgw_egtpc_s2a8','pgw_egtpc_s2a9','pgw_egtpc_s2aA','pgw_egtpc_s2aB',
			'pgw_egtpc_s2b1','pgw_egtpc_s2b2','pgw_egtpc_s2b3','pgw_egtpc_s2b4','pgw_egtpc_s2b5',
			'pgw_egtpc_s2b6','pgw_egtpc_s2b7','pgw_egtpc_s2b8','pgw_egtpc_s2b9','pgw_egtpc_s2bA','pgw_egtpc_s2bB',
			'pgw_egtpc_s2bC','pgw_egtpc_s2bD',
			'pgw_egtpc_s5s81','pgw_egtpc_s5s82','pgw_egtpc_s5s83','pgw_egtpc_s5s84','pgw_egtpc_s5s85','pgw_egtpc_s5s86',
			'pgw_egtpc_s5s87','pgw_egtpc_s5s88','pgw_egtpc_s5s89','pgw_egtpc_s5s8A','pgw_egtpc_s5s8B','pgw_egtpc_s5s8C',
			'pgw_egtpc_s5s8D','pgw_egtpc_s5s8E','pgw_egtpc_s5s8F','pgw_egtpc_s5s8G','pgw_egtpc_s5s8H','pgw_egtpc_s5s8I',
			'pgw_egtpc_s5s8J','pgw_egtpc_s5s8K','pgw_egtpc_s5s8L','pgw_egtpc_s5s8M',
			'apn_qci1','apn_qci2',
			'P2P1',
			'RADIUS',
			'RADIUSGroup',
			'RADIUS',
			)

			
conf_lines = []
try:
	config	= open('config.cfg','r')
	lines	= config.readlines()
	config.close()
	for i in lines:
		if re.search(r'.schema.',i[:40]):
			i = i.replace("\t","")
			i = i.strip()
			i = i.replace("%","")
			# system schema
			if re.search(r'^schema',i):
				vars = i.split(" ")
				if vars[1] in sys_schemas:
					vals = i.split(" ")
					conf_lines.append(vals[len(vals)-1])
			# <name> schema
			else:
				# schema name	[ first ]
				# misc
				# config		[ last ]
				vars = i.split(" ")
				if vars[0] in schemas:
					#i = i.replace("%","")
					vals = i.split(" ")
					conf_lines.append(vals[len(vals)-1])
except:
	error = False
	
def read_file(filename):
	error = 0
	try:
		bulkstats = open(filename,'r')
		lines = bulkstats.readlines()
		bulkstats.close()
		sqls = []
		for line in lines:
			line = line.replace("\r","")
			line = line.replace("\n","")
			line = line.replace("\t","")
			line_def = line[:30].split(",")
			for conf_line in conf_lines:
				conf_line_attr = conf_line[:30].split(",")
				# EMS		[ 0 ]
				# <name>	[ 1 ]
				# misc		[ 2 ]
				# For weird configuration
				if re.search(r'samog',conf_line_attr[2]) or re.search(r'epdg',conf_line_attr[2]):
					if conf_line_attr[1] == line_def[1] and conf_line_attr[2] == line_def[2]:
						if line_def[1] in snames:
							sql = go_insert(line_def[1],conf_line,line,node)
							if sql:
								try:								
									oscmd = """echo '%s' >>__data""" % sql
									os.system(oscmd)
								except:
									error += 1				
				# For normal configuration
				else:				
					if line_def[0] == conf_line_attr[0] and line_def[1] == conf_line_attr[1]:
						#vals = line.split(",")
						#
						if line_def[1] in snames:
							sql = go_insert(line_def[1],conf_line,line,node)
							if sql:
								try:								
									oscmd = """echo '%s' >>__data""" % sql
									os.system(oscmd)
								except:
									error += 1
	except:
		print sys.exc_info()
		print line
	if error > 0:
		return False
	else:
		return True
		
files = [f for f in os.listdir('.') if path.isfile(f)]
files.sort()
err_files = []
exec_count = 0
sqls = []
good = 0
bad = 0
for i in files:
	if re.search(r'^JO2.{1,30}txt',i):
		result = read_file(i)
		if result is True:
			try:
				oscmd = "curl -i -XPOST 'http://10.0.1.10:8086/write?db=bulkstats' --data-binary @__data"
				p = subprocess.Popen([oscmd], shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				out, err = p.communicate()
				if re.search(r'HTTP.1.1.204.No.Content',str(out)):
					good += 1
				else:
				#	print out,err
					bad += 1
				#pass
			except:
				print "  >> Can't process file: %s" %i
		else:
			print "  >> Failed to analyze file: %s" %i

		exec_count += 1
		sys.stdout.write(" Execution in progress .. %s%% (%s/%s) | Good: %s  ..  Bad: %s\r" %((round((exec_count / float(len(files)-7/100)),1)),exec_count,len(files),good,bad))
		sys.stdout.flush()
	oscmd = """rm -f __data"""
	os.system(oscmd)	
sys.stdout.flush()
print(" Execution done! | Good: %s  ..  Bad: %s\r" %(good,bad))
